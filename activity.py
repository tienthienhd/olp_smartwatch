import numpy as np
import pandas as pd
import preprocess
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier


def segment_window(data, time_split):
    results = list()
    timestamps = data[['timestamps']].values
    start_time = timestamps[0]
    start_index = 0
    for idx, current_time in enumerate(timestamps[1:]):
        delta = current_time - start_time
        if delta >= time_split:
            results.append(data.loc[start_index: idx, ['yaw', 'pitch', 'roll', 'ax', 'ay', 'az']].values)
            start_index = idx + 1
            start_time = timestamps[start_index]

    return results


def get_features(data, path_save=None):
    features = list()
    for window in data:
        # window = window[:, 1:]
        max_win = np.amax(window, axis=0)
        min_win = np.amin(window, axis=0)
        mean_win = np.mean(window, axis=0)
        std_win = np.std(window, axis=0)
        mad_win = np.median(window, axis=0)
        feature = np.concatenate([max_win, min_win, mean_win, std_win, mad_win], axis=0)
        features.append(feature)
    if path_save is not None:
        df = pd.DataFrame(features)
        df.to_csv(path_save, header=False, index=False)
    return np.array(features)




import preprocess
with open('data/tay_len_xuong.txt', 'r') as f:
    data = f.read()
    # print(data)
df = preprocess.parse_data(data)

seg = segment_window(df, 5)
features = get_features(seg, 'data/features.csv')

print(features.shape)