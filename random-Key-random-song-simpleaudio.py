# press anykey will play the song

from pynput import keyboard
import simpleaudio as sa
from random import randrange

first=1
finial=5 # total song amount
wave_obj = sa.WaveObject.from_wave_file("song{randrange(first,finial)}.wav") # random play song
play_obj = wave_obj.play()
play_obj.stop()

keylist = [e for e in keyboard.Key]
keylist.remove(keyboard.Key.f13)
keylist.remove(keyboard.Key.f14)
keylist.remove(keyboard.Key.f15)
keylist.remove(keyboard.Key.f16)
keylist.remove(keyboard.Key.f17)
keylist.remove(keyboard.Key.f18)
keylist.remove(keyboard.Key.f19)
keylist.remove(keyboard.Key.f20)
keylist.remove(keyboard.Key.f21)
keylist.remove(keyboard.Key.f22)
keylist.remove(keyboard.Key.f23)
keylist.remove(keyboard.Key.f24)
keylist.remove(keyboard.Key.scroll_lock)
keylist.remove(keyboard.Key.num_lock)
keylist.remove(keyboard.Key.print_screen)
# print(keylist)
bingo = keylist[randrange(0, len(keylist))]
# print(bingo)

def on_press(key):
    global play_obj
    global bingo
    if key == bingo:
        if play_obj.is_playing():
            play_obj.stop()
            play_obj = wave_obj.play()
        else:
            play_obj = wave_obj.play()
        bingo = keylist[randrange(0, len(keylist))]
        # print(bingo)


def on_release(key):
    pass
# if key == keyboard.Key.esc: # press esc to stop
#     return False


if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
