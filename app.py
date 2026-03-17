import streamlit as st
import requests
import plotly.express as px
import pandas as pd
from fpdf import FPDF
import time

# (Optional voice)
try:
    import speech_recognition as sr
    voice_available = True
except:
    voice_available = False

st.set_page_config(page_title="AI Business Assistant", layout="centered")

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}
h1, h2, h3 {
    color: #00f5ff;
}
.stButton>button {
    background: linear-gradient(90deg, #00f5ff, #00ff87);
    color: black;
    border-radius: 10px;
    font-weight: bold;
}
.stTextInput>div>div>input {
    background-color: #1e293b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Business Assistant")

# ---------------- VOICE FUNCTION ----------------
def get_voice_input():
    if not voice_available:
        return "Voice not available"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand audio"

# ---------------- BUDGET ----------------
st.subheader("Budget Analysis")

if st.button("Analyze Budget"):
    try:
        response = requests.post("http://127.0.0.1:8000/analyze-budget")
        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.success("Analysis Complete")
            st.write("Revenue:", data["revenue"])
            st.write("Expenses:", data["expenses"])
            st.write("Savings:", data["savings"])
            st.write("Insight:", data["insight"])

    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- DASHBOARD ----------------
st.subheader("Business Insights Dashboard")

try:
    df = pd.read_csv("data.csv")

    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    profit = total_revenue - total_expenses

    profit_margin = (profit / total_revenue) * 100
    expense_ratio = (total_expenses / total_revenue) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Revenue", total_revenue)
    col2.metric("Expenses", total_expenses)
    col3.metric("Profit", profit)

    st.write(f"Profit Margin: {profit_margin:.2f}%")
    st.write(f"Expense Ratio: {expense_ratio:.2f}%")

    fig = px.bar(df, x="Month", y=["Revenue", "Expenses"])
    st.plotly_chart(fig)

except:
    st.warning("No data available")

# ---------------- SIMULATION ----------------
st.subheader("Smart Business Simulation")

revenue = st.slider("Monthly Revenue", 1000, 50000, 10000)
expenses = st.slider("Monthly Expenses", 1000, 50000, 8000)

profit_sim = revenue - expenses
st.write("Profit:", profit_sim)

# ---------------- AI ----------------
st.subheader("AI Business Assistant")

mode = st.selectbox(
    "Choose AI Mode",
    ["Finance Advisor", "Marketing Expert", "Customer Support"]
)

query = st.text_input("Ask something")

if st.button("Speak"):
    query = get_voice_input()
    st.write("You said:", query)

if st.button("Ask AI"):
    if not query.strip():
        st.warning("Enter a question first")
    else:
        try:
            if mode == "Finance Advisor":
                system_prompt = "You are a financial advisor."
            elif mode == "Marketing Expert":
                system_prompt = "You are a marketing expert."
            else:
                system_prompt = "You are customer support."

            with st.spinner("Thinking..."):
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    params={"query": f"{system_prompt}\nUser: {query}"}
                )

            res_json = response.json()

            if "response" in res_json:
                answer = res_json["response"]
                st.success(answer)

                # PDF FIX
                filename = f"report_{int(time.time())}.pdf"
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, answer)
                pdf.output(filename)

                with open(filename, "rb") as f:
                    st.download_button("Download Report", f, file_name=filename)
            else:
                st.error(res_json)

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- PREDICTION ----------------
st.subheader("Future Prediction")

if st.button("Predict Next Month Revenue"):
    try:
        res = requests.get("http://127.0.0.1:8000/predict")
        data = res.json()

        if "prediction" in data:
            st.write("Predicted Revenue:", data["prediction"])
        else:
            st.error(data)

    except Exception as e:
        st.error(f"Error: {e}")