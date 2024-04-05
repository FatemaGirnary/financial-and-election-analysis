#Your task is to create a Python script that analyses the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#file path
csvpath = os.path.join('Resources','budget_data.csv')
#output file path
output_file = "Financial Analysis.txt" 


total_months = 0
net_total = 0
prev_profit_loss = 0
total_changes = 0
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}
changes = []

# Read the CSV file
with open(csvpath, 'r') as file:
    csv_reader = csv.DictReader(file)

#Iterate through each row
    for row in csv_reader:

#Extract date and profit/losses
        date = row['Date']
        profit_loss = int(row['Profit/Losses'])

# Calculate total number of months from each row of data after the header
        total_months += 1

#Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += profit_loss

#Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            total_changes += change
            changes.append(change)

#The greatest increase in profits (date and amount) over the entire period
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

#The greatest decrease in profits (date and amount) over the entire period
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        prev_profit_loss = profit_loss

# Calculate the average of those changes
average_change = total_changes / (total_months-1)

#print results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

#output results in a text file
with open(output_file, 'w') as output:
        output.write("Financial Analysis\n")
        output.write("--------------------\n")
        output.write(f"Total Months: {total_months}\n")
        output.write(f"Total: ${net_total}\n")
        output.write(f"Average Change: ${average_change: .2f}\n")
        output.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        output.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print("Election results have been saved to 'election_results.txt'")