from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (102, 20)
    print(f"Mouse moved to: {mouse.position}")

def controlKeyboard():
    keyboard = Controller()
    keyboard.type('My Name is Emmanuel, Growing!!') 


controlKeyboard()