import os
import csv

#Create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#Define PyBank's variables
months = []
profit = []
profit_changes = []
count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_change = 0

#Define path of csv file
pybank_csv_path = os.path.join("Resources", "budget_data.csv")

#Open csv with path pybank_csv_path
with open(pybank_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:
        print(row, type(row))
        count_months += 1
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss
        if (count_months == 1):
            #Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:
            #Compute change in profit loss 
            profit_change = current_month_profit_loss - previous_month_profit_loss
            #Append each month to the months[]
            months.append(row[0])
            #Append each profit_change to the profit_changes[]
            profit_changes.append(profit_change)
            #Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #Sum and average of changes in "profit/losses" 
    sum_profit_loss = sum(profit_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    #Highest and lowest of changes in "profit/losses" 
    highest_change = max(profit_changes)
    lowest_change = min(profit_changes)

    #Index value of highest and lowest changes in "profit/losses" 
    highest_month_index = profit_changes.index(highest_change)
    lowest_month_index = profit_changes.index(lowest_change)

    #Best and worst months
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")
