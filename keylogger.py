from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key


def controlMouse():
    mouse = MouseController()
    mouse.position = (860, 20)
    mouse.click(Button.left, 2)
    print(f"Mouse moved to: {mouse.position}")

def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    keyboard.type('www.google.com') 


def enter():
    keyboard = KeyboardController()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

controlMouse()
controlKeyboard()
enter()