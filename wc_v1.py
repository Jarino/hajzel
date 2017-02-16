import pygame
from __builtin__ import open
import RPi.GPIO as GPIO
import time
import os
from random import randint

buttonPin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.IN)

pygame.init()
pygame.mixer.init()


c=0
close=0
open=0
open1=0
close1=0

def randomize():
    string1 = str(randint(2,6))
    string = string1 + ".mp3"
    return string

def play_rand(c):
    nazov=randomize()
    pygame.mixer.music.load(nazov)
    time.sleep(1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        if (GPIO.input(buttonPin) == False):  # zistujeme ci su dvere otvorene. ak su dvere otvorene v kazdom cykle sa pripocita
            open1 = 0
        elif (GPIO.input(buttonPin) == True):
            open1 += 1
        if open1<5:
            close1=0
            while close1 < 4:
                if (GPIO.input(buttonPin) == False):
                    close1 += 1
                elif (GPIO.input(buttonPin) == True):
                    close1 = 0
            if close1 == 3:
                time.sleep(2)
                c+= 1
                quit();
    open1=0
    close1=0
    return c

def quit():
    pygame.mixer.music.stop()
    time.sleep(2)

def play(c):
    pygame.mixer.music.load("1.mp3")
    time.sleep(1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        if (GPIO.input(buttonPin) == False):  # zistujeme ci su dvere otvorene. ak su dvere otvorene v kazdom cykle sa pripocita
            open1 = 0
        elif (GPIO.input(buttonPin) == True):
            open1 += 1
        if open1<5:
            close1=0
            while close1 < 4:
                if (GPIO.input(buttonPin) == False):
                    close1 += 1
                elif (GPIO.input(buttonPin) == True):
                    close1 = 0
            if close1 == 3:
                time.sleep(2)
                c+= 1
                quit();
    open1=0
    close1=0
    return c




if __name__ == "__main__":
        while True:
            time.sleep(0.3)
            if (GPIO.input(buttonPin) == False):    #zistujeme ci su dvere otvorene. ak su dvere otvorene v kazdom cykle sa pripocita
                open = 0                            #1 Hlavny cyklus kontroly otvorenia trva 0.3 sekundy
            elif (GPIO.input(buttonPin) == True):
                open+= 1
            if open== 3:
                close=0
                while close<4:
                    if (GPIO.input(buttonPin) == False):
                        close+=1
                    elif (GPIO.input(buttonPin) == True):
                        close=0
                if close<5:
                    c+=1
                    prehrane=play(c)
                    if prehrane==1:
                        prehrane=play_rand(c);

                    while prehrane < 2:
                        if (GPIO.input(buttonPin) == False):
                            d = 0
                        if (GPIO.input(buttonPin) == True):
                            d += 1
                        if d == 3:
                            prehrane += 1
                            time.sleep(7)
        a=0
        prehrane=0
        d=0
        c=0
        open=0
        close=0
#TODO uploadni projekt do hajzla
