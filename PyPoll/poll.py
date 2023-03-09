import csv
import math
read_fpath = ("C:/Users/panka/OneDrive/Desktop/Class Folder/Github/python-challenge/PyPoll/Resources/election_data.csv")
Votes = []
Candidates = []
County = []
Net_total_Votes = 0
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
# * The total number of votes each candidate won = total particular votes
    for items in set(Candidates):
        count = Candidates.count(items)  
# * The percentage of votes each candidate won = "particular votes/ total votes"
        percentage_votes = round((count/Net_total_Votes)*100)
        print(f"{items}: {percentage_votes}%({count})")
# * The winner of the election based on popular vote.
# Names = list(dict.fromkeys(Candidates))
      # * The total number of votes cast
print(f"Total Net Votes = {Net_total_Votes}")
print(winner)
# print(Names[0])
# print(Names[1])
# print(Names[2])
#   Winner: Diana DeGette