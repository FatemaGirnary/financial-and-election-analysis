#Calculate the total number of votes cast
#Calculate a complete list of candidates who received votes
#Calculate the percentage of votes each candidate won
#Calculate the total number of votes each candidate won
#Calculate the winner of the election based on popular vote

import os
import csv

#file path
csvpath = os.path.join('Resources','election_data.csv')
#output file path
output_file = "Election_results.txt" 

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

#print results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

 #Calculate the winner of the election based on popular vote
for candidate, Votes in candidates.items():

    if Votes > winner_votes:
        winner = candidate
        winner_votes = Votes

        #Calculate the total number of votes each candidate won
        if candidate_name in candidates:
            candidates[candidate_name] +=1
        else:
            candidates[candidate_name] = 1



#output results in a text file
with open(output_file, 'w') as output:
    output.write("Election Results\n")
    output.write("----------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("----------------------------\n")

    #Calculate the percentage of votes each candidate won
    for candidate, Votes in candidates.items():
        percentage = (Votes/total_votes)*100
        output.write(f"{candidate}: {percentage:.3f}% ({Votes})\n")
        print(f"{candidate}: {percentage:.3f}% ({Votes})")
        
    output.write("---------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("---------------------------\n")


print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")
print("Election results have been saved to 'election_results.txt'")