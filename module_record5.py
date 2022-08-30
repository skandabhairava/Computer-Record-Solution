import random

def get_acc_details(lis, modify=False):

    username = input("Enter the username: ")
    password = input("Enter the password: ")

    social_media_accs = []
    amt = int(input("Enter the no. of social medias: "))
    for _ in range(amt):
        sc_user = input("Enter the username: ")
        social_media_accs.append(sc_user)

    if modify:
        passcode = 0
    else:
        passcode = define_a_passcode(lis)

    return passcode, {"username": username, "password": password, "social_media_accs": social_media_accs}

def display_acc_details(acc):
    print("Acc Username: " + acc["username"])
    print("Acc Password: " + acc["password"])
    print("Acc Social Medias: " + str(acc["social_media_accs"]))

def define_a_passcode(lis):
    generated = random.randint(0, 1000)

    while generated in lis:
        generated = random.randint(0, 1000)

    return generated