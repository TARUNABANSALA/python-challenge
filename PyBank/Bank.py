import csv
import math
read_fpath = ("C:/Users/panka/OneDrive/Desktop/Class Folder/Github/python-challenge/PyBank/Resources/budget_data.csv")
Date = []
Profit_losses = []
Profit_losses_a = []
Profit_losses_b = []
change_profit_losses_list = [] 
Net_total_amount = 0
sum_of_change = 0
dictionary = {}
with open(read_fpath, 'r') as f: 
    reader = csv.reader(f, delimiter=',')
    for row in reader: 
        #print(row[0], row[1])
        Date.append(row[0])
        Profit_losses.append(row[1])
        if(row[1] != 'Profit/losses'):
            dictionary[row[1]]= row[0]
# * The total number of months included in the dataset
    for x in range(1, len(Date)):
        Total_months = x
        x = x + 1
# * The net total amount of "Profit/Losses" over the entire period
    for x in range(1, len(Profit_losses)):
        Net_total_amount = Net_total_amount + int(Profit_losses[x])
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
        Profit_losses_a.append(Profit_losses[x])
    Profit_losses_a = Profit_losses_a[:-1]
    for y in range(2, len(Profit_losses)):
        Profit_losses_b.append(Profit_losses[y])
        # Made two list A profit loss a and B profit loss 2
    changeProfitLossDict = {}
    greatest_increase_profits_date = ''
    greatest_decrease_profits_date = ''
    for i in range(0, len(Profit_losses_a)):
        changeInProfitLoss = int(Profit_losses_b[i]) - int(Profit_losses_a[i])
        change_profit_losses_list.append(changeInProfitLoss)
        dateOfChange = dictionary.get(Profit_losses_b[i])
        changeProfitLossDict[changeInProfitLoss] = dateOfChange
        sum_of_change = (sum_of_change + int(change_profit_losses_list[i]))
    Average_change = (sum_of_change/len(change_profit_losses_list)) 
#  The greatest increase in profits (date and amount) over the entire period
    greatest_increase_profits = max(change_profit_losses_list)
    greatest_increase_profits_date = changeProfitLossDict.get(greatest_increase_profits)
    greatest_decrease_profits = min(change_profit_losses_list)
    greatest_decrease_profits_date = changeProfitLossDict.get(greatest_decrease_profits)
    
print(f"The total number of months included in the dataset is = {Total_months}")
print(f"Total Net total amount is = {Net_total_amount}")
print(f"Total Average change is = {Average_change}")
print(f"Greatest Increase in Profits = {greatest_increase_profits_date} {greatest_increase_profits}")
print(f"Greatest Decrease in Profits = {greatest_decrease_profits_date} {greatest_decrease_profits}")


  
         

    
