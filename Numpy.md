# Numpy数组的基本操作

## 数组属性

``` python

ndarray.ndim：数组维度

ndarray.shape：数组每个维度大小

ndarray.size：数组元素总数

ndarray.dtype：数组数据类型

ndarray.itemsize：数组元素字节大小

ndarray.nbytes：数组总字节大小

nbytes = size * itemsize

Numpy数组是固定类型，不同于Python列表的可变类型

```

## 数组索引

```
ndarray[索引元组]
索引符号为“，”
其中：
索引元组的维度：ndarray.ndim
索引元组的元素范围值：正向索引[0,ndarray.shape)，逆向索引[-ndarray.shape,-1]

```


## 数组切片(slice)

```
ndarray[start:stop:step]

切片符号为":"

其中:

start默认为0
stop默认为维度大小
step默认为1

```

注：Numpy数组切片：值的视图，切片视图的操作会影响数组，可通过copy()方法，获取数组的副本。
   Python列表切片：值的副本，切片副本的操作不会影响列表。




## 数组变形


``` python
ndarray.reshape()
c1=np.array([[1,2,3]]),行向量
c2=np.array([1,2,3])，列向量

```
## 数组拼接和分裂
