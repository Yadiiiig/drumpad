from browser import document, html
from browser.html import AUDIO, SOURCE
import javascript

sounds = ['sound1.wav', 'sound2.wav', 'sound3.wav', 'sound4.wav', 'sound5.wav', 'sound6.wav', 'sound7.wav', 'sound8.wav']
keys = {'49': 'pad0', '50': 'pad1', '51': 'pad2', '52': 'pad3', '53': 'pad4', '54': 'pad5', '55': 'pad6', '56': 'pad7', '57': 'pad8'}

def load_sounds():
    count = 0
    for sound in sounds:
        audioTag = AUDIO(id = 'pad' + str(count))
        audioTag <= SOURCE(src = 'sounds/' + sound, )
        document <= audioTag
        count += 1

def charCode(ev):
    trace = document["traceCharCode"]
    char = chr(ev.charCode)

    try:
        document[keys[str(ev.charCode)]].play()
    except:
        pass

def padPress(ev):
    print(document["test"].name)
    document["pad0"].play()

load_sounds()
document["charCode"].bind("keypress", charCode)
document["test"].bind("click", padPress)