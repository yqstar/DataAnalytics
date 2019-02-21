# Jupyter Notebook配置

## 自动补全配置

首先安装 **nbextensions**
```
pip install jupyter_contrib_nbextensions
```
```
jupyter contrib nbextension install --user
```

然后安装 nbextensions_configurator
```
pip install jupyter_nbextensions_configurator
```
```
jupyter nbextensions_configurator enable --user
```

最后重启jupyter noebook，在弹出的主页面里，能看到增加了一个Nbextensions标签页，在这个页面里，勾选Hinterland即启用了代码自动补全。 
