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

'''
import pyglet
filename='/home/curtank/Music/CloudMusic/Avicii - The Nights (Original Mix).mp3'
import pyglet
pyglet.options['audio'] = ('pulse', 'alsa')

window = pyglet.window.Window(width=800, height=600)

player=pyglet.media.Player()
# == Queue more tracks,
#    the label will update automatically
player.queue( pyglet.media.load(filename, streaming=True) )
player.volume=0.3

# window is the variable 'window' from earlier.
@window.event
def on_draw():
    window.clear()

    if player.playing:
        label = pyglet.text.Label('{artist} - {song}'.format(**{'artist' : player.source.info.author.decode('UTF-8'),
                                                                'song' : player.source.info.title.decode('UTF-8')}),
                              font_size=36,
                              x=window.width//2, y=window.height//2, # same here, window on line 6
                              anchor_x='center', anchor_y='center')
    else:
        label = pyglet.text.Label('Music paused!', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
    label.draw()

    window.flip() # This is overkill but ensures proper rendering at all times.

@window.event
def on_key_press(symbol, modifiers):
    # Up and Down controls the volume for instance
    if symbol == pyglet.window.key.UP:
        player.volume = player.volume+0.1
    elif symbol == pyglet.window.key.DOWN:
        player.volume = player.volume-0.1

    # Any key really will start/pause the playback
    elif player.playing:
        player.pause()
    else:
        player.play()

pyglet.app.run()
'''
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