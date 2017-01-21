import pygame
import RPi.GPIO as GPIO
import time
import os

buttonPin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.IN)

pygame.init()
pygame.mixer.init()
a=0
b=0
c=0
d=0
x=0
def quit():
         pygame.mixer.music.stop()
#        print 'quit'

def play(c):
        pygame.mixer.music.load("1.mp3")
        time.sleep(3)
        pygame.mixer.music.play()
        before=GPIO.input(buttonPin)
        time.sleep(3)
        while pygame.mixer.music.get_busy()==True:
                if (GPIO.input(buttonPin)==False):
                        b=0
                if (GPIO.input(buttonPin)==True):
                        b+=1
                if b==5:
#                       print 'quit'
                        time.sleep(5)
#                       print 'open'
#                       print before
                        c+=1
                        quit();
                        time.sleep(5)
        a=0
        b=0
        return c

#       if pygame.mixer.music.get_busy()==False:
#               quit()


if __name__ == "__main__":
        while True:
#                print 'binit'
#                print GPIO.input(buttonPin)
                time.sleep(0.5)
                if (GPIO.input(buttonPin)==False):
                        a=0
                if (GPIO.input(buttonPin)==True):
                        a+=1
                if a==3:
                        c+=1
#                       print c
                        pomocna=play(c);
#                       c+=pomocna
#                       print pomocna
#                       print 'pred' + c
                        while pomocna<2:
                                if (GPIO.input(buttonPin)==False):
                                        d=0
                                if (GPIO.input(buttonPin)==True):
                                        d+=1
                                if d==3:
                                        pomocna+=1
#                                       print pomocna
#                                       print 'in loop'
                                        time.sleep(7)
#                       print 'out loop'
                pomocna=0
                c=0
                d=0




