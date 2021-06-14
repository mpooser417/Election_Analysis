import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Bootcamp_Folders/Election_Analysis","Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Bootcamp_Folders/Election_Analysis","analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

#The total number of votes cast
#List of all candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on the popular vote