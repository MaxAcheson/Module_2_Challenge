# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(path, new_loan_data): # This save_csv file allows data from the new filtered loan list to be written into a CSV file.
    
    with open(path, "w") as csvfile: # This line describes the file path, and that we are writing to a CSV file. 
        csvwriter = csv.writer(csvfile, delimiter = ",") # This part explains how the file will be written, using commas (,) as the separator for text strings.
        for row in new_loan_data: # Used a 'for loop' to access data within new_loan_data.
            csvwriter.writerow(row) # Telling the csvwriter to write data as rows in the CSV file. 