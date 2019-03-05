# Python配置

## 目录
* [Fbprophet配置](#Fbprophet配置)
* [Pypi镜像配置](#Pypi镜像配置)
    * Pypi镜像使用
    * 常见的Pypi镜像源
* [JupyterNotebook配置](#JupyterNotebook配置)
    * 自动补全配置


## Fbprophet配置

## Pypi镜像配置

### Pypi镜像使用

* 临时使用

``` Python
pip install -i mirror-url some-package
```

注意：`mirror-url`为镜像的链接，其中： `simple` 不能少, 是 `https` 而不是 `http`。

* 设为默认
``` Python
pip install pip -U
pip config set global.index-url mirror-url
```

### 常见的Pypi镜像源

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
jupyter contrib nbextension install --user
```

然后安装 nbextensions_configurator
``` Python
pip install jupyter_nbextensions_configurator
```
``` Python
jupyter nbextensions_configurator enable --user
```

最后重启jupyter noebook，在弹出的主页面里，能看到增加了一个Nbextensions标签页，在这个页面里，勾选Hinterland即启用了代码自动补全。 
