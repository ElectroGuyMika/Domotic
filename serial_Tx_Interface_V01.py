# -*- coding: utf-8 -*-
################################################
#            serial Tx INTERFACE V1.0          #
#                                              #
#   written by Qi TANG             29.04.2014  #
#   modified by Mickaël CAPTANT    29.05.2014  #
#                                              #
# Description: Transmit data to Serial port    #
#                                              #
################################################

## HOW TO TEST
## Open a serial port COM1 and tape that in command line:
    ## python serial_Tx_Interface_V01.py $.02-02.00-01.R11.R21.R30.#

##import all librairies we needed
import serial
from ConfigParser import SafeConfigParser
import time
import sys

##Initiation of the variables with .conf file
def  initVariables():
    ##open the conf file
    cfg = SafeConfigParser()
    cfg.read('config.ini')
    ##Define Serial Port
    global serialPort
    global baud
    global serial1
    serialPort = cfg.get('SERIAL_PORT', 'serialPort')
    baud = cfg.get('SERIAL_PORT', 'baud')
    serial1 = serial.Serial(serialPort, baud)
    ##Define file for data logging
    global log
    log = cfg.get('LOG', 'logTx')

def logger(dataToLog,fileToLog):
    logFile = open(fileToLog, 'a')
    logBuffer = time.strftime("%d %m %Y %H:%M:%S") + ">" + dataToLog + "\r"
    logFile.write(logBuffer)

def serialWrite(commandToSend):
    global serial1
    ##Make a loop to instaure a delay
    #for x in range(0 ,len(commandToSend)):
        #serial1.write(commandToSend[x])
        #time.sleep(0.003)
    ##Without delay
    serial1.write(commandToSend)

def main():
    initVariables()
    lenArg = len(sys.argv)
    if lenArg == 2:
        TxBuffer = sys.argv[1]
	logger(TxBuffer[1:],log)
    	serialWrite(TxBuffer[1:])
    if lenArg == 1:
	print "ERROR SYSTEM nb 202"

if __name__ == "__main__":
    main()
