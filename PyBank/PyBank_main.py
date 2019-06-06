# Esther Lowe's Financial Analysis Program 06012019

#First, I'll import the os and csv modules
import os
import csv

# grabbing the file
bank_csv = "budget_data.csv"

# Lists to store data
dates = []
date_changes = []
profits_losses = []
changes = []

with open(bank_csv, newline="", encoding='utf-8') as csvfile:
    # CSV reader has the delimiter and a new variable to hold the gotten info
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of data after the header and then append it to the appropriate list

    for row in csvreader:
        # append the date list
        dates.append(row[0])

        # append the profit/loss list
        profits_losses.append(row[1])

# zip lists together and make a new list
cleaned_bank = list(zip(dates,profits_losses))

for i in range(len(cleaned_bank)):
    # making a list for the given i 
    row = cleaned_bank[i]

    # append the average change list
    cur_profit = float(row[1])

    # keeping the program from jamming when doing an i + 1
    if i == len(cleaned_bank) - 1:
        break

    # making a list and variables of the next i set of list values
    next_row = cleaned_bank[i+1]
    next_profit = float(next_row[1])
    date_diff = next_row[0]

    # computing the difference in profit/loss each month
    cur_diff = next_profit - cur_profit

    changes.append(cur_diff)
    date_changes.append(date_diff)
    
# add newly generate lists to a new calculated_bank list
calculated_bank = list(zip(date_changes, changes))
    
# create and initialize variables to store profit, loss, average, and greatest increase and decrease

profit = 0
loss = 0
adiff = 0
greatest_profit = 0
greatest_loss = 0

# Loop through the original list of data and calculate total profit and total loss
for row in cleaned_bank:

    # If the money in a row is >= 0, add and if money is < 0 add separately
    num = float(row[1])
    if num >= 0:
        profit = profit + num
    else:
        loss = loss + num

# loop throught the next list of data to assign more variables for analysis computation    
# store values for the sum of the differences to calculate average change
# store values for the greatest increase in profit and loss
for row in calculated_bank:

    # adds the differences in profit/loss calculated earlier
    num1 = float(row[1])
    adiff = adiff + num1

    # checks the values to find the month of greatest profit and the value thereof    
    if num1 >= greatest_profit:
        greatest_profit = int(num1)
        date_gp = row[0]

    # checks the values to find the month of greatest loss and the value thereof 
    elif num1 <= greatest_loss:
        greatest_loss = int(num1)
        date_gl = row[0]

# some financial analysis using values from the lists and turning them into floats
total_len_date_changes = len(date_changes)
total_len_date_changes = float(total_len_date_changes)
total_months = len(dates)
total_months = int(total_months)
total = profit + loss
average = round((adiff/total_len_date_changes),2)

# Define the function to output financial analysis
def print_analysis():

    financial_analysis = [["Financial Analysis"],
                          ["-------------------------------------------------------------------------------"],
                          [f"Total Number of Months Analyzed: {total_months}"],
                          [f"Total: ${total}"],
                          [f"Average company profit or loss per month was: ${average}"],
                          [f"Greatest Increase in Profits: {date_gp} for (${greatest_profit})"],
                          [f"Greatest Decrease in Profits: {date_gl} for (${greatest_loss})"],
                          ["-------------------------------------------------------------------------------"]]

    # print the financial summary in a text file
    # Set variable for output file
    output_file = "PyBank_final.txt"

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

    # print out a summary including total months, total, average monthly change, greatest increase in profit, greatest decrease in profit to the terminal
        writer.writerows(financial_analysis)
    
    # Because I don't like how the regular loop printed, I did my own loop:
    for row in financial_analysis:
        print(row)

    # This was instead of a simple print of the list to the terminal
    #print(financial_analysis)

print_analysis()




