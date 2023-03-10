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
    Candidates_set = set(Candidates)
    Candidates_sort_list = sorted(list(Candidates_set))
    maxVotes = 0
    winner = ''
    for items in Candidates_sort_list:
        count = Candidates.count(items)  
        if(count > maxVotes):
            winner = items
            maxVotes = count
# * The percentage of votes each candidate won = "particular votes/ total votes"
        percentage_votes = round((count/Net_total_Votes)*100)
        print(f"{items}: {percentage_votes}%({count})")
# * The winner of the election based on popular vote.
      # * The total number of votes cast
print(f"winner = {winner}")
print(f"Total Net Votes = {Net_total_Votes}")
# print(winner)
# print(Names[0])
# print(Names[1])
# print(Names[2])
#   Winner: Diana DeGette