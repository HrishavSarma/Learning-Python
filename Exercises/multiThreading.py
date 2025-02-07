# Multithreading -> Used to perform multiple tasks concurrently(multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
#                   threading.Thread(target=my_function)

import threading
import time
import datetime

is_running = True

def clock():
    while is_running:
        time.sleep(1)
        print(f"Current Time : {datetime.datetime.now().strftime("%H:%M:%S")}")

def walk_dog(first,last):
    global is_running
    time.sleep(5)
    print(f"You walked the {first}{last}")
    is_running = False

def take_trash():
    time.sleep(2)
    print("You took out the trash")

def get_mail():
    time.sleep(3)
    print("You got the mail")

chore0 = threading.Thread(target = clock)
chore0.start()

chore1 = threading.Thread(target = walk_dog, args = ("Milo", "Mister"))
chore1.start()

chore2 = threading.Thread(target= take_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All the tasks are done")