import csv
# Assigning filepath for reading
read_fpath = ("PyPoll\Resources\election_data.csv")

# Assigning variables: all the variables & lists have been defined thoroughly in the readme file
Ballotid = []
Candidates = []
Net_total_Votes = 0
maxVotes = 0
winner = ''
name_Candidates = []
candidate_percentage_votes = []
candidate_count = []

# Reading the file
with open(read_fpath, 'r') as f: 
    reader = csv.reader(f, delimiter=',')
# Taking off the header
    header_row = next(f)
# Adding the csv file data into the lists that we created above
    for row in reader: 
        #print(row[0], row[1])
        Ballotid.append(row[0])
        Candidates.append(row[2])
# Calculations
# Total number of votes
    for x in range(len(Ballotid)):
        Net_total_Votes = Net_total_Votes + 1
# * The total number of votes each candidate won = total particular votes
    Candidates_set = set(Candidates)
    Candidates_sort_list = sorted(list(Candidates_set))
    for items in Candidates_sort_list:
        count = Candidates.count(items)  
# * The percentage of votes each candidate won = "particular votes/ total votes"
        percentage_votes = round(((count/Net_total_Votes)*100), 3)
# * The total number of votes each candidate won
        name_Candidates.append(items)
        candidate_percentage_votes.append(percentage_votes)
        candidate_count.append(count)
# * The winner of the election based on popular vote.
        if(count > maxVotes):
            winner = items
            maxVotes = count

# Printing the results according to the given format
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
# Exported a text file with the results in file named "PollOutput.txt".
# Specify the file path
file_path = 'PyPoll/Analysis/PollOutput.txt'
# Open the file for writing
with open(file_path, 'w',  newline='') as wf:
    wf.write('```text\n')
    wf.write('Election Results\n')
    wf.write('-------------------------\n')
    wf.write('Total Votes =' + str(Net_total_Votes) + '\n')
    wf.write('-------------------------\n')
    wf.write(str(name_Candidates[0]) + ':' + ' ' + str(candidate_percentage_votes[0]) + '%' + ' ' + str(candidate_count[0]) + '\n')
    wf.write(str(name_Candidates[1]) + ':' + ' ' + str(candidate_percentage_votes[1]) + '%' + ' ' + str(candidate_count[1]) + '\n')
    wf.write(str(name_Candidates[2]) + ':' + ' ' + str(candidate_percentage_votes[2]) + '%' + ' ' + str(candidate_count[2]) + '\n')
    wf.write('-------------------------\n')
    wf.write('winner = ' + str(winner) + '\n')
    wf.write('-------------------------\n')
    wf.write('```') 
    