# modeling/statistics.py
import numpy as np

def calculate_mean(data):
    return np.mean(data)

def calculate_median(data):
    return np.median(data)

def calculate_standard_deviation(data):
    return np.std(data)

def calculate_variance(data):
    return np.var(data)

def calculate_mode(data):
    # Note: numpy's mode function returns the mode along with its frequency
    mode_result = np.mode(data)
    mode = mode_result.mode[0]
    frequency = mode_result.count[0]
    return mode, frequency
