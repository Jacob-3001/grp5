#lyskryds lavet med en Statemachine
from gpiozero import LED
from time import sleep

NSred= LED(13)
NSyellow= LED(19)
NSgreen= LED(26)
EWred= LED(21)
EWyellow= LED(20)
EWgreen= LED(16)

print("test...")
EWred.on()
sleep(1)
EWgreen.on()
sleep(1)
EWyellow.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSyellow.on()
sleep(1)
NSyellow.off()
sleep(1)
NSred.off()
sleep(1)
NSgreen.off()
sleep(1)
EWred.off()
sleep(1)
EWgreen.off()
sleep(1)
EWyellow.off()

def state0(x):#udganspunkt for lyskrydset
    if x=="red":
        x="yellow"
        print("skifter til gul for EW")
        sleep(3)
        EWyellow.on()
        EWred.on()
        NSred.on()
        return state1(x)

def state1(x):
    if x=="yellow":
        x="green"
        print("nu nskifter EW til grønt")
        sleep(3)
        EWyellow.off()
        EWred.off()
        EWgreen.on()
        return state2(x)
        
def state2(x):
    if x=="green":
        x="yellow1"
        print("Nu skifter EW til gult")
        sleep(3)
        EWyellow.on()
        EWgreen.off()
        NSyellow.on()
        return state3(x)

def state3(x):
    if x=="yellow1":
        x="green1"
        print("nu skifter NS til grønt")
        sleep(3)
        EWyellow.off()
        EWred.on()
        NSyellow.off()
        NSred.off()
        NSgreen.on()
        return state4(x)

def state4(x):
    if x=="green1":
        x="red1"
        print("nu skifter NS til gult")
        sleep(3)
        NSgreen.off()
        NSyellow.on()
        return state0(x)

    

    
state=state0(x="red")
while state: state=state0(x="red")
print("så starter lortet")