#press home will play the song,end key will stop the song

from pynput import keyboard
from playsound import playsound
import multiprocessing

def playsong():
    playsound(sound="song.wav")  # song's file format must be wav

p = multiprocessing.Process(target=playsong)

def on_press(key):
    global p
    if key==keyboard.Key.home:
        if p.is_alive():
            p.terminate()
            p = multiprocessing.Process(target=playsong)
            p.start()
        else:
            p = multiprocessing.Process(target=playsong)
            p.start()
    if key == keyboard.Key.end:
        if p.is_alive():
            p.terminate()

def on_release(key):
    pass
    # if key == keyboard.Key.esc: # press esc to stop
    #     return False

if __name__ == '__main__':
    multiprocessing.freeze_support()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
