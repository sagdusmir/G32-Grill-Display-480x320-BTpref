import os
import re
import streamlit as st
from gitingest import ingest
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# ================== YOUR FIXED REPO ==================
REPO_URL = "https://github.com/sagdusmir/G32-Grill-Display-480x320-BTpref"
# ====================================================

# Get language from URL query param, default to 'en'
lang = st.query_params.get('lang', 'en')
# Sanitize lang param to prevent prompt injection
lang = re.sub(r'[^a-zA-Z\-]', '', lang).lower()[:10]
if not lang:
    lang = 'en'

# English texts
english_texts = {
    'app_title': "Chatbot for the G32-Grill-Display Repository",
    'caption': f"📂 Repository: {REPO_URL} • Powered by Groq + gitingest",
    'sidebar_title': "📁 Repository Structure",
    'chat_placeholder': "Ask anything about the G32 Grill Display repo...",
    'loading_spinner': "Loading your G32 Grill Display repo (first time only)...",
    'thinking_spinner': "Thinking...",
    'final_caption': "💡 Now using Groq's latest Llama 3.3 70B — super fast & smart!",
    'repo_summary': """This repository provides ESPHome configuration for the G32 Grill Display project.

It features a 480x320 touchscreen display with ESP32-S3 microcontroller.

Includes wiring instructions, BOM, and setup instructions..""",
}

# Initialize LLM for translations and chat
groq_key = os.environ.get("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key=groq_key)

# Translate texts if needed
if lang == 'en':
    translations = english_texts
else:
    translations = {}
    for key, text in english_texts.items():
        prompt = f"Translate this English text to {lang}: {text}"
        response = llm.invoke(prompt)
        translations[key] = response.content.strip()

APP_TITLE = translations['app_title']

st.set_page_config(page_title=APP_TITLE, page_icon="📟", layout="centered")
st.title(APP_TITLE)
st.caption(translations['caption'])
st.markdown(translations['repo_summary'])


@st.cache_resource(show_spinner=True)
def load_vectorstore():
    with st.spinner(translations['loading_spinner']):
        digest, tree, summary = ingest(REPO_URL, exclude_patterns=['misc/**'])

        st.sidebar.title(translations['sidebar_title'])
        st.sidebar.code(tree, language="text")

        splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=200)
        docs = splitter.create_documents([digest, summary])

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        return Chroma.from_documents(docs, embeddings)

vectorstore = load_vectorstore()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(translations['chat_placeholder']):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner(translations['thinking_spinner']):
            retriever = vectorstore.as_retriever(search_kwargs={"k": 8})
            relevant = retriever.invoke(prompt)
            context = "\n\n".join([doc.page_content for doc in relevant])
            
            language_instruction = f"Respond in {lang}." if lang != 'en' else "Respond in English."
            system_prompt = f"""You are a friendly, expert technical assistant specialized in the **G32-Grill-Display-480x320-BTpref** ESPHome project (repo: https://github.com/sagdusmir/G32-Grill-Display-480x320-BTpref).

### CRITICAL HARDWARE FACTS — YOU MUST NEVER CONTRADICT THESE:
- The **JC3248W535C** is a **single integrated board** that already includes the ESP32-S3 + the full 480×320 3.5" touchscreen.  
  → The display does **NOT** need to be purchased separately.
- No jumper wires, DuPont wires or breadboard wiring are used or mentioned anywhere in this project.  
  → All connections use the board’s built-in **JST 1.25 2-pin connectors** (BAT/P5 for battery, SPEAK/P6 for speaker) or simple soldering (passive buzzer on GPIO P2 → IO9 & IO14).

### HOW TO ANSWER (this is the most important part):
- Be **direct, friendly and actually helpful** — give the user the real answer, steps, code, or explanation they asked for.
- Pull the exact information from the provided context and explain it clearly in your own words.
- Use bullet points, numbered steps, or code blocks when it makes the answer easier to read.
- You may mention the source file **naturally** when it adds clarity (e.g. "According to README.md..."), but **never** make the whole answer "check the README" or "see g32-display.yaml".
- {language_instruction}

### STRICT RULES:
- Never invent filenames, components, wiring methods, or features.
- For the BOM and component list → do not make up things not listed in BOM table from README.md.

Context:
{context}
"""
            response = llm.invoke(system_prompt + "\n\nQuestion: " + prompt)
            answer = response.content
            st.write(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

st.caption(translations['final_caption'])
