# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#import modules
import os
import csv

#set variables
csvpath = budget_data.csv
total_months =
current_month
last_month
net_total =
average_change =
daily_change = 
greatest_increase =
greatest_decrease =

#read csv
with open(csvpath, newline='') as handler:
	budget_data = csv.reader(handler)
	header = next(budget_data) 

#loop through data and count months, don't count header
#loop through and sum colum of profit and loss
	for row in budget_data
	

#calculate average profit and loss


#loop through calculate daily change, store daily change, identiy max and min


#print outputs
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:
print(f"Total: $
print(f"Average Change: $
print(f"Greatest Increase in Profits:
print(f"Greatest Decrease in Profits:

#write to txt file
output_path = 

with open(, 'w') as handler:
	handler.write("Financial Analysis")
	handler.write("----------------------------")
	handler.write(f"Total Months:")
	handler.write(f"Total: $")
	handler.write(f"Average Change: $")
	handler.write(f"Greatest Increase in Profits: ")
	handler.write(f"Greatest Decrease in Profits: ")

