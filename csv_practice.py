
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



# Exercise 3: Skip the header
print("\nEXERCISE 3: SKIP HEADER")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)



# Exercise 4: Compute totals
print("\nEXERCISE 4: COMPUTE TOTALS")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(
            f"{product}: {quantity} units × "
            f"${price:.2f} = ${total:.2f}"
        )

print(f"Total Revenue: ${total_revenue:.2f}")



# Exercise 5: Filter and write
print("\nEXERCISE 5: FILTER AND WRITE")

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([
                    product,
                    f"{price:.2f}",
                    quantity,
                    f"{total:.2f}"
                ])

                cleaned_count += 1

print(f"Original rows: {original_count}")
print(f"Cleaned rows written: {cleaned_count}")



# Exercise 6: csv.DictReader
print("\nEXERCISE 6: DICTREADER")

# csv.reader is useful when column positions are known and consistent.
# csv.DictReader is better when accessing data using column names.

dict_total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader Total Revenue: ${dict_total_revenue:.2f}")



# Exercise 7: Sales summary by product
print("\nEXERCISE 7: SALES SUMMARY")

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")
