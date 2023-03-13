<!-- PyBank -->
In this challenge, we have to create a Python script to analyze the financial records of our company. We were given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".
We created a Python script that analyzes the records to calculate each of the following:
*First we read a csv file: describe the file path:
*Then we assigned variables, lists and dictionaries such as:
    Profitlossesdate = {} : Dictionary named Profitlossesdate was based on profit/losses as key and date as values from csv file
    netAmount = 0 : netAmount as a zero variable was used to calculate net total amount "Profit/Losses" over the entire period
    change_profit_losses_list = []: a list of 'Profit/losses' was made using dictionary {Profitlossesdate} key values to calculate the changes in "Profit/Losses" over the entire period
    changeProfitLossDict = {}: a dictionary of 'changeProfitlossesDict' was made. Key:Value pair, where key is change in Profit/losses and Values is Change of Dates according to change in Profit/losses 
    sum_of_change = 0: sum_of_change as a zero variable was used to calculate total change in "Profit/Losses" over the entire period 
    Average_change: it was calculated using sum_of_change and len(change_profit_losses_list)
    greatest_increase_profits_date = '': This variable was calculated using maximum of change_profit_losses_list, where this particular element we mapped in a dictionary named changeProfitLossDict and called the Values section to get a particular date
    greatest_decrease_profits_date = '': This variable was calculated using minimum of change_profit_losses_list, where this particular element we mapped in a dictionary named changeProfitLossDict and called the Values section to get a particular date

*A dictionary named {Profitlossesdate} is being created based on Profit/losses as key and Date as Value
*Read the rows from the csv file and made a dictionary out of it in the main.py program, the headers of csv file were removed by putting an IF statement
* The net total amount of "Profit/Losses" over the entire period:
        calculated via for loop iteration of row[1]: profit/losses 
*The total number of months included in the dataset: 
    calculated using the len of the dictionary: Profitlossesdate, values section (Date)
* The changes in "Profit/Losses" over the entire period, and then the average of those changes:
  change_profit_losses_list = []: a list of 'Profit/losses' was made using dictionary {Profitlossesdate} key values to calculate the changes in "Profit/Losses" over the entire period
    changeProfitLossDict = {}: a dictionary of 'changeProfitlossesDict' was made. Key:Value pair, where key is change in Profit/losses and Values is Change of Dates according to change in Profit/losses 
    sum_of_change = 0: sum_of_change as a zero variable was used to calculate total change in "Profit/Losses" over the entire period 
    Average_change: it was calculated using sum_of_change and len(change_profit_losses_list)
    *The greatest increase in profits over the entire period
    greatest_increase_profits and greatest_increase_profits_date = '': This variable was calculated using maximum of change_profit_losses_list, where this particular element we mapped in a dictionary named changeProfitLossDict and called the Values section to get a particular date
    The greatest decrease in profits (date and amount) over the entire period
    greatest_decrease_profits and greatest_decrease_profits_date = '': This variable was calculated using minimum of change_profit_losses_list, where this particular element we mapped in a dictionary named changeProfitLossDict and called the Values section to get a particular date

We print the analysis to the terminal as well as exported a text file with the results in file named "BankOutput.txt".

<!-- PyPoll -->

In this challenge, we have to create a python script for helping a small, rural town modernize its vote counting process. We were given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Our task is to create a Python script that analyzes the votes and calculates each of the following:
We created a Python script that analyzes the records to calculate each of the following:
*First we read a csv file: describe the file path:
*Assigning variables: Then we assigned variables and lists such as:
Ballotid = []: a list where the row[0] from csv file Ballot ID data will be extracted
Candidates = []: a list where the row[2] from csv file Candidates data will be extracted
Net_total_Votes = 0: This variable is created to calculate the Total Votes
maxVotes = 0: This variable is created to calculated the winner based on the highest counts
winner = '': This variable is created to call the winner name by putting the item 
name_Candidates = [], candidate_percentage_votes = [], candidate_count = []: They are created to print the results in a particular format out of the for loop
*Two lists were created named [Ballotid] and [Candidates] using the csv data from Ballot id and Candidates name 
*Read the rows from the csv file and made a lists out of it in the main.py program, the headers of csv file were removed
Calculations:
* The total number of votes cast (Net_total_Votes): a for loop was used to calculate this in the range of len(Ballotid list)
* A complete list of candidates who received votes
 The total number of votes each candidate won = total particular votes
 This was calculated using set method on [Candidates] list, where we were able to extract individual candidate name without the duplicates or unique names, then we applied sorting on (Candidates_set) as well as made a list of those sorted elements at the same time and finally we counted how many times a particular name appeared by reading through a for loop on list named [Candidates_sort_list]
*The percentage of votes each candidate won was calulated using "particular votes/ total votes" and were rounded using the round function upto 3 decimals
* The winner of the election based on popular vote. This is calculated using an IF statement on the Count. Highest count would be the winner
We print the analysis to the terminal as well as exported a text file with the results in file named "PollOutput.txt".

In addition, your final script should both print the analysis to the terminal and export a text file with the results.