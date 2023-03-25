from replit import audio
import os, time

    
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 to stop music "))
    if stop_playback == 2:
      source.paused = True 
      return 
    else: 
      continue


while True:
    os.system("clear") # Changed to "cls" in newer Python
    print("🎵 Happy Pants Music Player 🎵\n")
    time.sleep(1)
    print("Press 1 to PLAY ")
    time.sleep(0.5)
    print("Press 2 to EXIT ")
    time.sleep(0.5)
    print("Press any button for menu ")
    userChoice = int(input())
    if userChoice == 1:
        print("Music baby!! Woo Woo ")
        play()
    elif userChoice == 2:
        exit()
    else:
        continue