"""
    @Name: function.py
    @Author: Yang Yicheng
    @Time: 2022/5/9
"""


import os
from record import Record
import time
from models import *


def pre_load_model():
    time_start = time.time()
    print('Loading model...')
    asr_model('./wav/1.wav')

    time_end = time.time()
    os.system('clear')
    print("Model Load! Cost: %.3fs" % (time_end - time_start))


def record_and_recognize():
    Record()
    time_start = time.time()
    text = asr_model('./temp.wav')
    time_end = time.time()
    os.system('clear')
    os.remove('./temp.wav')
    print("Predict time: %.3fs" % (time_end - time_start))
    print('ASR Result: {}'.format(text))
