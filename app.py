import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Financial Advisor Pro", page_icon="💰", layout="centered")
st.title("💰 AI Financial Advisor Pro")

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🎯 Goal Planner", "💬 Chatbot"])

# =========================================================
# 📊 DASHBOARD TAB
# =========================================================
with tab1:

    st.header("📊 Financial Overview")

    income = st.number_input("Monthly Income (₹)", min_value=0.0)
    expenses = st.number_input("Monthly Expenses (₹)", min_value=0.0)

    savings = income - expenses

    st.write(f"💾 Monthly Savings: ₹ {savings:.2f}")

    if expenses > 0:
        emergency_fund = expenses * 6
        st.info(f"🛡 Recommended Emergency Fund (6 months): ₹ {emergency_fund:.2f}")

    # Pie Chart
    if income > 0:
        fig, ax = plt.subplots()
        ax.pie([expenses, savings], labels=["Expenses", "Savings"], autopct="%1.1f%%")
        ax.set_title("Income Distribution")
        st.pyplot(fig)


# =========================================================
# 🎯 GOAL PLANNER TAB
# =========================================================
with tab2:

    st.header("🎯 Smart Goal Planner")

    goal_name = st.text_input("Enter Your Goal (e.g., Car, Higher Studies)")
    target_amount = st.number_input("Target Amount (₹)", min_value=0.0)
    years = st.number_input("Years to Achieve Goal", min_value=1)

    risk = st.selectbox("Select Risk Level", ["Low (8%)", "Medium (12%)", "High (15%)"])

    # Risk based return
    if "8%" in risk:
        rate = 0.08
    elif "12%" in risk:
        rate = 0.12
    else:
        rate = 0.15

    if st.button("Generate Smart Plan"):

        months = years * 12
        monthly_rate = rate / 12

        if target_amount > 0:

            # SIP Formula
            sip = target_amount * monthly_rate / ((1 + monthly_rate) ** months - 1)

            st.subheader("📈 Goal Plan Summary")
            st.write(f"🎯 Goal: {goal_name}")
            st.write(f"💰 Target: ₹ {target_amount:,.2f}")
            st.write(f"⏳ Time: {years} years")
            st.write(f"📊 Assumed Return: {rate*100:.0f}%")
            st.write(f"💳 Required Monthly SIP: ₹ {sip:,.2f}")

            if sip > savings:
                st.error("⚠ Your current savings are not enough for this goal.")
            else:
                st.success("✅ You can achieve this goal with disciplined investing!")

            # Growth Chart
            investment = []
            total = 0

            for i in range(months):
                total = (total + sip) * (1 + monthly_rate)
                investment.append(total)

            df = pd.DataFrame({
                "Month": range(1, months + 1),
                "Investment Value": investment
            })

            st.line_chart(df.set_index("Month"))

        else:
            st.warning("Please enter valid target amount.")


# =========================================================
# 💬 CHATBOT TAB
# =========================================================
with tab3:

    st.header("💬 Financial Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_message = st.text_input("Ask your financial question:")

    def simple_bot(message):
        msg = message.lower()
        if "save" in msg:
            return "Try following 50-30-20 budgeting rule."
        elif "invest" in msg:
            return "Consider SIP in Mutual Funds for long-term wealth creation."
        elif "loan" in msg:
            return "Avoid high-interest loans and maintain good credit score."
        else:
            return "Focus on budgeting, saving, and long-term investing."

    if st.button("Send"):
        if user_message:
            reply = simple_bot(user_message)
            st.session_state.chat_history.append(("You", user_message))
            st.session_state.chat_history.append(("Bot", reply))

    for sender, msg in st.session_state.chat_history:
        st.write(f"**{sender}:** {msg}")
