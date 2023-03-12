## PyBank Instructions
In this challenge, we have to create a Python script to analyze the financial records of our company. We were given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".
We created a Python script that analyzes the records to calculate each of the following:

*First we read a csv file: describe the file path
*Then we assigned variables, lists an dictionaries
* We open the csv file through csv.reader function
Putting inputs from csv file to python variable, lists or dictionary
*A dictionary is being created based on Profit/losses as key and Date as Value
*Read the rows from the csv file and made a dictionary out of it in the main.py program, the headers of csv file were removed by putting an IF statement
* The total number of months included in the dataset: a variable named "netAmount = 0" was created and it was calculated via for loop iteration of row[1]: profit/losses 

# Calculating Total Months
    totalMonths = len(dictionary.values())
# Calculating Average Change
    # Making a dictionary for change in profit/losses
    changeProfitLossDict = {}
    greatest_increase_profits_date = ''
    greatest_decrease_profits_date = ''
    # Making a list of Profit/losses using dictionary key values
    profitLossList = list(dictionary.keys())
    for i in range(0, len(profitLossList)-1):
        changeInProfitLoss = int(profitLossList[i+1]) - int(profitLossList[i])
        change_profit_losses_list.append(changeInProfitLoss)
        # getting the date of Change by calling values from dictionary
        dateOfChange = dictionary.get(profitLossList[i+1])
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

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll Instructions

In this challenge, we have to create a python script for helping a small, rural town modernize its vote counting process. We were given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Our task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.


In addition, your final script should both print the analysis to the terminal and export a text file with the results.