#press anykey will play the song

from pynput import keyboard
import os
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file(os.getcwd()+"\\song.wav")
play_obj = wave_obj.play()
play_obj.stop()

def on_press(key):
    global play_obj
    if key == keyboard.Key.home:
        if play_obj.is_playing():
            play_obj.stop()
            play_obj = wave_obj.play()
        else:
            play_obj = wave_obj.play()
    if key==keyboard.Key.end:
        play_obj.stop()

def on_release(key):
    pass
    # if key == keyboard.Key.esc: # press esc to stop
    #     return False

if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
