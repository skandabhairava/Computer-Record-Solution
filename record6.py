def prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False

    return True

inp = int(input("Enter a number to find the prime of: "))
print("is the number entered, a prime number: ", prime(inp))