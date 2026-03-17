# AI Business Assistant

An AI-powered platform that helps startups analyze finances, simulate business scenarios, and make smart decisions using AI + Machine Learning.

---

## ✨ Features

*  Budget Analysis (Revenue, Expenses, Savings)
*  Interactive Business Dashboard (KPIs + Charts)
*  Future Scenario Simulation (Real-time sliders)
*  AI Decision Engine (Actionable recommendations)
*  Multi-role AI Assistant:

  * Finance Advisor
  * Marketing Expert
  * Customer Support
  *  Voice Input Support (optional)
  * AI Insights on Business Data
  *  Download AI Reports (PDF)
  *  Revenue Prediction using Machine Learning

---

## Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **ML Model:** Scikit-learn (Linear Regression)
* **AI API:** Groq (LLaMA models)
* **Data Handling:** Pandas, NumPy
* **Visualization:** Plotly

---

## Project Structure

```
ai-business-assistant/
│
├── backend.py
├── app.py
├── data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation & Setup (Run Locally)

### Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/ai-business-assistant.git
cd ai-business-assistant
```

---

### Create Virtual Environment (Recommended)

#### Windows:

```
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Set Up Environment Variables

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_api_key_here
```

 Replace with your actual Groq API key

---

### Run Backend (FastAPI)

```
uvicorn backend:app --reload
```

 Backend runs at:

```
http://127.0.0.1:8000
```

---

###  Run Frontend (Streamlit)

Open a new terminal and run:

```
streamlit run app.py
```

 App runs at:

```
http://localhost:8501
```

---

## Dataset Format (data.csv)

Your CSV should look like:

```
Month,Revenue,Expenses
Jan,100000,80000
Feb,120000,90000
Mar,150000,100000
...
```

---

## Optional Features Setup

### Voice Input (Optional)

If you want voice support:

```
pip install SpeechRecognition pyaudio
```

 Note:

* PyAudio may require additional setup on Windows

---

## Important Notes

* Do NOT upload your `.env` file to GitHub
* Make sure `data.csv` exists before running
* Backend must run before frontend

---

## 🚀 Future Improvements

* Cloud deployment (Streamlit Cloud / Render)
* Multi-user dashboards
* Real-time database integration
* Advanced ML forecasting models

---

##  Why This Project?

This project acts as a **complete AI Business Co-Pilot** —
combining analytics, prediction, and decision-making into one platform.

---

##  Author

Built with for innovation & hackathons

---

##  If you like this project

Give it a star on GitHub!
