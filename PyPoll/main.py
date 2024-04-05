#Calculate the total number of votes cast
#Calculate a complete list of candidates who received votes
#Calculate the percentage of votes each candidate won
#Calculate the total number of votes each candidate won
#Calculate the winner of the election based on popular vote

import os
import csv

#file path
csvpath = os.path.join('Resources','election_data.csv')

#Inititalize Variale
total_votes = 0
candidates = {}
winner = " "
winner_votes = 0

#Read CSV file
with open(csvpath, 'r') as file:
    csv_reader = csv.DictReader(file)

    #Iterate through loops
    for row in csv_reader:

        #Calculate the total number of votes cast
        total_votes += 1

        #Calculate a complete list of candidates who received votes
        candidate_name = row['Candidate']

        #Calculate the total number of votes each candidate won
        if candidate_name in candidates:
            candidates[candidate_name] +=1
        else:
            candidates[candidate_name] = 1

#Print total votes
print("Election Rusults")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

#Calculate the percentage of votes each candidate won
for candidate, Votes in candidates.items():
    percentage = (Votes/total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({Votes})")

    #Calculate the winner of the election based on popular vote
    if Votes > winner_votes:
        winner = candidate
        winner_votes = Votes

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")