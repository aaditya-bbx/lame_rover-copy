import os
import system
import curses
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
pkill -f car_back.py
pkill -f car_left.py
pkill -f car_right.py
pkill -f car_halt.py

try:
        while True:   
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(38,False)
                GPIO.output(40,True)
             
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
