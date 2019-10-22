import serial
import sys
import time

# 16x2 LCD:
ROWS = 2
COLS = 16

def matrixwritecommand(commandlist):
    commandlist.insert(0, 0xFE)
    #ser.write(bytearray([0xFE]))
    #time.sleep(0.1);
    for i in range(0, len(commandlist)):
         #print chr(commandlist[i]),
         ser.write(chr(commandlist[i]))
    #ser.write(bytearray(commandlist))

# 1. get serial port
if len(sys.argv) != 2:
    print "Usage: python test.py <serialport>"
    exit(0)

ser = serial.Serial(sys.argv[1], 9600, timeout=1)
matrixwritecommand([0x58])

# set size
matrixwritecommand([0xD1, COLS, ROWS]);
matrixwritecommand([0x58])

# set color
matrixwritecommand([0xD0, 200, 0, 0])
time.sleep(0.005)

# Write text to screen
# New line begins...      X               X
ser.write("Playing         Time Circuits");
time.sleep(4)

#matrixwritecommand([0x58])

