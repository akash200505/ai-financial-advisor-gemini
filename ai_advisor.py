def generate_advice(financial_data, goal, risk):

    savings = financial_data["savings"]
    savings_ratio = financial_data["savings_ratio"]

    advice = ""

    if savings <= 0:
        advice += "You are spending more than your income. Reduce your expenses.\n\n"
    elif savings_ratio < 0.2:
        advice += "Try to save at least 20% of your income.\n\n"
    else:
        advice += "Good job! You are saving well.\n\n"

    if goal == "Emergency Fund":
        advice += "Build at least 6 months of expenses as an emergency fund.\n"

    elif goal == "Wealth Creation":
        advice += "Consider investing in SIP and long-term equity funds.\n"

    elif goal == "Retirement Planning":
        advice += "Start retirement investments like NPS or PPF.\n"

    if risk == "Low":
        advice += "\nChoose low-risk options like Fixed Deposits or Debt Funds."
    elif risk == "Medium":
        advice += "\nBalanced mutual funds are suitable."
    elif risk == "High":
        advice += "\nEquity mutual funds or stocks may suit you."

    return advice