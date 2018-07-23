from soundRecorder import soundRecorder
from sensorRecorder import sensorRecorder
from multiprocessing import Process
from segmentator import segmentator
import numpy as np

soundOld = []
soundNew = []
sensorOld = []
sensorNew = []
recorder = soundRecorder
sensors = sensorRecorder
segmenter = segmentator


def runInParallel():
    p1 = Process(target=sensorHandler(sensors))
    p1.start()
    p2 = Process(target=soundHandler(recorder))
    p2.start()
    p1.join()
    p2.join()


def sensorHandler(recorder):
    global sensorNew
    sensorNew = recorder.record(recorder, 10000)


def soundHandler(recorder):
    global soundNew
    soundNew = recorder.record(recorder, 10)


def brain():
        runInParallel()
        soundConfirm, soundPunch = segmenter.soundSegment(soundNew)
        sensorConfirm, sensorPunch = segmenter.sensorSegment(sensorNew)
        if soundConfirm:
            print("Sound")
        if sensorConfirm:
            print("Sensor")



def main():
    brain()


if __name__ == '__main__':
    main()
