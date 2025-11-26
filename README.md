# ai-meditation-coach
An AI-powered meditation companion that guides short mindfulness sessions, tracks mood and stress, and helps users build a self-care habit.

Built with:
- A lightweight open-source LLM (`google/flan-t5-base`)
- Streamlit for the UI
- Simple analytics via session logs

---

## Overview

**AI Meditation Coach** is a small but complete product-style project:

- Guides 2–5 minute text-based meditations  
- Asks for a quick emotional check-in (mood, stress, energy)  
- Generates short affirmations and supportive messages  
- Logs each session (date, mood, stress, meditation type, rating)  
- Allows basic progress tracking over time (number of sessions, average stress, etc.)

It’s designed as a portfolio project that demonstrates:
- Prompt engineering for wellness / mental health
- Simple analytics and log-based insights
- Clean product-oriented UX with Streamlit

>  This project is **not** a replacement for professional mental health support.

---

##  Features

-  Guided meditation scripts generated dynamically
-  Mood & stress check-in before each session
-  Personalized affirmations based on user state
-  Session logs stored locally (`data/session_logs.csv`)
-  Basic analytics (sessions count, average stress, average rating) — ready to expand

---

##  Tech Stack

- **Language:** Python 3.10+
- **LLM:** `google/flan-t5-base` (Hugging Face Transformers)
- **UI:** Streamlit
- **Data:** CSV logs via `pandas`
- **Config:** `.env` with Hugging Face token
