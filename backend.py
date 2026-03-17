from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import requests
import os

app = FastAPI()

# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "Backend working"}

# ---------------- BUDGET ----------------
@app.post("/analyze-budget")
def analyze_budget():
    try:
        df = pd.read_csv("data.csv")
    except:
        return {"error": "data.csv not found"}

    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    savings = total_revenue - total_expenses

    return {
        "revenue": int(total_revenue),
        "expenses": int(total_expenses),
        "savings": int(savings),
        "insight": "Try reducing unnecessary expenses by 10-15% and optimize operational costs."
    }

# ---------------- AI CHAT ----------------
@app.post("/chat")
def chat(query: str):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert AI business consultant. Give clear, practical, high-value startup advice."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            return {
                "response": result["choices"][0]["message"]["content"]
            }
        else:
            return {
                "response": f"API Error: {result}"
            }

    except Exception as e:
        return {"response": f"Error: {str(e)}"}

# ---------------- PREDICTION ----------------
@app.get("/predict")
def predict():
    try:
        df = pd.read_csv("data.csv")
    except:
        return {"error": "data.csv not found"}

    X = np.array(range(len(df))).reshape(-1, 1)
    y = df["Revenue"]

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(df)]])[0]

    return {"prediction": float(prediction)}