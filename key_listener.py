from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'a':
            print("Натиснута клавіша 'A'")
        elif key.char == 'd':
            print("Натиснута клавіша 'D'")
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char == 'a':
            print("Відпущена клавіша 'A'")
            keyboard.Controller().press('d')
            keyboard.Controller().release('d')
            print("Натиснута клавіша 'D'")
        elif key.char == 'd':
            print("Відпущена клавіша 'D'")
            keyboard.Controller().press('a')
            keyboard.Controller().release('a')
            print("Натиснута клавіша 'A'")
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()