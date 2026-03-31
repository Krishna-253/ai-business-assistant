# AI Business Assistant

> AI-powered business co-pilot for startups — budget analysis, revenue prediction (ML), scenario simulation, and multi-role AI assistant.

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red) ![Groq](https://img.shields.io/badge/Groq-LLM-purple)

---

## Features

- **Budget Analysis** — Revenue, expenses, and savings breakdown with visual charts
- **Revenue Prediction** — Machine learning model to forecast future revenue trends
- **Scenario Simulation** — Real-time sliders to simulate best/worst case business scenarios
- **AI Decision Engine** — Actionable recommendations powered by Groq LLM
- **Multi-role AI Assistant** — Switch between Finance Advisor, Marketing Expert, and Customer Support roles
- **Voice Input Support** — Optional voice-to-text for natural interaction
- **AI Business Reports** — Downloadable PDF reports with insights
- **Interactive KPI Dashboard** — Live charts and key performance indicators

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | FastAPI (Python) |
| AI/LLM | Groq API |
| ML | scikit-learn |
| Data | Pandas, CSV |

---

## Getting Started

### Prerequisites
- Python 3.10+
- Groq API Key

### Installation

```bash
git clone https://github.com/Krishna-253/ai-business-assistant
cd ai-business-assistant
pip install -r requirements.txt
```

### Run the App

```bash
# Start FastAPI backend
uvicorn backend:app --reload

# Start Streamlit frontend (in a new terminal)
streamlit run app.py
```

### Environment Variables

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

---

## Project Structure

```
ai-business-assistant/
├── app.py              # Streamlit frontend
├── backend.py          # FastAPI backend
├── data.csv            # Sample business data
├── requirements.txt    # Dependencies
└── .gitignore
```

---

## Built By

**Krishna Rai** — BTech AI/Data Science @ JIMS JEMTEC
GitHub: [Krishna-253](https://github.com/Krishna-253)
