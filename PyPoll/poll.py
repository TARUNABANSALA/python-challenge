import csv
import math
read_fpath = ("C:/Users/panka/OneDrive/Desktop/Class Folder/Github/python-challenge/PyPoll/Resources/election_data.csv")
Votes = []
Candidates = []
County = []
Net_total_Votes = 0
Candidates_dictionary = {}
with open(read_fpath, 'r') as f: 
    reader = csv.reader(f, delimiter=',')
    header_row = next(f)
    for row in reader: 
        #print(row[0], row[1])
        Votes.append(row[0])
        County.append(row[1])
        Candidates.append(row[2])
    for x in range(len(Votes)):
        Net_total_Votes = Net_total_Votes + 1
# #  A complete list of candidates who received votes
    candidatesSet = set(Candidates)
    for items in candidatesSet:
        count = Candidates.count(items)  
        print(f"{items} appears {count} times") 
# Names = list(dict.fromkeys(Candidates))
#       # * The total number of votes cast

# print(f"Total Net Votes = {Net_total_Votes}")
# print(Names[0])
# print(Names[1])
# print(Names[2])
# * The percentage of votes each candidate won = "particular votes/ total votes"
# * The total number of votes each candidate won = total particular votes
# * The winner of the election based on popular vote.
# Your analysis should look similar to the following:

#   Charles Casper Stockham: 23.049% (85213)
#   Diana DeGette: 73.812% (272892)
#   Raymon Anthony Doane: 3.139% (11606)
#   -------------------------
#   Winner: Diana DeGette