# Python Alarm Clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    
    print(f"Alarm has been set for {alarm_time}")
    sound_file = "stuffs/yt1s.com - Playboi Carti  Sky Lyrics.mp3"
    is_running = True


    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!\nIT'S FIRST OF THE MONTH!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            
            pygame.mixer.music.play()
            pygame.mixer.music.set_pos(41.5)

            while pygame.mixer.music.get_busy():
                time.sleep(3)
                pygame.mixer.music.stop()

            is_running = False

        time.sleep(1)
if __name__ =="__main__":
    alarm_time = input(f"Time now: {datetime.datetime.now().strftime("%H:%M:%S")}\nEnter the alarm time(HH:MM:SS): ")
    #alarm_time = datetime.datetime.now().strftime("%H:%M:%S")
    set_alarm(alarm_time)