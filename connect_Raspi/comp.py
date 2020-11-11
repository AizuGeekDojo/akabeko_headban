#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import pygame.mixer as game
import os

GPIO.setmode(GPIO.BCM)

# input pin
IN = [20, 21, 24]
# led pin( these pins don't use now )
LED = [23, 18, 17]
# BPM
BPM = [80, 116, 145]
# MOTOR control pin
MOTOR = 12

# music dir and names
MUSICDIR = "/home/pi/akabeko_headban/music"
MUSICS_NAME = ['akabeko1.mp3','akabeko2.mp3','akabeko3145.mp3']

# pin used in mode i
for in_p, led in zip(IN, LED):
	GPIO.setup(in_p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(led, GPIO.OUT)

# music init
MUSICS=[os.path.join(MUSICDIR,name) for name in MUSICS_NAME]

# pin used in LED flush
GPIO.setup(MOTOR, GPIO.OUT)

tmptime = 30.0

game.init()

try:
	while True:
		for in_p, led, music, bpm in zip(IN, LED, MUSICS, BPM):
			if GPIO.input(in_p):
				while GPIO.input(in_p):
					continue
				time.sleep(0.5)
				game.music.load(music)
				game.music.set_volume(0.3)
				game.music.play(1)
				GPIO.output(led, True)
				intime=time.time()
				intime2=time.time()
				flg=True
				GPIO.output(MOTOR, flg)
				while time.time() - intime < tmptime:
					if time.time()-intime2>=bpm/160000.0*2:
						flg= not flg
						intime2=time.time()
						GPIO.output(MOTOR, flg)
					if GPIO.input(in_p):
						break
				GPIO.output(MOTOR, False)
				GPIO.output(led,False)
				game.music.stop()
				while GPIO.input(in_p):
					continue
				time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
