import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

activation_toggle_key = KeyCode(char="y")

clicking_process_active = False
mouse_hardware_controller = Controller()

def perform_clicking_task():
    global clicking_process_active 
    while True:
        if clicking_process_active:
            mouse_hardware_controller.click(Button.left, 1)
            time.sleep(0.03)
        else:
            time.sleep(0.1)
        
def toggle_event(pressed_keyboard_key): 
    if pressed_keyboard_key == activation_toggle_key:
        global clicking_process_active
        clicking_process_active = not clicking_process_active
        print(f"Clicking: {clicking_process_active}")

click_thread = threading.Thread(target=perform_clicking_task)
click_thread.daemon = True 
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()