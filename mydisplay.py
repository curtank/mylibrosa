import pickle
import threading
import time,datetime
import random
#import mp3play
#beat=pickle.load(open('beattimes','rb'))
#print beat
def out(num):
    print '*',str(num)
filename='/home/curtank/Music/CloudMusic/avi.ogg'
#filename='/home/curtank/Music/CloudMusic/s1.ogg'

import pygame
pygame.mixer.init()
pygame.mixer.music.load(filename)

sttime=0
beatfile=open('beat_times.csv','r')
num=0
for time in beatfile.readlines():
    dtime=float(time)-float(sttime)
    sttime=float(time)
    #print type(dtime)
    timer=threading.Timer(float(time),out,(num,))
    timer.start()
    
    num+=1

pygame.mixer.music.play()
print '*start'

#from pygame import mixer
#mixer.init()
#mixer.music.load(filename)
#mixer.music.play()
#timer=threading.Timer(0,play)