import numpy as np
import pandas as pd
from sodapy import Socrata
import json
from urllib.request import urlopen
from pprint import pprint


# load peachtree csv file and seperate by vehicle
data_type = [int, int, int, int, float, float, float, float, float, float, int, float, float, int, int, int, int, int, int, int, int, int, int, float, float]
peachtree_data_file = './data/peachtree_all.csv'
raw_data = np.loadtxt(peachtree_data_file, dtype=float, delimiter=',', skiprows=1, usecols=range(24))
print(raw_data.shape)

print(type(raw_data))
raw_data[:, :5].astype(int)
print(raw_data[:2, :])