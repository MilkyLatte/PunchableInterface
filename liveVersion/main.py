from soundRecorder import soundRecorder
from sensorRecorder import sensorRecorder
from multiprocessing import Process
from segmentator import segmentator
from classifier import classifier
from featureExtractor import featureExtractor
from threading import Thread
import numpy as np
import peakutils

soundNew = []
sensorNew = []
recorder = soundRecorder
sensors = sensorRecorder
segmenter = segmentator
featureExtraction = featureExtractor
decisions = classifier


def runInParallel(timeSensor, timeSound):
    stream = recorder.createStream(recorder)
    Process(target=sensorHandler(sensors, timeSensor)).start()
    Process(target=soundHandler(recorder, timeSound, stream)).start()


def sensorHandler(recorder, time):
    global sensorNew
    sensorNew = recorder.record(recorder, time)


def soundHandler(recorder, time, stream):
    global soundNew
    soundNew = recorder.record(recorder, time, stream)
    print(len(soundNew))


def predict(features):
    print("Your Sequence was: ")
    for i in decisions.linearClassifier.predict(features):
        if i == 0:
            print("Jab\n")
        elif i == 1:
            print("Palm Strike\n")
        elif i == 2:
            print("Hook\n")
        elif i == 3:
            print("Back Fist")
        elif i == 4:
            print("Uppercut")
    input("Press any key to continue")


def keyboardWait():
    x = input("press C to do another round")
    if x == 'c' or x == 'C':
        pass


def brain():
    global sensorNew
    global soundNew
    decisions.loadData(decisions)
    decisions.trainClassifier(decisions)
    input("done loading, press any key to start punching")
    while 1:
        print("recording...")
        runInParallel(7000, 7)
        print("segmenting")
        soundConfirm, soundPunch = segmenter.soundSegment(segmenter, soundNew)
        sensorConfirm, sensorPunch = segmenter.sensorSegment(segmenter, sensorNew)
        print("classifying")
        if soundConfirm and sensorConfirm:
            if len(soundPunch) == len(sensorPunch):
                features = []
                for x in range(len(sensorPunch)):
                    features.append(featureExtraction.extract(featureExtraction, sensorPunch[x], soundPunch[x]))
                features = np.array(features)
                predict(features)
            else:
                print("the punches detected don't match")
        else:
            input("no punches where detected press any key to continue")
        keyboardWait()


def main():
    brain()


if __name__ == '__main__':
    main()
