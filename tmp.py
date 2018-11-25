from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_train_x = pd.read_csv('../code/data/dataset_uci/final_X_train.txt', header=None)
df_train_y = pd.read_csv('../code/data/dataset_uci/final_y_train.txt', header=None)
# print(df_train_x.shape)
df_train = pd.concat([df_train_x, df_train_y], axis=1)
df_train.columns = range(0, 562)
# print(df_train.shape)
df_train = df_train.sort_values(561)
index = df_train[561].diff()[df_train[561].diff() != 0].index.values
print(index)
# print(df_train_y)
pca = PCA(n_components=2)
data = pca.fit_transform(df_train.loc[:,:561].values)
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
print(data.shape)
print(df_train.iloc[[0, 1779, 2537, 2758, 3355, 3112], 561])

for i, val in enumerate(index[1:]):
    plt.scatter(data[index[i]:val, 0], data[index[i]: val, 1], c=color[i], label=df_train.iloc[val, 561])

plt.legend()
plt.show()