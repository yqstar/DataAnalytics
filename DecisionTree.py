import matplotlib
# matplotlib.interactive(b)
import matplotlib.pyplot as plt

import pandas as pd

from sklearn.datasets.california_housing import fetch_california_housing

housing = fetch_california_housing()

print(housing.DESCR)

print(housing.data.shape)

from sklearn import tree

dtr = tree.DecisionTreeRegressor(max_depth=2)

dtr.fit(housing.data[:, [6, 7]], housing.target)

print(dtr)

# 下载安装graphviz
dot_data=\
    tree.export_graphviz(
        dtr,
        out_file=None,
        feature_names=housing.feature_names[6:8],
        filled=True,
        impurity=False,
        rounded=True
    )
# 下载安装pydotplus
import pydotplus

graph = pydotplus.graph_from_dot_data(dot_data)

graph.get_nodes()[7].set_fillcolor("#FFF2DD")

from IPython.display import Image

Image(graph.create_png())

print(Image(graph.create_png()))

graph.write_png("test.png")

from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = \
    train_test_split(housing.data,housing.target,test_size=0.1,random_state=42)
dtr = tree.DecisionTreeRegressor(random_state=42)
dtr.fit(data_train,target_train)

print(dtr.score(data_test, target_test))

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(random_state=42)
rfr.fit(data_train, target_train)
rfr.score(data_test, target_test)

from sklearn.grid_search import GridSearchCV
tree_param_grid = {'min_samples_split': list((3, 6, 9)), 'n_estimators': list((10, 50, 100))}
grid = GridSearchCV(RandomForestRegressor(), param_grid=tree_param_grid, cv=5)
grid.fit(data_train, target_train)
print(grid.grid_scores_)
print(grid.best_params_)
print(grid.best_score_)

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(random_state=42,min_samples_split=3,n_estimators=100)
rfr.fit(data_train, target_train)
rfr.score(data_test, target_test)

pd.Series(rfr.feature_importances_,index=housing.feature_names).sort_values(ascending=False)
