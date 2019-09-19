import os
import csv
import statistics

csv_path = os.path.join("budget_data.csv")
months = 0
total = 0
prev_month = 0
current_month = 0
change = []
avg_change = 0
inc = 0
dec = 0

with open(csv_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    header = next(csvreader)
    print(header)
    for row in csvreader:
        months += 1
        current_month = float(row[1])
        total += current_month
        change.append(current_month - prev_month)
        prev_month = current_month
        if current_month > inc:
            inc = current_month
        elif current_month < dec:
            dec = current_month
        

print(months)
print('${:0,.2f}'.format(total))
print(statistics.mean(change))
print(inc)
print(dec)
