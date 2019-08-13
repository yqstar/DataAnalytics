# 支持向量机

要解决的问题：什么样的决策边界才是最好的？(找一个最胖的决策边界)

特征数据本身如果就很难分，怎么办呢？（核函数）

计算复杂度怎么样？能实际应用吗？

目标：基于上述问题对SVM进行推导。

决策边界：选出来离雷区最远的（雷区就是边界上的点，要Large Margin）

距离计算：

$$Distance(x,w,b)=\frac{1}{\left \| \omega  \right \|}\left \| \omega^{T} + b \right \|$$

数据标签定义


数据集：(X1,Y1),(X2,Y2)...(Xn,Yn)

Y为样本的类别：当X为正例时候Y=+1，当X为负例时Y=-1


决策方程：$y(x) = \omega^{T} \phi(x) + b$

其中$\phi(x)$是对数据进行了变换。

$y(x_{i})>0 <=> y_{i} = +1$
$y(x_{i})<0 <=> y_{i} = -1$
故：

$y_{i}*y(x_{i})>0$

优化的目标：

通俗解释：
找到一条直线（w和b）,使得离该线最近的点（雷区），越远越好。

将点到直线的距离化简得：

$$\frac{y_{i}(\omega^{T} \phi(x_{i}) + b)}{\| \omega \|}$$

目标函数：

放缩变换：对于决策方程（w,b）可以通过放缩使得其结果置|Y|>=1.

进而：

$y_{i}(\omega^{T} \phi(x_{i}) + b) \geq 1$

(之前我们认为恒大于0，现在严格了些)

优化目标：

$\underset{w,b}{arg max}\{\frac{1}{\|w\|}\underset{i}{min}[y_{i}\cdot (\omega^{T} \cdot \phi(x_{i}) + b)] \}$

由于$y_{i}(\omega^{T} \phi(x_{i}) + b) \geq 1$，只需要考虑:$\underset{w,b}{arg max} \frac{1}{\|w\|}$

目标函数搞定。

目标函数

当前目标：

$max_{w,b}\frac{1}{\|w\|}$

约束条件：

$y_{i}(\omega^{T} \phi(x_{i}) + b) \geq 1$

常规套路：

将求解极大值问题转换成极小值问题：

$min_{w,b}\frac{1}{2}{w}^2$

如何求解：

应用拉格朗日乘子法求解

拉格朗日乘子法：

带约束得优化问题，参考百度百科。

我们得式子经拉格朗日乘子法转换：

$L(\omega,b,\alpha)=\frac{1}{2}{\| \omega \|}^2-\sum_{i=1}^{n} \alpha_{i}(y_{i}(\omega^{T} \phi(x_{i}) + b)-1)$

约束条件不要忘。

SVM求解

分别对w和b求偏导，分别得到两个条件（由于对偶性质）

$\underset{w,b}{min}\ \underset{\alpha}{max} \ L(w,b,a) -> \underset{\alpha}{max} \ \underset{w,b}{min} \ L(w,b,a)$

对w求导：$\frac{\nabla L}{\nabla w}=0 => w = \sum_{i=1}^{n} \alpha_{i} y_{i} \phi(x_{n})$

对b求导：

$\frac{\nabla L}{\nabla b}=0 => 0 = \sum_{i=1}^{n} \alpha_{i} y_{i}$


支持向量：真正发挥作用的数据点，a值不为0的数据点。

soft-margin:

软间隔：有时候数据中有一些噪音点，如果考虑他们我们的线就不太好了。

之前的方法要求把两类点完全分开，这个要求有点过于严格，我们放松一点。

为了解决该问题，引入松弛因子：

$y_{i}(\omega \cdot x_{i} + b)>=1-\epsilon_{i}$

新的目标函数：

$min \frac{1}{2} {\| w \|}^2 + C\sum_{i=1}^{n} \epsilon_{i}$

当C趋近于很大时，意味着分类严格不能有错误。
当C趋近于很小时，意味着分类可以有很大的容忍。

低维不可分问题

找到一种变换的方法，也就是$\phi(x)$,低维不可分的问题，变成高维可分的问题，进行核变换。

高斯核函数：

$K(X,Y)=exp{-\frac{{\| X-Y \|}^2}{2{\sigma}^2}}$

