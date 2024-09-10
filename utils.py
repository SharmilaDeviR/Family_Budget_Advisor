import pandas as pd

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(file_path)

def calculate_total_expenses(df):
    """Calculate total expenses for each month."""
    expense_columns = ['rent', 'groceries', 'transport', 'utilities', 'entertainment', 'healthcare']
    df['total_expenses'] = df[expense_columns].sum(axis=1)
    return df

def calculate_savings(df):
    """Calculate savings for each month."""
    df['savings'] = df['income'] - df['total_expenses']
    return df

def filter_by_location(df, location):
    """Filter the DataFrame by location."""
    return df[df['location'] == location]

def average_expenses(df):
    """Calculate average expenses for each category."""
    expense_columns = ['rent', 'groceries', 'transport', 'utilities', 'entertainment', 'healthcare']
    return df[expense_columns].mean()

def save_data(df, file_path):
    """Save the DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)
