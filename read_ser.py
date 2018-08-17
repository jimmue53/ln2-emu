# this program takes input from COM5 ( use PUTTY), and outputs on the terminal.  Type q into session to quit.

import serial
import sys
import msvcrt
chillser = serial.Serial('COM3', 9600, timeout=0.1 )
# s = chill.write(b'hello');

QuitIt = False
while (not QuitIt) :
  bin = chillser.read()
  strin = bin.decode("utf-8") #create string from bytearray
  if strin != '':
      msvcrt.putch(bin )
      if strin == '\r' :
        msvcrt.putch('\n'.encode("utf-8")) #create byte from string and output
  if msvcrt.kbhit() :
     c=msvcrt.getch()
     cstr = c.decode("utf-8")
     if cstr == 'q' :
         QuitIt = True

  
    
