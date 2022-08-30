from module_record5 import get_acc_details, display_acc_details

DATABASE = {}

while True:
    print("1. Create a New Account")
    print("2. Retrieve Account Name")
    print("3. Retrieve Password for an Account")
    print("4. Retrieve Details of an Account")
    print("5. Modify an Existing Aaccount")
    print("6. Exit")

    main_inp = int(input("Enter your option: "))
    if main_inp == 1:
        passcode, acc = get_acc_details(list(DATABASE.keys()))
        DATABASE[passcode] = acc
        print("Passcode for the account:", passcode)
    elif main_inp == 2:
        passcode = int(input("Enter the passcode: "))
        if passcode not in DATABASE.keys():
            print("Passcode account doesnt exist.")
            continue

        print("Acc username: " + DATABASE[passcode]["username"])
    elif main_inp == 3:
        passcode = int(input("Enter the passcode: "))
        if passcode not in DATABASE.keys():
            print("Passcode account doesnt exist.")
            continue

        print("Acc password: " + DATABASE[passcode]["password"])
    elif main_inp == 4:
        passcode = int(input("Enter the passcode: "))
        if passcode not in DATABASE.keys():
            print("Passcode account doesnt exist.")
            continue

        display_acc_details(DATABASE[passcode])
    elif main_inp == 5:
        passcode = int(input("Enter the passcode: "))
        if passcode not in DATABASE.keys():
            print("Passcode account doesnt exist.")
            continue

        _, acc = get_acc_details(DATABASE.keys(), True)
        DATABASE[passcode] = acc
    elif main_inp == 6:
        break
    else:
        print("Wrong option.")
