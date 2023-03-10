import csv
import math
read_fpath = ("C:/Users/panka/OneDrive/Desktop/Class Folder/Github/python-challenge/PyPoll/Resources/election_data.csv")
Ballotid = []
Candidates = []
Net_total_Votes = 0
maxVotes = 0
winner = ''
name_Candidates = []
candidate_percentage_votes = []
candidate_count = []
with open(read_fpath, 'r') as f: 
    reader = csv.reader(f, delimiter=',')
    header_row = next(f)
    for row in reader: 
        #print(row[0], row[1])
        Ballotid.append(row[0])
        Candidates.append(row[2])
    for x in range(len(Ballotid)):
        Net_total_Votes = Net_total_Votes + 1
# * The total number of votes each candidate won = total particular votes
    Candidates_set = set(Candidates)
    Candidates_sort_list = sorted(list(Candidates_set))
    for items in Candidates_sort_list:
        count = Candidates.count(items)  
        if(count > maxVotes):
            winner = items
            maxVotes = count
# * The percentage of votes each candidate won = "particular votes/ total votes"
        percentage_votes = round(((count/Net_total_Votes)*100), 3)
# * The total number of votes each candidate won
        name_Candidates.append(items)
        candidate_percentage_votes.append(percentage_votes)
        candidate_count.append(count)
# * The winner of the election based on popular vote.
      # * The total number of votes cast
print("```text")
print("Election Results")
print("-------------------------")
print(f"Total Votes = {Net_total_Votes}")
print("-------------------------")
print(f"{name_Candidates[0]}: {candidate_percentage_votes[0]}%, ({candidate_count[0]})")
print(f"{name_Candidates[1]}: {candidate_percentage_votes[1]}%, ({candidate_count[1]})")
print(f"{name_Candidates[2]}: {candidate_percentage_votes[2]}%, ({candidate_count[2]})")
print("-------------------------")
print(f"winner = {winner}")
print("-------------------------")
print("```")