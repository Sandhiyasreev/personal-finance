import streamlit as st
from advisor import rule_based_advice
from clustering import get_cluster
from charts import (
    savings_vs_debt_pie,
    savings_projection_chart,
    financial_health_score_chart
)
from report import create_pdf

st.set_page_config(page_title="AI Personal Finance Advisor", layout="wide")
st.title("💼 AI Personal Finance Advisor")

# 📥 User Input Form
with st.form("user_input"):
    name = st.text_input("👤 Your Name", placeholder="e.g., Sandhiya Sree")
    income = st.number_input("Monthly Income", min_value=1000)
    expenses = st.number_input("Monthly Expenses", min_value=0)
    savings = st.number_input("Current Savings", min_value=0)
    debts = st.number_input("Current Debts", min_value=0)
    age = st.slider("Your Age", 18, 70)
    goal = st.text_input("Your Financial Goal (Type anything)", placeholder="e.g., Start a business, Save for wedding")
    risk = st.selectbox("Risk Appetite", ["Low", "Medium", "High"])
    submit = st.form_submit_button("Get Advice")

# 🧠 Financial Health Score Logic
def calculate_financial_score(income, expenses, savings, debts):
    score = 0
    if savings >= 0.2 * income:
        score += 40
    if debts <= 0.3 * income:
        score += 30
    if expenses <= 0.7 * income:
        score += 20
    score += 10
    return min(score, 100)

# 🚀 On Submit
if submit:
    user = {
        "name": name,
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "debts": debts,
        "age": age,
        "goal": goal.strip(),
        "risk_appetite": risk
    }

    advice = rule_based_advice(user)
    cluster = get_cluster(income, expenses, savings)
    score = calculate_financial_score(income, expenses, savings, debts)

    # Generate Charts
    pie_fig = savings_vs_debt_pie(savings, debts)
    trend_fig = savings_projection_chart(income, expenses, savings)

    # Save chart images
    pie_fig.savefig("pie.png", format="png")
    trend_fig.savefig("trend.png", format="png")

    # Generate PDF instantly
    create_pdf(advice, name=user['name'], pie_img_path="pie.png", trend_img_path="trend.png")

    # Show All Output in Tabs
    tab1, tab2, tab3 = st.tabs(["📥 Input Summary", "📊 Charts & Advice", "📄 PDF Report"])

    with tab1:
        st.subheader("📋 Your Input Summary")
        st.write(f"**Name:** {user['name']}")
        st.write(f"**Income:** ₹{income}")
        st.write(f"**Expenses:** ₹{expenses}")
        st.write(f"**Savings:** ₹{savings}")
        st.write(f"**Debts:** ₹{debts}")
        st.write(f"**Age:** {age}")
        st.write(f"**Goal:** {goal}")
        st.write(f"**Risk Appetite:** {risk}")

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Savings vs Debts")
            st.pyplot(pie_fig)

        with col2:
            st.subheader("🧠 Financial Health Score")
            st.plotly_chart(financial_health_score_chart(score))

        st.subheader("📈 Savings Projection")
        st.pyplot(trend_fig)

        st.subheader("💡 Personalized Advice")
        for tip in advice:
            st.write("🔹", tip)

        st.success(f"👤 You are a **{cluster}** type user.")

    with tab3:
        st.subheader("📄 Download Your Financial Report")
        with open("financial_advice.pdf", "rb") as f:
            st.download_button("📥 Download PDF Report", f, file_name="financial_advice.pdf", mime="application/pdf")
