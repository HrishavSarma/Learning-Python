# Python CountDown timer
import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0,my_time+1)):
    seconds = x % 60 # % gets reminder, / get quotient
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.1)
print("HAPPY NEW YEAR!!")