# 🍏 adk-apple-intelligence (A Mock Siri That Actually Remembers)

This is a lightweight, Gemini-powered mock assistant built with **Google’s Agent Development Kit (ADK)** — inspired by Apple’s now-infamous Bella Ramsey ad, where Siri magically remembered “that guy from the café”… and then Apple quietly deleted the ad.

This mock project **does what the ad promised**, using:

- ✅ A simple tool-based architecture (contacts, calendar, emails)
- ✅ A Gemini 2.0 Flash model for generating responses
- ✅ Mock data to simulate realistic memory and context
- ✅ Google ADK for agent orchestration and a web chat UI

---

## 🧠 What It Can Do

Ask vague, human questions like:

> “What was the name of the guy I met a couple of months ago at Cafe Grenel?”

And it will figure out:

> “You met Zac Wingate on July 3rd at Cafe Grenel to discuss project milestones.”

It also supports:

- Listing users and retrieving contact info
- Searching calendar events (by time or location)
- Summarizing recent email messages
- Responding naturally using Gemini

---

## ⚙️ Installation & Setup

### 1. Clone and set up environment

```bash
git clone https://github.com/yourusername/apple-intelligence-agent.git
cd apple-intelligence-agent
python -m venv .venv
source .venv/bin/activate  # Or appropriate activation for your OS
```

### 2. Install ADK
```bash
pip install google-adk
```

### 3. Project structure
Make sure your folder looks like this:

```bash
apple-intelligence-agent/
└── apple_intelligence/
    ├── __init__.py
    ├── agent.py         # Your main agent logic (see code)
    └── .env             # Contains your Gemini API key
```

### 4. Add your API key
Get a Gemini API key from Google AI Studio and paste it into .env like so:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

5. Run the agent
From the parent directory:

```bash
adk web
```

Then open the link in your terminal (usually http://localhost:8000), select apple_intelligence in the top-left dropdown, and chat with your assistant.


✨ Why This Exists
This is a fun and slightly cheeky response to Apple’s over-promised ad. It's not production-ready—but it proves that real context-aware assistants are entirely doable with the right structure and tools.


📖 Blog Post
https://medium.com/@nilsonsaless/what-was-the-name-of-that-guy-rebuilding-apples-missing-intelligence-with-google-adk-23ff389ce354


🧩 License
MIT License. Build something smarter than a keynote demo.
