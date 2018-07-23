import numpy as np


class segmentator():
    def soundSegment(dataSound):
        soundIncluded = 0
        punchSound = []
        punch = False
        for x in range(len(dataSound)):
            if abs(dataSound[x]) >= 1200 and x > soundIncluded:
                currentPunch = []
                punch = True
                for i in range(400):
                    try:
                        currentPunch.append(dataSound[x+i])
                    except Exception:
                        pass
                punchSound.append(currentPunch)
                soundIncluded = x + 300
        punchSound = np.array(punchSound)
        return(punch, punchSound)

    def sensorSegment(dataSensor):
        dataSensor = np.array(dataSensor)
        print(dataSensor.shape)
        accelMean = np.mean(dataSensor[0:, :3], axis=1)
        included = 0
        punch = []
        confirm = False
        for x in range(len(accelMean)):
            if (accelMean[x]) >= 13700 and x > included:
                confirm = True
                currentPunch = []
                xvalue = x - 50
                for i in range(100):
                    try:
                        currentPunch.append(dataSensor[xvalue + i])
                    except Exception:
                        pass
                punch.append(currentPunch)
                included = x+50
        punch = np.array(punch)
        return(confirm, punch)
