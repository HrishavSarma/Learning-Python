 # Intro to datetime

import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now_formatted = now.strftime("%H:%M:%S %d-%m-%Y")

target_time = datetime.datetime(2026, 1, 2, 12, 45, 0)
current_time = datetime.datetime.now()

if target_time < current_time:
    print("THE TIME HAS PASSED")
else:
    print("THE TIME WILL COME")

print(now_formatted)
