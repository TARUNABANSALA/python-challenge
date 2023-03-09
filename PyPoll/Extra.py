print("Welcome to the House of Pies! Here are our pies:")
print("----------------------------------------------")
# Print out options
for i in range(len(candy_list)): 
    print(f"[{i}] - {candy_list[i]}")

import os
import csv

# Path to collect data from the Resources folder
graduation_path = os.path.join("..", "Resources", "graduation_data.csv")

# Define the function and have it accept the 'state_data' as its sole parameter

def print_percentages(state_data):
    
    state = str(state_data[0])
    public_students = int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

    total_students = public_students + nonprofit_students + forprofit_students
    total_graduates = public_graduates + nonprofit_graduates + forprofit_graduates
    public_grad_rate = (public_graduates / public_students) * 100    

    if nonprofit_students == 0:
        nonprofit_grad_rate = 0
    else:
        nonprofit_grad_rate = (nonprofit_graduates / nonprofit_students) * 100

    if forprofit_students == 0:
        forprofit_grad_rate = 0
    else:
        forprofit_grad_rate = (forprofit_graduates / forprofit_students) * 100

    # Calculate the overall graduation rate
    overall_grad_rate = (total_graduates / total_students) * 100

    print(overall_grad_rate)

# Read in the CSV file
with open(graduation_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)