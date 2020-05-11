#Power budget

def sm1310nm():
        print("")
        print("output power=", outputpower, "dBm")
        print("recieversensitivity=", recieversensitivity, "dBm")
        print("brutto overskud=", outputpower-recieversensitivity, "dB")
        print("")
        print(konnektreringer, "konnekteringer", konnektreringer*0.5, "dB")
        print(splidsninger, "splidsninger", splidsninger*0.1, "dB")
        print(længde, "km", fiber, længde*0.35, "dB")
        print("linkmargin=", (outputpower-recieversensitivity)-((konnektreringer*0.5)+(splidsninger*0.1)+(længde*0.35)), "dB")
        print("")
        print("sikkerhedsmargin = 3 dB")
        print("reparationer = 0.5 dB")
        print("nettooverskud=", (outputpower-recieversensitivity)-((konnektreringer*0.5)+(splidsninger*0.1)+(længde*0.35))-(3.5), "dB")
        exit(0)

def sm1550nm():
        print("")
        print("output power=", outputpower, "dBm")
        print("recieversensitivity=", recieversensitivity, "dBm")
        print("brutto overskud=", outputpower-recieversensitivity, "dB")
        print("")
        print(konnektreringer, "konnekteringer", konnektreringer*0.5, "dB")
        print(splidsninger, "splidsninger", splidsninger*0.1, "dB")
        print(længde, "km", fiber, længde*0.2, "dB")
        print("linkmargin=", (outputpower-recieversensitivity)-((konnektreringer*0.5)+(splidsninger*0.1)+(længde*0.2)), "dB")
        print("")
        print("sikkerhedsmargin = 3 dB")
        print("reparationer = 0.5 dB")
        print("nettooverskud=", (outputpower-recieversensitivity)-((konnektreringer*0.5)+(splidsninger*0.1)+(længde*0.2))-(3.5), "dB")
        exit(0)

fiber = input("vælg mellem sm 1310nm eller sm 1550nm?")
outputpower = int(input("hvad er din output power?"))
recieversensitivity = int(input("hvad er din reciever sensitivitet?"))
konnektreringer = int(input("hvor mange konnekteringer har du?"))
splidsninger = int(input("hvor mange splidsninger har du?"))
længde = float(input("hvor langt er dit fiber stræk i km?"))

while True:
    while fiber=="sm 1310nm":
        sm1310nm()
    while fiber=="sm 1550nm":
        sm1550nm()