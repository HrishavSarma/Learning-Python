# Python Alarm Clock

import time
from datetime import datetime, timedelta
import pygame

def set_alarm(alarm_time_str):
    
    print(f"Alarm has been set for {alarm_time_str}")
    sound_file = "stuffs/yt1s.com - Playboi Carti  Sky Lyrics.mp3"
    is_running = True


    while is_running:
        current_time_str = datetime.now().strftime("%H:%M:%S")
        print(current_time_str)

        # For TIME-LEFT
        # current_time = datetime.strptime(current_time_str.replace(":",""), "%H%M%S")
        # alarm_time = datetime.strptime(alarm_time_str.replace(":",""), "%H%M%S")
        
        # time_left = alarm_time - current_time
        # print(time_left)
        
        if current_time_str == alarm_time_str:
            print("WAKE UP!\nIT'S FIRST OF THE MONTH!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            
            pygame.mixer.music.play()
            pygame.mixer.music.set_pos(41.5)

            while pygame.mixer.music.get_busy():
                time.sleep(3.5)
                pygame.mixer.music.stop()

            is_running = False

        time.sleep(1)
if __name__ =="__main__":
    alarm_time_str = input(f"Time now: {datetime.now().strftime("%H:%M:%S")}\nEnter the alarm time(HH:MM:SS): ")
    #alarm_time = datetime.datetime.now().strftime("%H:%M:%S")
    set_alarm(alarm_time_str)