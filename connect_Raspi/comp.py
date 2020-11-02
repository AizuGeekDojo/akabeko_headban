#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import pygame.mixer as game

GPIO.setmode(GPIO.BCM)

IN=[20,21,24]
LED=[23,18,17]
BPM=[80,116,145]
MOTOR=12
MUSICS=['akabeko1.mp3','akabeko2.mp3','akabeko3145']

# pin used in mode i
for i in range(len(IN)):
	GPIO.setup(IN[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(LED[i], GPIO.OUT)

# pin used in LED flush
GPIO.setup(MOTOR, GPIO.OUT)

tmptime=30.0

MUSICDIR = "../music/" #"/home/pi/akabeko_headban/music"

try:
    while True:
	for i in range(len(IN)):
	    if GPIO.input(IN[i]) == True:
	    	while GPIO.input(IN[i]) == True:
	    		continue
		time.sleep(0.5)
            	game.init()
            	game.music.load(MUSICDIR + MUSICS[i])
            	game.music.set_volume(0.3)
            	game.music.play(1)
            	GPIO.output(LED[i], True)
            	intime=time.time()
            	intime2=time.time()
            	flg=True
            	GPIO.output(12, flg)
            	while time.time() - intime < tmptime:
            	    if time.time()-intime2>=BPM[i]/160000.0*2:
                    	flg= not flg
			intime2=time.time()
                    	GPIO.output(MOTOR, flg)
	            if GPIO.input(IN[i]) == True:
			while GPIO.input(IN[i])==True:
				continue
			break
                GPIO.output(MOTOR, False)
		GPIO.output(LED[i],False)
	        game.music.stop()
		time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
