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




## 数组变形

## 数组拼接和分裂
