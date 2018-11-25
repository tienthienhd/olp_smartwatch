import numpy as np
import json
import pandas as pd


def parse_data(raw_data):
    """
    convert from string list of data to array of data
    :param raw_data: string of list dict data :
    [{'yaw': -157.6705, 'pitch': -4.33582, 'roll': -2.451883, 'Ax': 0, 'Ay': 485, 'Az': 7381, 'timestamps': 1542884104.3810017},
    {'yaw': -157.7411, 'pitch': -4.701654, 'roll': -1.870299, 'Ax': -53, 'Ay': 630, 'Az': 7189, 'timestamps': 1542884104.3893933},
    {'yaw': -157.8128, 'pitch': -5.099143, 'roll': -1.229501, 'Ax': -92, 'Ay': 793, 'Az': 6948, 'timestamps': 1542884104.3895116},
    {'yaw': -157.888, 'pitch': -5.491229, 'roll': -0.536322, 'Ax': -101, 'Ay': 972, 'Az': 6662, 'timestamps': 1542884104.3895922},
    {'yaw': -157.9806, 'pitch': -5.876004, 'roll': 0.203376, 'Ax': -78, 'Ay': 1154, 'Az': 6383, 'timestamps': 1542884104.3896697}]
    :return: dataframe of data
    """
    raw_data = raw_data.replace('[', '')
    raw_data = raw_data.replace(']', '')
    raw_data = raw_data.replace('}, {', "};{")
    raw_data = raw_data.replace("'", '"')
    raw_data = raw_data.replace('}\n{', '};{')
    print("===================", raw_data)
    lines = raw_data.split(';')

    data = dict({'timestamps': [],
                 'yaw': [],
                 'pitch': [],
                 'roll': [],
                 'ax': [],
                 'ay': [],
                 'az': []})
    for line in lines:
        try:
            line_json = json.loads(line)
            print(line_json)
        except Exception as e:
            print(e)
            continue

        data['timestamps'].append(line_json['timestamps'])
        data['yaw'].append(line_json['yaw'])
        data['pitch'].append(line_json['pitch'])
        data['roll'].append(line_json['roll'])
        data['ax'].append(line_json['Ax'] / 1638)
        data['ay'].append(line_json['Ay'] / 1638)
        data['az'].append(line_json['Az'] / 1638)

    results = pd.DataFrame(data)
    return results


# data = "[{'yaw': -157.6705, 'pitch': -4.33582, 'roll': -2.451883, 'Ax': 0, 'Ay': 485, 'Az': 7381, 'timestamps': 1542884104.3810017}, " \
#        "{'yaw': -157.7411, 'pitch': -4.701654, 'roll': -1.870299, 'Ax': -53, 'Ay': 630, 'Az': 7189, 'timestamps': 1542884104.3893933}, " \
#        "{'yaw': -157.8128, 'pitch': -5.099143, 'roll': -1.229501, 'Ax': -92, 'Ay': 793, 'Az': 6948, 'timestamps': 1542884104.3895116}, " \
#        "{'yaw': -157.888, 'pitch': -5.491229, 'roll': -0.536322, 'Ax': -101, 'Ay': 972, 'Az': 6662, 'timestamps': 1542884104.3895922}, " \
#        "{'yaw': -157.9806, 'pitch': -5.876004, 'roll': 0.203376, 'Ax': -78, 'Ay': 1154, 'Az': 6383, 'timestamps': 1542884104.3896697}]"
#
# df = parse_data(data)
# print(df.head())