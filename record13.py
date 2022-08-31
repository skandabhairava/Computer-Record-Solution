import pickle

with open("Hospital.dat", "rb") as file:
    data = pickle.loads(file.read())

print("Current data:", data)

while True:
    print("1. Edit Patient's record")
    print("2. Quit")
    main_inp = int(input("Enter your choice: "))
    if main_inp == 1:
        room = int(input("Enter patient's room number: "))
        if room not in data.keys():
            print("That room does not exist.")
            continue

        name = input("Enter patient's name: ")
        blood_type = input("Enter patient's blood type: ")

        data[room] = {"name": name, "blood_type": blood_type}

        print("New data:", data)
    elif main_inp == 2:
        with open("Hospital.dat", "wb") as file:
            file.write(pickle.dumps(obj=data))
        print("Saving new data...")
        break
    else:
        print("Choice doesn't exist")
