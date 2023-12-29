# Python-Challenge

# Background

It's time to put away the Excel sheet and enter the world of programming with Python. In this assignment, you'll use the concepts you've learned to complete two Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.

# Before You Begin

* Before starting the assignment, be sure to complete the following steps:
* Create a new repository for this project called python-challenge. Do not add this homework assignment to an existing repository.
* Clone the new repository to your computer.
* Inside your local Git repository, create a folder for each Python assignment and name them PyBank and PyPoll.
* In each folder that you just created, add the following content:
* A new file called main.py. This will be the main script to run for each analysis.
* A Resources folder that contains the CSV files you used. Make sure that your script has the correct path to the CSV file.
* An analysis folder that contains your text file that has the results from your analysis.
* Push these changes to GitHub or GitLab.

# PyBank Instructions

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period
* Your analysis should align with the following results:

![Snip20231102_30](https://github.com/JesseOli100/Python-Challenge/assets/62526904/68f9f541-2859-4a19-9138-573ada58aad7)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# PyPoll Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote
* Your analysis should align with the following results:

![Snip20231102_31](https://github.com/JesseOli100/Python-Challenge/assets/62526904/b77809c8-345c-4727-9483-4ec96438d224)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Hints and Considerations

Consider what you've learned so far. You've learned how to import modules like csv. You’ve learned how to read and write files in various formats. You’ve learned how to store content in variables, lists, and dictionaries. You’ve learned how to iterate through basic data structures. And you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.

The datasets for these Challenges are quite large. This was done purposefully to showcase one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more powerful options for handling big data.

Write one script for each of the provided datasets. Run each script separately to make sure that the code works for its respective dataset.

Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

# Sources 

* Help from TA Matthew Werth
  
* Met up w/ other students during study groups to hash out the code through what we have learned so far
  
* Used StackOverFlow and ChatGPT for issues on the code and/or to explain why certain pieces of the script were not running as intended

# Final Notes

What is each set of code supposed to be doing?

The purpose of the “main.py” file in both PyBank and PyPoll is just to display a specific output based on the instructions provided. Granted, you are supposed to use some formulas to get the outputs for some of the things that are being asked, but in the end the value of this project is to display a summary of information relevant to the user at the given time and also store that summary in a csv file. 

Syntax Learned:

* import os – Imports the OS module (this module provides functions for creating and removing a directory, getting its contents, changing information, etc.)
  
* import csv – Imports the csv module (this module implements classes to read and write tabular data in CSV format)
  
* os.path.join(“Folder_Name”, “csv_file_name.csv”) – Defines the path to the input CSV file

* len(Variable_or_Function_name) – Returns the length of an object

* list = [] – Creates a blank list 

* with open(input_file, 'r') as file: - Opens the specific file in ‘read’ mode, this is convenient because it also takes care of closing the file for you 

* object_name = csv.reader(file) – Creates as csv reader object that reads the contents of the specified file name and allows you to read and manipulate data stored in that file 

* for row in object_name: - Loops through each element in the variable, in each iteration of the loop, the element is assigned to the “row” variable which allows you to perform operations on said variable. You could change “row” for something else within the variable you’d want to read within the csv file, but the file would need to have that variable already in it. 

* if len(row) > 1: - If the length of the “row” variable is greater than 1 
 
* if Variable_Name is not None: - If the specified variable is not equal to None (if there is any value other than None present). “None” is a special value in Python that represents the absence of a value. 

* Variable_Name = f''' [insert string here] ''' – Creates a variable which will use the f-strings feature or formatted string literals. It allows for the user to embed expressions inside strings using {}. 

* variable_name = “./Folder_Name/csv_file_name.txt” – Defines the path to the output text file

* with open(output_file, 'w') as f:
     f.write(variable_name) - Outputs the desired information into the specified csv file 

- - -

This is submitted by Jesse Olivarez for the University of Utah: Data Analytics Bootcamp
