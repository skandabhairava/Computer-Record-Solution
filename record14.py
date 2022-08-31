import csv

with open("student.csv", "r", newline="") as file:
    data = csv.reader(file)

    header = next(data)
    print(header)
    print("-"*len(header))
    for row in data:
        if row[-1].upper() == "F":
            print(row)
        