import os
import csv

# Define the path to the input CSV file
BASE_1 = os.path.join(".", "Resources", "election_data.csv")

# Create an empty dictionary to store candidate data
Political_Candidate_Dict = {}

# Create an empty list to store candidate names
Political_Candidates_Names_List = []

# Create an empty set to store unique candidate names
Political_Candidates_Names_Set = set()

# Initialize the total vote count to zero
Total_Votes = 0

# Open and read the CSV file
with open(BASE_1, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Read the header row

    # Loop through each row in the CSV file
    for row in csvreader:
        if len(row) > 2:  # Check if the row contains candidate data
            Total_Votes += 1  # Increment the total vote count
            Ballot_ID = row[0]
            County = row[1]
            Candidate = row[2]

            # Check if the candidate is not already in the list
            if Candidate not in Political_Candidates_Names_List:
                Political_Candidates_Names_List.append(Candidate)  # Add the candidate name to the list
                Political_Candidate_Dict[Candidate] = 1  # Initialize the candidate's vote count to 1
            else:
                Political_Candidate_Dict[Candidate] += 1  # Increment the candidate's vote count

# Calculate and display the percentage of votes for each candidate
for candidate, votes in Political_Candidate_Dict.items():
    percentage = (votes / Total_Votes) * 100
    Political_Candidate_Dict[candidate] = {
        'votes': votes,
        'percentage': percentage
    }

# Find the candidate with the most votes
winner = max(Political_Candidate_Dict, key=lambda x: Political_Candidate_Dict[x]['votes'])

# Prepare the full text with line breaks
val = "\n\n".join([f"{candidate}: {Political_Candidate_Dict[candidate]['percentage']:.3f}% ({Political_Candidate_Dict[candidate]['votes']})" for candidate in Political_Candidates_Names_List])

Full_Text = f'''
Election Results
----------------------------
Total Votes: {Total_Votes}
----------------------------
{val}
----------------------------
Winner: {winner}
----------------------------
'''

# Print the full text to the console
print(Full_Text)
# Define the path to the output text file
export_file = "./Analysis/Result.txt"

# Open and write the "Full_Text" to the text file in the "Analysis" folder
with open(export_file, 'w') as f:
    f.write(Full_Text)
