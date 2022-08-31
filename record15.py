import csv

with open("user_pass.csv", "r", newline="") as file:
    data = csv.reader(file)

    header = next(data)

    data_dict = {}
    for row in data:
        data_dict[int(row[0])] = row[1]

while True:
    print("1. Search User-ID")
    print("2. Quit")
    main_inp = int(input("Enter your choice: "))

    if main_inp == 1:
        u_id = int(input("Enter user id to search: "))
        if u_id not in data_dict.keys():
            print("That User ID doesnt exist.")
            continue

        print("Password:", data_dict[u_id])
    elif main_inp == 2:
        break
    else:
        print("Choice doesn't exist.")
