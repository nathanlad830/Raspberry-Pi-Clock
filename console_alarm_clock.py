# Import Libraries
import pygame.mixer
import time
import os

# Create Variables To Control The Alarm
alarm_hour = 18     # Change These Values To The Appropriate Tie (24h clock)
alarm_minute = 37

pygame.mixer.init()     # Initialise The Pygame Library
num_loops = 5   # Set How Many Times You Want Your Sound File To Loop
alarm = pygame.mixer.Sound("/home/pi/elec_chime.wav")   # Change This Path To Your Sound File
alarm_length = (pygame.mixer.Sound.get_length(alarm)* num_loops)

while True:
    currentTime = list(time.localtime())    # Get The Local Time
    hour = currentTime[3]
    minute = currentTime[4]
    
    if hour == alarm_hour and minute == alarm_minute:
        print("Wake Up!")   # Print A Message On Console
        alarm.play(loops = num_loops)   # Play Sound File
        time.sleep(alarm_length)
        break
