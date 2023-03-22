from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen 

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input