import streamlit as st

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config(page_title="AI Financial Advisor", layout="centered")
st.title("💰 AI Financial Advisor & Goal Planner")

# -------------------------------
# Income & Expense Section
# -------------------------------
st.header("📊 Financial Details")

income = st.number_input("Monthly Income (₹)", min_value=0.0)
expenses = st.number_input("Monthly Expenses (₹)", min_value=0.0)

savings = income - expenses

st.write(f"💾 Monthly Savings: ₹ {savings:.2f}")

# -------------------------------
# Simple Chatbot Function
# -------------------------------
def get_chatbot_response(message, income, expenses):
    savings = income - expenses
    
    if savings <= 0:
        return "⚠️ You are not saving money. Try reducing expenses."
    elif "save" in message.lower():
        return f"✅ You are saving ₹{savings:.2f} per month. Keep investing wisely!"
    elif "invest" in message.lower():
        return "📈 Consider SIP, Mutual Funds, or Fixed Deposits."
    else:
        return "🤖 I recommend budgeting properly and investing regularly."

# -------------------------------
# Chatbot Section
# -------------------------------
st.header("💬 Financial Chatbot")

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

# -------------------------------
# Goal Planning Section
# -------------------------------
st.header("🎯 Advanced Goal Planning")

goal_name = st.text_input("Enter Your Personal Goal (e.g., Buy Car, Higher Studies)")
target_amount = st.number_input("Target Amount (₹)", min_value=0.0)
years = st.number_input("Years to Achieve Goal", min_value=1)

if st.button("Generate Goal Plan"):
    
    if target_amount > 0 and years > 0:
        monthly_required = target_amount / (years * 12)

        st.subheader("📈 Goal Plan Summary")
        st.write(f"🎯 Goal: {goal_name}")
        st.write(f"💰 Target Amount: ₹ {target_amount:.2f}")
        st.write(f"⏳ Time: {years} years")
        st.write(f"📌 Required Monthly Investment: ₹ {monthly_required:.2f}")

        if monthly_required > savings:
            st.error("⚠️ Your current savings are not enough to achieve this goal.")
            st.write("Suggestion: Increase income or reduce expenses.")
        else:
            st.success("✅ You can achieve this goal with disciplined investing!")

    else:
        st.warning("Please enter valid goal details.")
