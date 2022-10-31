import csv
from pathlib import Path


csvpath = ""
# add a header for the csv file
header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
# designate a path for the file to populate on the local computer

def save_csv(save_qualifying_loans):
    save_cvs = [] 
    # function to write a new csv file with only the loans a potential borrower is qualified for
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for row in csvwriter:
            csvwriter.writerow(row.values())
            print(row.values())
    