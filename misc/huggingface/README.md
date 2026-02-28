# Step-by-step setup


1. Go to https://huggingface.co/new-space

2. Choose Docker / Streamlit as SDK → name it whatever (e.g. g32-grill-display-chat)

3. Add your free Groq API key (no one will see it):
   In your Space → Settings → Secrets
   - Add new secret:
   - Name: GROQ_API_KEY Value: your key from console.groq.com (free tier is very generous)

4. In the new Space, create replace these files with the given contnents:

   - requirements.txt
   - src/streamlit_app.py

5. Commit → the Space auto-builds and goes live in ~1–2 minutes.