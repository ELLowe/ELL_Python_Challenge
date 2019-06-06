# Esther Lowe's Election Polling Program 06042019

#First, I'll import the os and csv modules as well as Counter from collections
import os, csv, operator
from collections import Counter

# grabbing the file
poll_csv = "election_data.csv"

# Lists to store data

voter_ids = []
counties = []
candidates = []

with open(poll_csv, newline="", encoding='utf-8') as csvfile:
    # CSV reader has the delimiter and a new variable to hold the gotten info
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of data after the header and then append it to the appropriate list

    for row in csvreader:
        # append the voter ID to a list
        voter_ids.append(row[0])

        # append the county to a list
        counties.append(row[1])

        # append the candidate to a list
        candidates.append(row[2])

# zip lists together and make a new list
cleaned_election = list(zip(voter_ids,counties,candidates))

# store the value of the total number of votes cast
total_votes = int(len(voter_ids))

# store a list of the candidates who received votes and a dictionary of their name and how many votes they received
counted_candidates = dict(Counter(candidates))
candidate_list = list(counted_candidates.keys())

# calculating the winner! Formatted the max function to show the key rather than the value

winner = max(counted_candidates, key=counted_candidates.get)

#converting the count to a list for candidate votes
candidate_votes = list(counted_candidates.values())

# converting counted_candidates into a new list of dictionaries, one for each candidate
new_cand_list = []

for i in range(len(candidate_list)):
    candidate_dict = {}

    # assigning the name, vote count, and percent of vote keys with their respective values
    candidate_dict['name'] = candidate_list[i]
    candidate_dict['vote_count'] = candidate_votes[i]
    candidate_dict['vote_percent'] = round((candidate_votes[i]/total_votes)*100,2)

    # append the dictionary entries to the list
    new_cand_list.append(candidate_dict)

print(new_cand_list)


election_analysis_title = [["Election Results"],
                           ["-------------------------------------------------------------------------------"],
                           [f"Total Number of votes cast: {total_votes}"],
                           ["-------------------------------------------------------------------------------"]]

election_outcome = [[f"The winner is: {winner}, with {counted_candidates[winner]} votes!"],
                    ["-------------------------------------------------------------------------------"]]

# Because I don't like how the regular loop printed to the terminal, I did my own loop:

# Set variable for output file
output_file = "PyPoll_final.txt"
writer = csv.writer(datafile)

def print_title():

    for row in election_analysis_title:
        print(row)

# print the election analysis title in a text file

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

    # print out the summary into the text document
        writer.writerows(election_analysis_title)

# create a function to print the complete list of candidates who received votes, the number of votes and percentage of votes each candidate got, to the terminal and append it to the txt doc
def print_election_results():
    
    for i in range(len(candidate_list)):
        print(new_cand_list[i])

        with open(output_file, "a") as datafile:
            writer = csv.writer(datafile)
            writer.writerows(new_cand_list[i])

# create a function to print the election outcome to the terminal and append it to the txt doc
def print_outcome():

    with open(output_file, "a") as datafile:
        writer = csv.writer(datafile)
        writer.writerows(election_outcome)

    for row in election_outcome:
        print(row)




print_title()
print_election_results()
print_outcome()

