from serial import *
from serial.threaded import *
import traceback
from pprint import pprint
import json

remote = {}

class PrintSerial(Protocol):
    def connection_made(self, transport):
        super(PrintSerial, self).connection_made(transport)
        self.buf = []

    def data_received(self, data):
        self.buf.append(data)

    def connection_lost(self, exc):
        if exc:
            traceback.print_exc(exc)

    def savedata(self, ident):
        remote[ident] = list(self.buf)

    def printdata(self):
        for chunk in self.buf:
            print("{:02X}".format(ord(chunk)), end=" ")
        print()
        self.buf = []

    def cleardata(self):
        self.buf = []

def encode(obj):
    return ' '.join(x.hex() for x in obj)

s = serial.Serial("/dev/ttyUSB0")
with ReaderThread(s, PrintSerial) as protocol:
#   protocol.write(rb'\xA1\xF1')
    filename = input("What should this remote be called? ")
    while 1:
        name = input("Press button, enter name, hit enter (in that order): ")
        if name == "q":
            break
        protocol.savedata(name)
        protocol.printdata()
        pprint(remote)

remote2 = {x : encode(y) for x, y in remote.items()}
f = open(filename+'.json', "w")
json.dump(remote2, f)
f.close()
print("File written.")
