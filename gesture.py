import numpy as np
import pandas as pd


min_window_size = 30
max_window_size = 100
threshold_mean = 0
threshold_std = 0.5


def segment_window(data, array, min_window_size, max_window_size):
    index_segment = list()
    prev_point = array[0]
    start_index_window = 0
    for i, value in enumerate(array[1:]):
        if value >= 0 > prev_point or value < 0 <= prev_point:
            if max_window_size >= i - start_index_window >= min_window_size:
                print(start_index_window, i)
                index_segment.append((start_index_window, i))
                start_index_window = i
        prev_point = value

    result = list()
    for value in index_segment:
        window = data[value[0]:value[1]].values
        result.append(window)
    return result


def get_features(data):
    features = list()
    for window in data:
        window = window[:, 1:]
        max_win = np.amax(window, axis=0)
        min_win = np.amin(window, axis=0)
        mean_win = np.mean(window, axis=0)
        std_win = np.std(window, axis=0)
        mad_win = np.median(window, axis=0)
        feature = np.concatenate([max_win, min_win, mean_win, std_win, mad_win], axis=0)
        features.append(feature)
    return np.array(features)


def get_gesture(feature_window, field):
    mapping = {
        'ax': [15, 21, 'left', 'right'],
        'ay': [16, 22, 'left', 'right'],
        'az': [17, 23, 'up', 'down']
    }
    print(feature_window[15:24], field)
    if feature_window[mapping[field][1]] < threshold_std:
        return None

    if feature_window[mapping[field][0]] > threshold_mean:
        return mapping[field][2]
    else:
        return mapping[field][3]


def get_gestures(data):
    data_segmented_x = segment_window(data, data[['ax']].values,
                                      min_window_size=min_window_size, max_window_size=max_window_size)
    data_segmented_y = segment_window(data, data[['ay']].values,
                                      min_window_size=min_window_size, max_window_size=max_window_size)
    data_segmented_z = segment_window(data, data[['az']].values,
                                      min_window_size=min_window_size, max_window_size=max_window_size)

    features_x = get_features(data_segmented_x)
    features_y = get_features(data_segmented_y)
    features_z = get_features(data_segmented_z)

    predictions_x = list()
    predictions_y = list()
    predictions_z = list()

    for feature in features_x:
        predict = get_gesture(feature, 'ax')
        if predict is not None:
            predictions_x.append(predict)
    for feature in features_y:
        predict = get_gesture(feature, 'ay')
        if predict is not None:
            predictions_y.append(predict)
    for feature in features_z:
        predict = get_gesture(feature, 'az')
        if predict is not None:
            predictions_z.append(predict)

    print(predictions_x, predictions_y, predictions_z)
    if len(predictions_z) > 0:
        return predictions_z[0]
    elif len(predictions_y) > 0:
        return predictions_y[0]
    elif len(predictions_x) > 0:
        return predictions_x[0]
    # return predictions_x, predictions_y, predictions_z


# import preprocess
# with open('data/tay_len_xuong.txt', 'r') as f:
#     data = f.read()
#     # print(data)
# df = preprocess.parse_data(data)
# print(df.shape)
# pred = get_gestures(df)