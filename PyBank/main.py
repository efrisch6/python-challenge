import os
import csv
import statistics
import locale

# Set Local currency formatting
locale.setlocale(locale.LC_ALL,'en_US')
locale._override_localeconv = {'n_sign_posn':3}

# Set File Path variable-- Currently set for being in the same directory as the python script
csv_path = os.path.join("budget_data.csv")

# Set up variables to store information from file in
months = 0
total = 0
prev_month = 0
current_month = 0
change = 0
avg_change = []
inc = 0
incMonth = ''
dec = 0
decMonth = ''

# Open file
with open(csv_path,newline="") as csvfile:
    # read file
    csvreader = csv.reader(csvfile,delimiter=",")

    # skip header
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        # Count Months
        months += 1
        # Set current month profit/loss
        current_month = float(row[1])
        # Add current month to running total
        total += current_month
        # calculate change from previous month
        change = current_month - prev_month
        # add to list of cahnges (used to calculate average change at end)
        avg_change.append(change)
        # Check if larger than currently stored greatest increrase or decrease
        if change > inc:
            inc = change
            incMonth = row[0]
        elif change < dec:
            dec = change
            decMonth = row[0]
        # Set current month as previous month right before moving on to next row
        prev_month = current_month
        
# Print out results
print("Financial Analysis")
print('-'*20)
print(f'Total Months: {months}')
print(f'Total: {locale.currency(total)}')
# Average Change calculated here, not using first value, as we want to start with the change from the first month to the second month.
print(f'Average Change: {locale.currency(statistics.mean(avg_change[1:]))}')
print(f'Greatest Increase in Profits: {incMonth} ({locale.currency(inc)})')
print(f'Greatest Decrease in Profits: {decMonth} ({locale.currency(dec)})')
