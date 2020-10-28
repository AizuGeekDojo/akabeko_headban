#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import pygame.mixer as game

GPIO.setmode(GPIO.BCM)

# pin used in mode 1
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)

# Pin used in mode 2
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

# pin used in mode 3
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)

# pin used in LED flush
GPIO.setup(12, GPIO.OUT)

tmptime=30.0

MUSIC_DIR = "/home/pi/akabeko_headban/music/"


try:
    while True:
        if GPIO.input(20) == True:
            game.init()
            game.music.load(MUSICDIR + 'akabeko1.mp3')
            game.music.play(1)
            GPIO.output(23, True)
            intime=time.time()
            nowtime=intime

            while nowtime - intime < tmptime:
                GPIO.output(12, True)
                time.sleep(60.0/160000*2)
                GPIO.output(12, False)
                time.sleep(60.0/160000*2)
                nowtime=time.time()

            game.music.stop()

        if GPIO.input(21) == True:
            game.init()
            game.music.load(MUSICDIR + 'akabeko2.mp3')
            game.music.play(1)
            GPIO.output(18, True)
            intime=time.time()
            nowtime=intime

            while nowtime - intime < tmptime:
                GPIO.output(12, True)
                time.sleep(116.0/160000*2)
                GPIO.output(12, False)
                time.sleep(116.0/160000*2)
                nowtime=time.time()

            game.music.stop()

        if GPIO.input(24) == True:
            game.init()
            game.music.load(MUSICDIR+'akabeko3145.mp3')
            game.music.play(1)
            GPIO.output(17, True)
            intime=time.time()
            nowtime=intime

            while nowtime - intime < tmptime:
                GPIO.output(12, True)
                time.sleep(145.0/160000)
                GPIO.output(12, False)
                time.sleep(145.0/160000)
                nowtime=time.time()

            game.music.stop()
        else:
            GPIO.output(23, False)
            GPIO.output(17, False)
            GPIO.output(18, False)
            time.sleep(0.1)


except KeyboardInterrupt:
    GPIO.cleanup()
