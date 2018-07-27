from soundRecorder import soundRecorder
from sensorRecorder import sensorRecorder
from multiprocessing import Process
from segmentator import segmentator
import numpy as np

soundNew = []
sensorNew = []
recorder = soundRecorder
sensors = sensorRecorder
segmenter = segmentator
featureExtraction = featureExtractor


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
    while 1:
        runInParallel()
        soundConfirm, soundPunch = segmenter.soundSegment(soundNew)
        sensorConfirm, sensorPunch = segmenter.sensorSegment(sensorNew)
        if soundConfirm and sensorConfirm:
            if len(soundPunch) == len(sensorPunch):
                features = []
                for x in range(len(sensorPunch)):
                    features.append(featureExtraction.extract(featureExtraction, sensorPunch[x], soundPunch[x]))






def main():
    brain()


if __name__ == '__main__':
    main()
