# Python Compound interest calculator

principle = 0
interest = 0
time = 0 

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than zero")
    else:
        break

while True:
    interest = float(input("Enter the Interest rate: "))
    if interest < 0:
        print("Interest cannot be less than zero")
    else:
        break

while True:
    time = float(input("Enter the Time in years: "))
    if time < 0:
        print("Time cannot be less than zero")
    else:
        break

total = principle * pow(1 + interest / 100, time)

print(f"Principle Amount : $ {principle:,.2f}")
print(f"Interest Rate : {interest:}%")
print(f"Time : {time:} Years")

print(f"Your return amount : $ {total:,.2f}")
