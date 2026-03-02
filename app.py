import streamlit as st
import os
from finance_analysis import calculate_financials
from ai_advisor import generate_advice
from visualization import show_chart
from utils import format_currency

# ==============================
# PAGE CONFIG (MUST BE FIRST)
# ==============================
st.set_page_config(page_title="AI Financial Advisor", page_icon="💰")

# ==============================
# LOAD CSS
# ==============================
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ==============================
# TITLE SECTION
# ==============================
st.markdown('<div class="main-title">💰 AI Financial Advisor</div>', unsafe_allow_html=True)
st.markdown('<div class="subheading">Plan smarter. Invest better. Save consistently.</div>', unsafe_allow_html=True)

# ==============================
# SIDEBAR INPUTS
# ==============================
st.sidebar.header("📊 Financial Details")

income = st.sidebar.number_input("Monthly Income (₹)", min_value=0.0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0.0)

goal = st.sidebar.selectbox(
    "Investment Goal",
    ["Emergency Fund", "Wealth Creation", "Retirement Planning"]
)

risk = st.sidebar.selectbox(
    "Risk Preference",
    ["Low", "Medium", "High"]
)

# ==============================
# ANALYZE BUTTON
# ==============================
if st.sidebar.button("Analyze & Advise"):

    # Calculate financial metrics
    result = calculate_financials(income, expenses)
    savings = result["savings"]

    # Show results in card
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📈 Financial Overview")

    st.write(f"💵 Savings: {format_currency(savings)}")
    st.write(f"📊 Savings Ratio: {result['savings_ratio']*100:.2f}%")
    st.write(f"📉 Expense Ratio: {result['expense_ratio']*100:.2f}%")

    st.markdown("</div>", unsafe_allow_html=True)

    # Progress bar
    st.subheader("💹 Savings Progress")
    st.progress(min(result["savings_ratio"], 1.0))

    # Metrics display
    col1, col2 = st.columns(2)
    col1.metric("Monthly Income", format_currency(income))
    col2.metric("Monthly Expenses", format_currency(expenses))

    # Chart
    st.subheader("📊 Income vs Expenses vs Savings")
    show_chart(income, expenses, savings)

    # AI Advice
    st.subheader("🤖 AI Financial Advice")
    advice = generate_advice(income, expenses, goal, risk)
    st.success(advice)
# ==============================
# CHATBOT SECTION
# ==============================

st.subheader("💬 Financial Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_message = st.text_input("Ask your financial question:")

if st.button("Send"):
    if user_message:
        bot_reply = get_chatbot_response(user_message, income, expenses)
        st.session_state.chat_history.append(("You", user_message))
        st.session_state.chat_history.append(("Bot", bot_reply))

for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
# 🎯 Activity 3.5 – Goal-Oriented Planning
# ===================================

st.markdown("---")
st.header("🎯 Advanced Goal Planning")

goal_name = st.text_input("Enter Your Personal Goal (e.g., Buy Car, Higher Studies)")
target_amount = st.number_input("Target Amount (₹)", min_value=0.0)
years = st.number_input("Years to Achieve Goal", min_value=1)

if st.button("Generate Goal Plan"):

    if target_amount > 0 and financial_data["income"] > 0:

        monthly_required = target_amount / (years * 12)

        st.subheader("📊 Goal Plan Summary")

        st.write(f"🎯 Goal: {goal_name}")
        st.write(f"💰 Target Amount: ₹ {target_amount:,.2f}")
        st.write(f"⏳ Time: {years} years")
        st.write(f"📌 Required Monthly Investment: ₹ {monthly_required:,.2f}")

        if monthly_required > financial_data["savings"]:
            st.error("⚠ Your current savings are not enough to achieve this goal.")
            st.write("Suggestion: Increase income or reduce expenses.")
        else:
            st.success("✅ You can achieve this goal with disciplined investing!")

    else:
        st.warning("Please enter valid goal details.")
