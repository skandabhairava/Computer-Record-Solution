def nth_root(x, n):
    return x ** (1/n)

x_num = int(input("Enter a number to find the root of: "))
n_num =  int(input("Enter the root: "))

ans = nth_root(x_num, n_num)
print("The " + str(n_num) + "th root of " + str(x_num) + " is: " + str(ans))