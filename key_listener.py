from pynput import keyboard
import threading

a_pressed_once = False
d_pressed_once = False
action_completed = False  

def reset_state():
    global a_pressed_once, d_pressed_once, action_completed
    a_pressed_once = False
    d_pressed_once = False
    action_completed = False  
    print("Скидання стану через таймер. Можна знову натискати 'A' і 'D'.")

def on_press(key):
    global a_pressed_once, d_pressed_once, action_completed
    if action_completed:  
        return
    
    try:
        if key.char == 'a' and not a_pressed_once:
            print("Натиснута клавіша 'A'")
        elif key.char == 'd' and not d_pressed_once:
            print("Натиснута клавіша 'D'")
    except AttributeError:
        pass

def on_release(key):
    global a_pressed_once, d_pressed_once, action_completed
    if action_completed:  
        return
    
    try:
        if key.char == 'a' and not a_pressed_once:
            print("Відпущена клавіша 'A'")
            keyboard.Controller().press('d')
            keyboard.Controller().release('d')
            print("Натиснута клавіша 'D'")
            a_pressed_once = True  
            action_completed = True  
            threading.Timer(0.001, reset_state).start()  
        elif key.char == 'd' and not d_pressed_once:
            print("Відпущена клавіша 'D'")
            
            keyboard.Controller().press('a')
            keyboard.Controller().release('a')
            print("Натиснута клавіша 'A'")
            d_pressed_once = True  
            action_completed = True  
            threading.Timer(0.001, reset_state).start()  
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    