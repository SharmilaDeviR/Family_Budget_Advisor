# app.py

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title and description
st.title("AI-Powered Family Budget Planner")
st.write("This app helps families plan their budget by analyzing income, expenses, and suggesting savings.")

# Load Dataset
uploaded_file = st.file_uploader("Upload your family budget CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.write(data.head())

    # Data Analysis
    st.write("## Analyze Your Budget")
    income_column = st.selectbox("Select the income column", data.columns)
    expense_columns = st.multiselect("Select expense columns", data.columns)
    
    if income_column and expense_columns:
        total_income = data[income_column].sum()
        total_expenses = data[expense_columns].sum().sum()

        # Display Summary
        st.write(f"Total Income: ${total_income:.2f}")
        st.write(f"Total Expenses: ${total_expenses:.2f}")
        st.write(f"Net Savings: ${total_income - total_expenses:.2f}")
        
        # Recommendation
        st.write("## Budget Recommendations")
        savings_goal = st.slider("Set your savings goal percentage", min_value=0, max_value=100, value=20)
        recommended_savings = total_income * (savings_goal / 100)
        st.write(f"To achieve a savings goal of {savings_goal}%, you should save: ${recommended_savings:.2f}")

        if total_income - total_expenses < recommended_savings:
            st.write("**Recommendation:** Consider reducing your expenses or increasing your income to meet your savings goal.")
        else:
            st.write("**Great job!** You are on track to meet your savings goal.")
else:
    st.write("Please upload a budget CSV file to analyze your family's budget.")

