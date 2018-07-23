import serial
import numpy as np
import matplotlib as plt
from drawnow import *
import time
import csv

#arduinoData = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_85431303736351A09150-if00', 115200)
start = int(round(time.time()*1000))
#arduinoData = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_85431303736351A09150-if00', 1000000)
arduinoData = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 1000000)

data = []


def makeFig():
    plt.plot(data[0:, 6], data[0:, 0])
    plt.show


executingTime = 0

with open('sensorInfo.csv', 'w') as appendFile:
    newFileWriter = csv.writer(appendFile)
    # newFileWriter.writerow(['acX', 'acY', 'acZ', 'gyX', 'gyY', 'gyZ', 'time'])
    while executingTime < 25000:
        while (arduinoData.inWaiting() == 0):
            pass
        arduinoString = arduinoData.readline()
        dataArray = arduinoString.decode().split(',')
        try:
            pointlessVariable = "Pointless"
            acX = float(dataArray[0])
            acY = float(dataArray[1])
            acZ = float(dataArray[2])

            gyX = float(dataArray[3])
            gyY = float(dataArray[4])
            gyZ = float(dataArray[5])
            currentTime = int(round(time.time()*1000))
            timer = currentTime - start
            new = [acX, acY, acZ, gyX, gyY, gyZ]
            print("Not")
            newFileWriter.writerow(new)
            data.append(new)
        except Exception:
            pass
        executingTime = int(round(time.time()*1000)) - start

print("Done")
