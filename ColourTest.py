from Adafruit_IO import *
aio = Client('getyourownAPIKeyplz')
def ChangeColour(inputColour):
    choices = {'blue':(0,0,253),'red':(255,0,0),'green':(0,255,0),'orange':(254,138,0),'yellow':(254,254,0)}
    result = choices.get(inputColour)
    print(result)

while True:
    ChangeColour(input('enter colour'))
