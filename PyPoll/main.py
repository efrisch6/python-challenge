import os
import csv

csv_path = os.path.join("election_data.csv")

total = 0
election = {}

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        candidate = row[2]
        # Check in Candidate (third column) is in election dictionary
        if candidate in election.keys():
            # Add to vote count for candicate
            election[candidate] += 1
        # Add candidate to dictionary and add 1 vote
        else:
            election[candidate] = 1

for key in election:
    total += election[key]

winner = 0
winnerName = ''

print(f'Election Results')
print("-"*20)
print(f'Total Votes: {total}')
print("-"*20)
for key in election:
    votes = election[key]
    print(f'{key}: {"{0:.3f}%".format(votes/total*100)} ({votes})')
    if votes > winner:
        winnerName = key
        winner = votes
print("-"*20)
print(f"Winner: {winnerName}")
print("-"*20)


output_path = os.path.join("output.txt")

with open(output_path, 'w', newline="") as outfile:
    txtwriter = csv.writer(outfile, delimiter=",")
    txtwriter.writerow(['Election Results'])
    txtwriter.writerow(["-"*20])
    txtwriter.writerow([f'Total Votes: {total}'])
    txtwriter.writerow(["-"*20])
    for key in election:
        votes = election[key]
        txtwriter.writerow([f'{key}: {"{0:.3f}%".format(votes/total*100)} ({votes})'])
    txtwriter.writerow(["-"*20])
    txtwriter.writerow([f"Winner: {winnerName}"])
    txtwriter.writerow(["-"*20])