#Import csv and os
import os
import csv 
from pathlib import Path


#Create pathfile

input_file = Path('Resources','budget_data.csv')


#Open and pull from csv file 

with open(input_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

    #Prepare empty lists

    dates = []
    revenue = []
    change =[]
    previous = 0

    #Loop through rows 
    for row in csv_reader:
        dates.append(row[0])
        revenue.append(row[1])
        
        difference = int(row[1]) - int(previous)
        previous = row[1]
        change.append(difference)

zipped = zip(dates, change)
zipped_lst = list(zipped)
change.remove(change[0])
zipped_lst.remove(zipped_lst[0])

total_months = len(dates)
total = sum(map(int, revenue))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)

month_dec = 0
month_inc = 0

for row in zipped_lst:
    if row[1] == increase:
        month_inc = row[0]
    if row[1] == decrease:
        month_dec = row[0]

print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})')

#Exporting File
bank_analysis = Path('Analysis', 'bank_analysis.txt')
with open(bank_analysis, "w") as outfile: 
    
    # Write results to export text file
    outfile.write("Financial Analysis\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {month_inc} ({increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {month_dec} ({decrease})\n")
