def calculate_financials(income, expenses):

    savings = income - expenses

    savings_ratio = savings / income if income > 0 else 0
    expense_ratio = expenses / income if income > 0 else 0

    emergency_fund_target = expenses * 6

    return {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "savings_ratio": savings_ratio,
        "expense_ratio": expense_ratio,
        "emergency_fund_target": emergency_fund_target
    }