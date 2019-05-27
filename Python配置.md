# Python配置

## 目录
* [Fbprophet配置](#Fbprophet配置)
* [Pypi镜像配置](#Pypi镜像配置)
    * Pypi镜像使用
    * 常见的Pypi镜像源
* [JupyterNotebook配置](#JupyterNotebook配置)
    * 自动补全配置
* [Spyder启动报错](#Spyder启动报错)
    * No module named 'PyQt5.QtWebEngineWidgets' 报错
    
* [PyTorch安装使用](# )
    * import torch 报错



## Fbprophet配置

## PyPi镜像配置

### PyPi镜像使用

* 临时使用

``` Python
pip install -i mirror-url some-package
```

注意：`mirror-url`为镜像的链接，其中：`simple` 不能少, 是 `https` 而不是 `http`。

* 设为默认
``` Python
pip install pip -U
pip config set global.index-url mirror-url
```

### 常见PyPi源

|Mirror|url|
|------|---|
|阿里云|`http://mirrors.aliyun.com/pypi/simple/`|
|中国科技大学|`https://pypi.mirrors.ustc.edu.cn/simple/`|
|douban|`http://pypi.douban.com/simple`|
|Python官方|`https://pypi.python.org/simple`|
|v2ex|`http://pypi.v2ex.com/simple`|
|中国科学院|`http://pypi.mirrors.opencas.cn/simple/`|
|清华大学|`https://pypi.tuna.tsinghua.edu.cn/simple/`|

## JupyterNotebook配置

### 自动补全配置

首先安装 **nbextensions**
``` Python
pip install jupyter_contrib_nbextensions
```
``` Python
jupyter contrib nbextension install --
```
## Spyder启动报错

### No module named 'PyQt5.QtWebEngineWidgets' 报错

PyQt5对于v5.11及更高版本，64位Windows轮盘不包含WebEngine模块,Spyder会调用该模块，故会报错。

解决方法：

```
pip install pyqt5==5.10.1
```

## 使用pd.read_csv()读csv文件时，出现如下错误：

UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0xd0 in position 0: invalid continuation byte

出现原因：文件不是 UTF8 编码的，而系统默认采用 UTF8 解码。解决方法是改为对应的解码方式。

原文：https://blog.csdn.net/moledyzhang/article/details/78978312 


## Qt Designer的安装方法
https://www.2cto.com/kf/201802/720803.html

# import torch出现如下报错：

No module named 'numpy.core._multiarray_umath'

出现原因：可能时numpy的版本过低，需要升级numpy版本。

解决方案：`pip install --upgrade numpy`

原文：https://www.cnblogs.com/Terrypython/p/10467859.html
