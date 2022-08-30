import random

def rand(n):
    rand_num = ""
    rand_num += str(random.randrange(1, 10)) # This is because, the first number can be a 0, making the the length of generated number < n
    for _ in range(n - 1):
        rand_num += str(random.randrange(0, 10))

    return int(rand_num)

length = int(input("Enter the length of the random number to be generated: "))
random_number = rand(length)

print("The random number generated is: " + str(random_number))