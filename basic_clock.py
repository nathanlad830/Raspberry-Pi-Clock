# Import Modules
import time
import datetime

# Set Variables And Format How They Will Appear
date = datetime.datetime.now().strftime("%d-%m-%Y")
clock = datetime.datetime.now().strftime("%H:%M:%S")

# Output The Different Variables To The Console 
print "The Current Date Is " , date
print "The Current Time Is " , clock


#############################################################################################
# The Next Bit Is Going To Display The Different Variables On An Adafruit 16x2 LCD Screen   #
# If You Dont Wish To Use It, Simply Add The Three Quotation Marks At The Top And Bottom    #
#############################################################################################

import math
import Adafruit_CharLCD as LCD

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

# Display The Time And Date
while True:
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    clock = datetime.datetime.now().strftime("%H:%M:%S") 
    lcd.clear()
    lcd.message("Date ")
    lcd.message(date)
    lcd.message("\n")
    lcd.message("Time ")
    lcd.message(clock)
    time.sleep(1)
