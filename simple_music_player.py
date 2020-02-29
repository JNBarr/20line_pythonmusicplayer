# python music player in 20 lines of code!

from pygame import mixer

mixer.init() # start the mixer?

mixer.music.load("song.mp3") # load the song
mixer.music.set_volume(0.7) # set the volume
mixer.music.play() # play the mixer

while True:
    print("Press 'p' to pause and 'r' to resume ")
    print("Press 'e' to exit the program")
    query = input (">>> ")

    if query == 'p':
        mixer.music.pause() # pause music
    elif query == 'r':
        mixer.music.unpause() # unpause music
    elif query == 'e':
        mixer.music.stop() # stop the music
        break