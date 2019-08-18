feature_dict={i:label for i,lable in zip(
range(4),
('sepal length [cm]',
'sepal width [cm]',
'petal length [cm]',
'petal width [cm]',))}

import pandas as pd

df = pd.io.parsers.read_csv(
    filepath_or_buffer = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None, 
    sep=',')

df.columns = []