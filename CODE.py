Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import board
... from kmk.kmk_keyboard import KMKKeyboard
... from kmk.keys import KC
... from kmk.scanners.keypad import PinsScanner
... 
... from kmk.extensions.media_keys import MediaKeys 
... 
... keyboard = KMKKeyboard()
... 
... keyboard.extensions.append(MediaKeys())
... 
... keyboard.matrix = PinsScanner(
...     [board.D0, board.D1, board.D2, board.D3, board.D4],
...     value_when_pressed=False
... )
... 
... keyboard.keymap = [
...     [
...         KC.LCTRL(KC.C),           # Switch 1: Copy (Ctrl + C)
...         KC.LCTRL(KC.V),           # Switch 2: Paste (Ctrl + V)
...         KC.AUDIO_MUTE,            # Switch 3: Mute / Unmute Toggle
...         KC.LGUI(KC.LSFT(KC.S)),   # Switch 4: Snipping Tool (Win + Shift + S)
...         KC.MEDIA_PLAY_PAUSE,      # Switch 5: Play / Pause Media
...     ]
... ]
... 
... if __name__ == '__main__':
