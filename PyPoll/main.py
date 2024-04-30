import pandas as pd
import os

# Load the data from your CSV file
file_path = 'PyPoll/Resources/election_data.csv'
election_data = pd.read_csv(file_path)

# Total number of votes cast
total_votes = election_data['Ballot ID'].count()

# A complete list of candidates who received votes
candidates = election_data['Candidate'].unique()

# Calculate the total number of votes and percentage each candidate won
vote_counts = election_data['Candidate'].value_counts()
percentages = (vote_counts / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = vote_counts.idxmax()

# Preparing the analysis results
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in vote_counts.items():
    results += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"
results += "-------------------------\n"
results += f"Winner: {winner}\n"
results += "-------------------------\n"

# Print the results to the terminal
print(results)

# Path for the output file
output_file_path = os.path.join(os.path.dirname(file_path), 'election_results.txt')

# Write the results to a text file
with open('PyPoll/Resources/election_results.txt', 'w') as file:
    file.write(results)
