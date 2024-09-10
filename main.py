from utils import load_data, calculate_total_expenses, calculate_savings, filter_by_location, average_expenses, save_data

# Define the file path
file_path = r'C:\Users\GOD\family_budget_app\family_budget.csv'
output_path = r'C:\Users\GOD\family_budget_app\processed_family_budget.csv'

# Load the data
df = load_data(file_path)

# Calculate total expenses and savings
df = calculate_total_expenses(df)
df = calculate_savings(df)

# Filter data for a specific location (e.g., Salem)
df_salem = filter_by_location(df, 'Salem')

# Calculate average expenses
avg_expenses = average_expenses(df)
print("Average Expenses:\n", avg_expenses)

# Save the processed data
save_data(df, output_path)
