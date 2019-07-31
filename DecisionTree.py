# -*- coding: utf-8 -*-

"""
@author: AndrewYq

@Email: hfyqstar@163.com

@Date：2019/07/31
"""

from IPython.display import Image
import pandas as pd
import pydotplus
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets.california_housing import fetch_california_housing
from sklearn import tree


# 加载sklearn的dataset
housing = fetch_california_housing()

# 打印数据的描述和数据维度
print(housing.DESCR)
print(housing.data.shape)

# 实例化tree模型，并设定树的深度为2
dtr = tree.DecisionTreeRegressor(max_depth=2)

# 训练决策树模型
dtr.fit(housing.data[:, [6, 7]], housing.target)

# 打印树模型的信息
print(dtr)

# 下载安装graphviz，用于决策树的可视化展示
dot_data = \
    tree.export_graphviz(
        dtr,
        out_file=None,
        feature_names=housing.feature_names[6:8],
        filled=True,
        impurity=False,
        rounded=True
    )

# 下载安装pydotplus，pip install pydotplus
graph = pydotplus.graph_from_dot_data(dot_data)
graph.get_nodes()[7].set_fillcolor("#FFF2DD")

# 将生成的决策树图形写入本地的png文件
graph.write_png("test.png")

# 将决策树的可视化展示在console中
Image(graph.create_png())

# 划分数据的训练集和测试集，并设置random_state为定值
data_train, data_test, target_train, target_test = \
    train_test_split(housing.data, housing.target, test_size=0.1, random_state=42)

# 实例化决策树模型
dtr = tree.DecisionTreeRegressor(random_state=42)

# 训练决策树模型
dtr.fit(data_train, target_train)

# 决策树模型测试
print(dtr.score(data_test, target_test))

# 实例化随机森林回归模型，并设置random_state为定值
rfr = RandomForestRegressor(random_state=42)

# 训练随机森林回归模型
rfr.fit(data_train, target_train)

# 测试随机森林回归模型
print(rfr.score(data_test, target_test))

# 交叉验证
# gridsearch的参数
tree_param_grid = {'min_samples_split': list((3, 6, 9)), 'n_estimators': list((10, 50, 100))}
# 实例化GridSearchCV
grid = GridSearchCV(RandomForestRegressor(), param_grid=tree_param_grid, cv=3)
# 训练GridSearchCV模型
grid.fit(data_train, target_train)
print(grid.grid_scores_)
print(grid.best_params_)
print(grid.best_score_)

# 根据GridSearch和CrossValidation得出最佳模型参数是min_samples_split=3，n_estimators=100，使用该参数实例化模型
rfr = RandomForestRegressor(random_state=42, min_samples_split=3, n_estimators=100)
rfr.fit(data_train, target_train)
print(rfr.score(data_test, target_test))

# 打印模型建立中最重要的特征
print(pd.Series(rfr.feature_importances_, index=housing.feature_names).sort_values(ascending=False))
