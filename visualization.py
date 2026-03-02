import streamlit as st

def show_chart(income, expenses, savings):

    st.markdown("### 📊 Income vs Expenses vs Savings")

    chart_data = {
        "Income": income,
        "Expenses": expenses,
        "Savings": savings
    }

    st.bar_chart(chart_data)