import os
import csv

# Define the path to the input CSV file
input_file = os.path.join("Resources", "budget_data.csv")

# Initialize variables to store financial analysis results
total_months = 0
net_total = 0
previous_profit_losses = None
profit_losses_changes = []
months_list = []

# Open and read the CSV file
with open(input_file, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        if len(row) > 1:
            # Increment the total months count
            total_months += 1

            # Extract date and profit/loss from the row
            date = row[0]
            profit_losses = int(row[1])

            # Calculate the net total
            net_total += profit_losses

            # Calculate profit/loss changes
            if previous_profit_losses is not None:
                profit_losses_change = profit_losses - previous_profit_losses
                profit_losses_changes.append(profit_losses_change)
                months_list.append(date)

            previous_profit_losses = profit_losses

# Calculate the average of profit/loss changes
average_change = sum(profit_losses_changes) / len(profit_losses_changes)

# Find the greatest increase and decrease in profits
max_increase = max(profit_losses_changes)
max_decrease = min(profit_losses_changes)

max_increase_index = profit_losses_changes.index(max_increase)
max_decrease_index = profit_losses_changes.index(max_decrease)

max_increase_month = months_list[max_increase_index]
max_decrease_month = months_list[max_decrease_index]

# Prepare the financial analysis report
Full_Text = f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {max_increase_month} (${max_increase})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})
'''

print(Full_Text)

#Define the path to the output text file
output_file = "./Analysis/financial_analysis.txt"

#Write the financial analysis report to a text file
with open(output_file, 'w') as f:
     f.write(Full_Text)

     