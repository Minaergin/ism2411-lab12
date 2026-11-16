
# ISM2411 Lab 12
# Name: Mina Ergin

import csv
from datetime import datetime

# Exercise 1: Setup
print("EXERCISE 1: SETUP")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)

print("CSV file opened successfully.")
print("Header:", rows[0])
print("Number of data rows:", len(rows) - 1)



# Exercise 2: Read and print raw rows
print("\nEXERCISE 2: RAW ROWS")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
