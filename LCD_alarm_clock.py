# Import Libraries
import pygame.mixer
import time
import os

import Adafruit_CharLCD as LCD

# Create Variables To Control The Alarm
alarm_hour = 18 	# Change These Values To The Appropriate Time (24h clock)
alarm_minute = 37

pygame.mixer.init() 	# Initialise The Pygame Library
num_loops = 5 	# Set How Many Times You Want Your Sound File To Loop

alarm = pygame.mixer.Sound("/home/pi/elec_chime.wav") 	# Change This Path To Your Sound File
alarm_length = (pygame.mixer.Sound.get_length(alarm)* num_loops)

# Raspberry Pi Pin Configuration:
lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD Column And Row Size For 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize The LCD Using The Pins Above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

while True:
    currentTime = list(time.localtime()) 	# Get The Local Time
    hour	= currentTime[3]
    minute 	= currentTime[4]
    
    if hour == alarm_hour and minute == alarm_minute:
        lcd.clear()
        print("Wake Up!") 	# Print A Message On Console
        lcd.message("Wake Up Now!")
        alarm.play(loops = num_loops) 	# Play Sound File
        time.sleep(alarm_length)
        lcd.clear()
        break
