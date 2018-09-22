import pandas as pd
import keras
import numpy as np

if __name__ == '__main__':
    print("Hello, World!")

    baseinfo = pd.read_csv('dataset/1baseinfo.csv')

    train = pd.read_csv('dataset/train.csv')

    print(train)
