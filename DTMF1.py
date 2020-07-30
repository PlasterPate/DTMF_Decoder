from scipy.io import wavfile as wav
import numpy as np
import os
import random
import itertools


keymap = [
    ['0', 941, 1336],
    ['*', 941, 1209],
    ['#', 941, 1477],

    ['1', 697, 1209],
    ['2', 697, 1336],
    ['3', 697, 1477],

    ['4', 770, 1209],
    ['5', 770, 1336],
    ['6', 770, 1477],

    ['7', 852, 1209],
    ['8', 852, 1336],
    ['9', 852, 1477],

    ['A', 697, 1633],
    ['B', 770, 1633],
    ['C', 852, 1633],
    ['D', 941, 1633]
]

def findNearest(f1, f2, min):
    answer = ''
    for key in keymap:
        dist1 = np.abs(f1 - key[1]) + np.abs(f2 - key[2])
        dist2 = np.abs(f1 - key[2]) + np.abs(f2 - key[1])
        dist = np.min([dist1, dist2])
        if dist < min:
            min = dist
            answer = key[0]
    return answer, min

def DTMF(signal, rate):

    ##################################
              ####   write your code here   ####
    ##################################
    result = ''

    DTFT = np.fft.fft(signal)[range(int(len(signal)/2))]
    DTFT_abs = np.abs(DTFT)
    high_amp = np.sort(DTFT_abs)[-7:]

    high_f = np.array([])
    for f in high_amp:
        high_f = np.append(high_f, np.where(DTFT_abs == f)[0])

    if high_f.shape[0] != 7:
        return ''

    sec = rate / len(signal)
    high_f = np.array(high_f) * sec

    min = 10
    for a, b in itertools.combinations(high_f, 2):
        result_temp, dist = findNearest(a, b, min)
        if dist < min:
            min = dist
            result = result_temp

    # print(result)


    ### PAY ATTENTION: you should return the string of what you have found


    ### a sample csv file is attached: 'Phase1-Label-Test-Sample.csv'
    ### ba sure that you are saving data in the right format

    ### it's obvious that your score is loss! so the closer to zero, the better algorithm.

    return result

