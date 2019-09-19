import os
import csv
import datetime

csv_path = os.path.join("employee_data.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

emp_id = []
first = []
last = []
dob = []
ssn = []
state = []


with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        # employee id - no change
        emp_id.append(row[0])
        # split name at space into first and last name
        first.append(row[1].split(" ")[0])
        last.append(row[1].split(" ")[1])
        # Change DOB format from YYYY-MM-DD to MM/DD/YYYY
        dob.append(datetime.datetime.strptime(row[2],'%Y-%m-%d').strftime('%m/%d/%Y'))
        # Change first 5 digits of SSN to * and display last 4 digits
        ssn.append("***-**-" + row[3][-4:])
        # Change state to abbreviation
        state.append(us_state_abbrev[row[4]])

header = ['Emp ID','First Name','Last Name','DOB','SSN','State']
results = zip(emp_id, first, last, dob, ssn, state)

output_file = os.path.join("output.csv")

with open(output_file, 'w', newline="") as outfile:
    writer = csv.writer(outfile)

    writer.writerow(header)
    writer.writerows(results)