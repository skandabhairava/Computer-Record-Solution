def inp_list():
    length = int(input("Enter the length of the list: "))
    lis = []
    for i in range(length):
        lis.append(int(input("Enter " + str(i) + "th* item: ")))

    return lis

def sum(lis):
    ctr = 0
    for i in lis:
        ctr += i

    return ctr

print("The sum of the list entered: ", sum(inp_list()))