#!/usr/bin/python3

from serial import *
import serial
import json
import sys

def decode(obj):
    return bytes([int(x, 16) for x in obj.split(' ')])


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./tx.py <remote> <key>")

    rfn = sys.argv[1]
    keyn = sys.argv[2]

    f = open(rfn+'.json', "rb")
    remotestr = json.load(f)
    f.close()

    remote = {x : decode(y) for x, y in remotestr.items()}
#    print(remote[keyn])
    
    s = serial.Serial("/dev/ttyUSB0")
    s.write(b'\xA1\xF1' + remote[keyn])
    s.flush()
    s.close()

