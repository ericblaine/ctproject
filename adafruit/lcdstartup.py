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
# autoscroll on
matrixwritecommand([0x58])
matrixwritecommand([0x51])

ser.write("Loading Chrono  ");
ser.write("Trigger Project");
time.sleep(7)
matrixwritecommand([0x58])
ser.write("Press A or B to");
ser.write("begin music...");
time.sleep(7)

matrixwritecommand([0x58])

# turn off display
matrixwritecommand([0x46])
time.sleep(0.3);
