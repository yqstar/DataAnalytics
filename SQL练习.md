# SQL学习

SQL练习网站：[SQLZOO](https://sqlzoo.net/wiki/SQL_Tutorial)

## SQL JOIN练习

SQL join 用于根据两个或多个表中的列之间的关系，从这些表中查询数据。

![SQL_JOIN图列](https://img-blog.csdnimg.cn/20181107162131341.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM4MDYzMTcy,size_16,color_FFFFFF,t_70)

![SQL_JOIN_1](https://img-blog.csdn.net/20170426144430691?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZnJ5Y24=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![SQL_JOIN_2](https://img-blog.csdn.net/20170426144540551?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZnJ5Y24=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

参考博客：[博客1](https://blog.csdn.net/ys_code/article/details/79497294)、[博客1](https://blog.csdn.net/frycn/article/details/70800402)

主要来介绍下Inner Join , Full Out Join , Cross Join , Left Join , Right Join的区别。

Inner Join：筛选两边都有的记录 
Full Out Join：两边都筛选出来，匹配能匹配的，不能匹配的用NULL列出 
Cross Join：列出两边所有组合，也称为笛卡尔集 A×B 
Left Join:以左边的表为主表，列出主表所有记录，匹配能匹配的，不能匹配的用 NULL列出 
Right Join：以右边的表为主表，列出主表所有记录，匹配能匹配的，不匹配的用NULL列出


## 常见的JOIN操作

``` sql
-- 语法：create database database_name；作用：新建数据库
create database join_test;
use join_test;

create table Table_A (PK int,Value varchar(255));
insert into Table_A values(1,'both ab');
insert into Table_A values(2,'only a');

create table Table_B(PK int,Value varchar(255));
insert into Table_B values(1,'both ab');
insert into Table_B values(3,'only b');
```

* INNER JOIN

INNER JOIN 一般被译作内连接。内连接查询能将左表（表 A）和右表（表 B）中能关联起来的数据连接后返回。

  * 查询示例
  ``` sql
  SELECT A.PK AS A_PK, B.PK AS B_PK, A.Value AS A_Value, B.Value AS B_Value
  FROM Table_A A INNER JOIN Table_B B
  ON A.PK = B.PK;
  ```
  * 查询结果
  ```
    +------+------+---------+---------+
    | A_PK | B_PK | A_Value | B_Value |
    +------+------+---------+---------+
    |    1 |    1 | both ab | both ab |
    +------+------+---------+---------+
    1 row in set (0.07 sec)
  ```
   


## 更多的JOIN用法



## 参考
https://blog.csdn.net/moakun/article/details/80429267
