import pickle

with open("student.dat", "rb") as file:
    data = pickle.loads(file.read())
    
while True:
    print("1. Search for name")
    print("2. Quit")
    inp = int(input("Enter ur choice: "))
    if inp == 1:
        roll = int(input("Enter roll no.: "))
        if roll not in data.keys():
            print("Roll number doesnt exist.")
            continue

        print("Name:", data[roll])
    elif inp == 2:
        break
    else:
        print("Choice does not exit.")