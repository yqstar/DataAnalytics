# -*- coding: utf-8 -*-

"""
@author: AndrewYq

@Email: hfyqstar@163.com

@Date: 2019/08/06

@Purpose: KMeans and DBSCAN Demos
"""

import sys
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.cluster import DBSCAN


# 获取当前执行的Python脚本路径, os.getcwd()
base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
# 拼接获得最后数据所在文件路径
data_path = base_path + "\\" + "data.txt"
# 加载数据
beer_data = pd.read_csv(data_path, sep=' ')
print(beer_data.head(n=5))

# Creating the Training DataSet
X = beer_data[["calories", "sodium", "alcohol", "cost"]]

# Training the KMeans model
km = KMeans(n_clusters=3).fit(X)
km2 = KMeans(n_clusters=2).fit(X)

print(km.labels_)

beer_data['cluster'] = km.labels_
beer_data['cluster2'] = km2.labels_

print(beer_data.sort_values('cluster'))


cluster_centers = km.cluster_centers_
cluster_centers2 = km2.cluster_centers_

print(beer_data.groupby("cluster").mean())


print(beer_data.groupby("cluster2").mean())

centers = beer_data.groupby("cluster").mean().reset_index()


plt.rcParams["font.size"] = 14


plt.figure()
colors = np.array(["red", "green", "blue", "yellow"])

plt.scatter(beer_data["calories"], beer_data["alcohol"], c=colors[beer_data["cluster"]])
plt.scatter(centers.calories, centers.alcohol, linewidths=3, marker='+', s=300, c='black')

plt.xlabel("calories")
plt.ylabel("alcohol")
plt.show()

scatter_matrix(beer_data[["calories", "sodium", "alcohol", "cost"]], s=100, alpha=1, c=colors[beer_data["cluster"]], figsize=(10, 6))
plt.suptitle("With 3 centroids initialized")

scatter_matrix(beer_data[["calories", "sodium", "alcohol", "cost"]], s=100, alpha=1, c=colors[beer_data["cluster2"]], figsize=(10, 6))
plt.suptitle("With 2 centroids initialized")

# Scaled data


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

km_scale = KMeans(n_clusters=3).fit(X_scaled)

beer_data["scaled_cluster"]=km_scale.labels_

print(beer_data.sort_values("scaled_cluster"))
print(beer_data.groupby("scaled_cluster").mean())

# 聚类评估，轮廓系数

score_scaled = metrics.silhouette_score(X, beer_data.scaled_cluster)
score = metrics.silhouette_score(X, beer_data.cluster)
print(score_scaled,score)

scores = []

for k in range(2,20):
    labels = KMeans(n_clusters=k).fit(X).labels_
    score = metrics.silhouette_score(X,labels)
    scores.append(score)

print(scores)

plt.plot(list(range(2,20)),scores)

plt.xlabel("Number of Clusters Initialized")
plt.ylabel("silhouette_score")

# DBSCAN clustering
db = DBSCAN(eps=10,min_samples=2).fit(X)
labels = db.labels_
beer_data["cluster_db"] = labels
beer_data.sort_values("cluster_db")
