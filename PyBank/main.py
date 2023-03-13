import csv
read_fpath = ("PyBank/Resources/budget_data.csv")

# Assigning variables: all the variables & lists & dictionaries have been defined thoroughly in the readme file
Profitlossesdate = {}
netAmount = 0
change_profit_losses_list = []
changeProfitLossDict = {} 
sum_of_change = 0
greatest_increase_profits_date = ''
greatest_decrease_profits_date = ''

#Reading the file through csv reader
with open(read_fpath, 'r') as f: 
    reader = csv.reader(f, delimiter=',')
#Making a dictionary based on Profit/losses as key and Date as Value
    for row in reader: 
# Remove the header by putting an IF statement
        if(row[1] != 'Profit/losses'):
            Profitlossesdate[row[1]]= row[0]
# Calculations: Calculating Total Net Amount
            netAmount = netAmount + int(row[1])
# Calculating Total Months
    totalMonths = len(Profitlossesdate.values())
# Calculating Average Change: # Making a dictionary for change in profit/losses + # Making a list of Profit/losses using dictionary key values
    profitLossList = list(Profitlossesdate.keys())
    for i in range(0, len(profitLossList)-1):
        changeInProfitLoss = int(profitLossList[i+1]) - int(profitLossList[i])
        change_profit_losses_list.append(changeInProfitLoss)
        # getting the date of Change by calling values from dictionary
        dateOfChange = Profitlossesdate.get(profitLossList[i+1])
        # Making a new dictionary of key: changeInProfitLoss and value: dateOfChange
        changeProfitLossDict[changeInProfitLoss] = dateOfChange
        sum_of_change = (sum_of_change + int(change_profit_losses_list[i]))
        # Calulating the average change
    Average_change = round((sum_of_change/len(change_profit_losses_list)), 2) 
#  The greatest increase in profits (date and amount) over the entire period
    greatest_increase_profits = max(change_profit_losses_list)
    greatest_increase_profits_date = changeProfitLossDict.get(greatest_increase_profits)
    greatest_decrease_profits = min(change_profit_losses_list)
    greatest_decrease_profits_date = changeProfitLossDict.get(greatest_decrease_profits)

# Printing the results according to the given format
print("```text")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months = {totalMonths}")
print(f"Total Net amount = {netAmount}")
print(f"Average change = {Average_change}")
print(f"Greatest Increase in Profits = {greatest_increase_profits_date} {greatest_increase_profits}")
print(f"Greatest Decrease in Profits = {greatest_decrease_profits_date} {greatest_decrease_profits}")
print("```")
# Exported a text file with the results in file named "BankOutput.txt".
# Specify the file path
file_path = 'PyBank/Analysis/BankOutput.txt'
# Open the file for writing
with open(file_path, 'w',  newline='') as wf: 
    wf.write('```text\n')
    wf.write('Financial Analysis\n')
    wf.write('----------------------------\n')
    wf.write('Total Months = ' + str(totalMonths) + '\n')
    wf.write('Total Net amount = ' + str(netAmount) + '\n')
    wf.write('Average change = ' + str(Average_change) + '\n')
    wf.write('Greatest Increase in Profits = ' + str(greatest_increase_profits_date) + ' ' + str(greatest_increase_profits) + '\n')
    wf.write('Greatest Decrease in Profits = ' + str(greatest_decrease_profits_date) + ' ' + str(greatest_decrease_profits) + '\n')
    wf.write('```')