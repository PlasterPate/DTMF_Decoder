from scipy.io import wavfile as wav
import numpy as np
from itertools import groupby
from matplotlib import pyplot as plt
import os
import DTMF1


def DTMF(signal, rate):

    # Length of the signal in seconds
    length = len(signal) / rate
    # print("\nFile is " + str(length) + " seconds long")

    # print(length)
    chunk_count = int(length / 0.2)

    signal.reshape(signal.shape[0], 1)

    # Divide the signal into smaller pieces
    chunks = np.array_split(signal, chunk_count)
    # print("chunk len:   " + str(len(chunks)))

    res = []
    # Process every chunks to detect key beeps
    for chunk in chunks:
        res.append(DTMF1.DTMF(chunk, rate))

    # Group similar values which are useless
    grouped_res = [x[0] for x in groupby(res)]

    # Concatenate values together
    result = ''.join(grouped_res)


    # Second approach(worse)
    """
    threshold = 400
    ranges = np.array(list())
    last = 0

    # Iterate over signal to find bounds of signal tops where signal in stronger
        
    for i in range(length):
        if np.abs(signal[i]) > threshold:
            if last == 0 or (i - last) > 500:
                ranges = np.append(ranges, last)
                ranges = np.append(ranges, i)
            last = i
    ranges = np.append(ranges, last)
    
    # Seperate starting points and ending points
    final_ranges = np.array([ranges[1::2],
                             ranges[2::2]]).astype(int)
    

    # Calculate average duration of beeps
    mean = np.sum(final_ranges[1] - final_ranges[0]) / final_ranges.shape[1]
    print("\nmean is:" + str(mean))
    
    # Process selected chunks using DTMF1
    for i in range(final_ranges.shape[1]):
        start = final_ranges[0, i]
        end = final_ranges[1, i]
        l = end - start
        if l < mean / 4:
            continue
        result += DTMF1.DTMF(signal[start:end], rate)
    """
    # print(result)

    # plt.plot(signal.real)
    # plt.show()

    return result
