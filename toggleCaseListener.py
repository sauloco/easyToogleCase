import pyautogui
import pyperclip
import time
from pynput import keyboard

'''
    If the pressed key is caps_lock save the clipboard, 
    execute a Ctrl/Cmd+C (copy) key combination, get the 
    text just copied and overwrite it with its lower or 
    upper case, depends on the current state of caps_lock 
    in your system.

    Param:
        key, a keyboard key
'''
def on_press(key):
    try:
        if key == keyboard.Key.caps_lock:
            predata = pyperclip.paste()
            pyautogui.hotkey('ctrl','c')
            # get clipboard data
            data = pyperclip.paste()
            if data == '' or data == predata:
                return
            pyautogui.typewrite(data.lower())
            pyperclip.copy(predata)
    except AttributeError:
        return

'''
    The escape clause is the Esc key, by now.
    //TODO: create a harder to reach escape key combination like Ctrl+Pause, or something like that.
    Param:
        key, a keyboard key
'''
def on_release(key): 
    if key == keyboard.Key.esc:
        # Stop listener
        return False

'''
    Collect events until released with Esc key
'''
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()  