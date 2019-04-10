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

## Qt Designer的安装方法
https://www.2cto.com/kf/201802/720803.html
