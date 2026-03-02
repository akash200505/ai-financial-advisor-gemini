def get_chatbot_response(user_input, income, expenses):
    savings = income - expenses
    user_input = user_input.lower()

    if "save" in user_input:
        return f"You are currently saving ₹{savings:.2f} per month."

    elif "investment" in user_input:
        if savings > 10000:
            return "You can consider mutual funds or SIP investments."
        else:
            return "Try increasing your savings before investing aggressively."

    elif "emergency" in user_input:
        return "You should maintain 6 months of expenses as an emergency fund."

    elif "retirement" in user_input:
        return "Start long-term SIP investments for retirement planning."

    elif "hi" in user_input or "hello" in user_input:
        return "Hello! I am your AI Financial Assistant. Ask me about savings, investments, or retirement."

    else:
        return "I can help with savings, investment, emergency fund, and retirement advice."