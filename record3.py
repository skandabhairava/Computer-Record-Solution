def compound_interest(p, r, t, n):
    interest = p * (1 + (r / 100) / n) ** (n * t) - p
    return interest

principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time taken: "))
interest_time = float(input("Enter the interest given in the time period: "))

cmpd_interest = compound_interest(principle, rate, time, interest_time)
print("The compund interest is: " + str(cmpd_interest))