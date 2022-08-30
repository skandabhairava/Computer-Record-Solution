main_menu = ["Compute", "History", "Quit"]
compute_menu = ["Add", "Subtract", "Multiplication", "Division"]
history_menu = ["Subsitute number 1", "Subsitute number 2"]

HISTORY = []
FILL_UP_0 = None
FILL_UP_1 = None

def get_input(menu, show=True):
    if len(menu) == 0: return -1

    print("\n")

    if show:
        i = 0
        for item in menu:
            print(str(i) + ". " + str(item))
            i += 1

    inp = int(input("Enter an option: "))

    if (inp > (len(menu) - 1)) or (inp < 0):
        print("Invalid input")
        return get_input(menu, False)

    return inp

def append_history(i):
    HISTORY.append(i)
    if len(HISTORY) >= 10:
        HISTORY.pop(0)

while True:
    main_inp = get_input(main_menu)
    if main_inp == 0:
        comp_inp = get_input(compute_menu)

        num1 = float(input("Enter number 1: ")) if FILL_UP_0 is None else FILL_UP_0
        num2 = float(input("Enter number 2: ")) if FILL_UP_1 is None else FILL_UP_1

        FILL_UP_1, FILL_UP_0 = None, None

        if comp_inp == 0:
            calc = num1 + num2
            print(str(num1) + " + " + str(num2) + " = " + str(calc))
        elif comp_inp == 1:
            calc = num1 - num2
            print(str(num1) + " - " + str(num2) + " = " + str(calc))
        elif comp_inp == 2:
            calc = num1 * num2
            print(str(num1) + " * " + str(num2) + " = " + str(calc))
        elif comp_inp == 3:
            calc = num1 / num2
            print(str(num1) + " / " + str(num2) + " = " + str(calc))

        append_history(calc)
    elif main_inp == 1:
        idx = get_input(HISTORY)
        if idx == -1:
            print("\nHistory is empty.")
            continue
        save_history = HISTORY[idx]
        num1_num2 = get_input(history_menu)
        if num1_num2 == 0:
            FILL_UP_0 = save_history
        elif num1_num2 == 1:
            FILL_UP_1 = save_history
        else:
            print("Could not save it in '" + str(num1_num2) + "'.")
    elif main_inp == 2:
        break
    else:
        print(str(main_inp) + " is not an option.")
        