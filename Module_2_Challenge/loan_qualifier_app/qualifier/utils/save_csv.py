import csv
from pathlib import Path



# add a header for the csv file
header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
# designate a path for the file to populate on the local computer
output_path = Path("save_csv.csv")

def save_csv(save_qualifying_loans):
 
    # function to write a new csv file with only the loans a potential borrower is qualified for
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for loan in save_csv:
            csvwriter.writerow(loan.values())
            print(loan.values())
    