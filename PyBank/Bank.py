import csv
import math
from dateutil.relativedelta import relativedelta
from datetime import date
read_fpath = ("C:/Users/panka/OneDrive/Desktop/Class Folder/Github/python-challenge/PyBank/Resources/budget_data.csv")
Date = []
Profit_losses = []
Profit_losses_a = []
Profit_losses_b = []
Change_profit_losses = [] 
Net_total_amount = 0
sum_of_change = 0
with open(read_fpath, 'r') as f: 
    reader = csv.reader(f, delimiter=',')
    for row in reader: 
        #print(row[0], row[1])
        Date.append(row[0])
        Profit_losses.append(row[1])
        # * The total number of months included in the dataset
    for x in range(1, len(Date)):
        Total_months = x
        x = x + 1
    for x in range(1, len(Profit_losses)):
        Net_total_amount = Net_total_amount + int(Profit_losses[x])
        Profit_losses_a.append(Profit_losses[x])
    Profit_losses_a = Profit_losses_a[:-1]
    for y in range(2, len(Profit_losses)):
        Profit_losses_b.append(Profit_losses[y])
        # Made two list A profit loss a and B profit loss 2
    for i in range(0, len(Profit_losses_a)):
        Change_profit_losses.append(int(Profit_losses_b[i]) - int(Profit_losses_a[i]))
        sum_of_change = (sum_of_change + int(Change_profit_losses[i]))
    Average_change = (sum_of_change/85) 
    #  The greatest increase in profits (date and amount) over the entire period
    greatest_increase_profits = max(Change_profit_losses)
    greatest_decrease_profits = min(Change_profit_losses)
# print(Change_profit_losses)
print(f"The total number of months included in the dataset is = {Total_months}")
print(f"Total Net total amount is = {Net_total_amount}")
print(f"Total Average change is = {Average_change}")
print(f"Greatest Increase in Profits = {greatest_increase_profits}")
print(f"Greatest Decrease in Profits = {greatest_decrease_profits}")


  
         

    
