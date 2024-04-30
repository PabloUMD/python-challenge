import pandas as pd
import os

# Define the file path for the CSV
file_path = 'PyBank/Resources/budget_data.csv'  

# Load the data from your CSV file
data = pd.read_csv(file_path)

# Calculate the total number of months included in the dataset
total_months = data.shape[0]

# Calculate the net total amount of "Profit/Losses" over the entire period
total_profit_losses = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()

# Determine the greatest increase in profits (date and amount) over the entire period
greatest_increase = data.loc[data['Change'].idxmax()]
greatest_increase_date = greatest_increase['Date']
greatest_increase_amount = greatest_increase['Change']

# Determine the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = data.loc[data['Change'].idxmin()]
greatest_decrease_date = greatest_decrease['Date']
greatest_decrease_amount = greatest_decrease['Change']

# Prepare the results for display and output to a file
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase_amount)})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease_amount)})\n"
)

# Print the results to the terminal
print(results)

# Determine the path to save the text file in the same directory as the CSV file
output_path = os.path.join(os.path.dirname(file_path), 'financial_analysis_results.txt')

# Write the results to a text file at the determined path
with open(output_path, 'w') as file:
    file.write(results)


