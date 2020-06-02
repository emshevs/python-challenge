#Import OS and CSV
import os
import csv

#Filepath
file = '/Users/sheve/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv'

voter_id = []
candidates = []
unique_candidates = []
vote_counts = []


with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])

        candidates.append(row[2])
    
    def unique(candidates):
        unique_candidates = []

    for name in candidates:
        if name not in unique_candidates:
            unique_candidates.append(name)
 
candidate1_count = (candidates.count(unique_candidates[0]))
candidate2_count = (candidates.count(unique_candidates[1]))
candidate3_count = (candidates.count(unique_candidates[2]))
candidate4_count = (candidates.count(unique_candidates[3]))

candidate1_percentage = round((candidate1_count/(len(voter_id))),5) * 100
candidate2_percentage = round((candidate2_count/(len(voter_id))),5) * 100
candidate3_percentage = round((candidate3_count/(len(voter_id))),5) * 100
candidate4_percentage = round((candidate4_count/(len(voter_id))),5) * 100

candidate_counts = [candidate1_count, candidate2_count, candidate3_count, candidate4_count]
candidate_percentages = [candidate1_percentage, candidate2_percentage, candidate3_percentage, candidate4_percentage]

clean_data = list(zip(unique_candidates, candidate_percentages, candidate_counts))

maximum = max(clean_data, key=lambda item: item[1])[0]


print("Election Results")
print("----------------")
print(f"TOTAL VOTES: {len(voter_id)}")
print("----------------")
print("Name, Percentage %, Vote Count")
print(clean_data[0])
print(clean_data[1])
print(clean_data[2])
print(clean_data[3])
print("----------------")
print(f"Winner: {maximum}")
print("----------------")

 #Export file name and open as text file
election_analysis = '/Users/sheve/Documents/GitHub/python-challenge/PyPoll/Analysis/election_analysis.txt'
with open(election_analysis, "w") as outfile: 
    
    # Write results to export text file
    outfile.write("Election Results\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"TOTAL VOTES: {len(voter_id)}\n")
    outfile.write("-----------------------------\n")
    outfile.write("Name, Percentage %, Vote Count\n")
    outfile.write(f"{clean_data[0]}\n")
    outfile.write(f"{clean_data[1]}\n")
    outfile.write(f"{clean_data[2]}\n")
    outfile.write(f"{clean_data[3]}\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Winner:  {maximum}\n")
    outfile.write("-----------------------------\n")







