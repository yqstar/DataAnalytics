# SQL学习

SQL在线测试学习网站： [SQLZOO](https://sqlzoo.net/wiki/SQL_Tutorial) 和 [W3School-SQL](http://www.w3school.com.cn/sql/index.asp)

## 取出某字段中的最大值和最小值

数据库表test信息

+------+-------+--------------------------------------+
| id     | rev   | content                              |
+------+-------+--------------------------------------+
| id1    | 1     | ...                                  |
| id2    | 1     | ...                                  |
| id1    | 2     | ...                                  |
| id2    | 3     | ...                                  |
+------+-------+--------------------------------------+
### 取出某字段最大或者最小值的记录

取出最小值的记录

```
select id,min(rev) as test_select from test group by id
```

取出最大值的记录

```
select id,max(rev) as test_select from test group by id
```

取出最大值和最小值的记录
```
select id,min(rev) as test_select from test group by id
union
select id,max(rev) as test_select from test group by id
```

取出最大值和最小值的所有字段记录信息

```
SELECT a.id, a.rev,a.contents
FROM test a
INNER JOIN (
select id,min(rev) as test_select from test group by id
union
select id,max(rev) as test_select from test group by id
) b ON a.id = b.id and a.rev = b.rev;
```

## 使用sql语句统计重复某个字段出现重复次数

```
select mark_name ,COUNT(0) AS 重复数据 FROM livemark GROUP BY mark_name HAVING COUNT(mark_name)>1
```

## SQL数据准备

在`MySQL`新建数据库`join_test`，在`join_test`中新建两个数据表，分别是`Table_A`和`Table_B`，并插入两条数据。具体操作如下：

``` sql
-- 语法：create database database_name;
-- 作用：新建数据库
create database join_test;
use join_test;

-- 语法：create table table_name (field_name1 data_type1,field_name2 data_type2,...);
-- 作用：新建数据表
create table Table_A (PK int,Value varchar(255));
create table Table_B(PK int,Value varchar(255));

-- 语法：insert into table_name values(field_value1,field_value2,...);
-- 作用：插入数据
insert into Table_A values(1,'both ab');
insert into Table_A values(2,'only a');
insert into Table_B values(1,'both ab');
insert into Table_B values(3,'only b');
```

``` sql
-- 语法：select field_name1 (as) field_name1_alias, field_name2 (as) field_name2_alias from table_name (as) table_name_alias;
-- 作用：查询表中的某几个字段的数据记录，并对表名和字段名设置别名，其中别名（Alias）的关键字为as,一般可以省略。
select A.PK as A_PK, A.Value as A_Value from Table_A as A;
select B.PK B_PK, B.Value B_Value from Table_B B;

-- 查询结果及具体内容
+------+---------+
| A_PK | A_Value |
+------+---------+
|    1 | both ab |
|    2 | only a  |
+------+---------+
2 rows in set (0.00 sec)

+------+---------+
| B_PK | B_Value |
+------+---------+
|    1 | both ab |
|    3 | only b  |
+------+---------+
2 rows in set (0.00 sec)
```

## SQL中JOIN用法概述

SQL中JOIN用于根据两个或多个表中的列之间的关系，从这些表中查询数据。具体包括：`Inner Join`, `Full Out Join`, `Cross Join`, `Left Join`, `Right Join`等用法。具体区别如下：

`Cross Join`：列出两边所有组合，也称为笛卡尔集 A×B。

`Inner Join`：筛选两边都有的记录。

`Left Join`：以左边的表为主表，列出主表所有记录，匹配能匹配的，不能匹配的用 NULL列出。

`Right Join`：以右边的表为主表，列出主表所有记录，匹配能匹配的，不匹配的用NULL列出。

`Full Out Join`：两边都筛选出来，匹配能匹配的，不能匹配的用NULL列出。

## 常见的JOIN操作

* CROSS JOIN
  CROSS JOIN 列出两边所有组合，也称为笛卡尔集 A×B。查询示例如下。
  
  ``` sql
  -- 查询语句
  SELECT A.PK AS A_PK, B.PK AS B_PK, A.Value AS A_Value, B.Value AS B_Value
  FROM Table_A A CROSS JOIN Table_B B;
  
  -- 查询结果
  +------+------+---------+---------+
  | A_PK | B_PK | A_Value | B_Value |
  +------+------+---------+---------+
  |    1 |    1 | both ab | both ab |
  |    2 |    1 | only a  | both ab |
  |    1 |    3 | both ab | only b  |
  |    2 |    3 | only a  | only b  |
  +------+------+---------+---------+
  4 rows in set (0.08 sec)
  ```



* INNER JOIN

  INNER JOIN 一般被译作内连接。内连接查询能将左表（表 A）和右表（表 B）中能关联起来的数据连接后返回。查询示例如下。
   
  ``` sql
  -- 查询语句
  SELECT A.PK AS A_PK, B.PK AS B_PK, A.Value AS A_Value, B.Value AS B_Value
  FROM Table_A A INNER JOIN Table_B B
  ON A.PK = B.PK;
  
  -- 查询结果
  +------+------+---------+---------+
  | A_PK | B_PK | A_Value | B_Value |
  +------+------+---------+---------+
  |    1 |    1 | both ab | both ab |
  +------+------+---------+---------+
  1 row in set (0.07 sec)
  ```
 
 * LEFT JOIN
 
   LEFT JOIN 一般被译作左连接，也写作 LEFT OUTER JOIN。左连接查询会返回左表（表 A）中所有记录，不管右表（表 B）中有没有关联的数据。在右表中找到的关联数据列也会被一起返回。
   
 ```sql
 -- 查询语句
 SELECT A.PK AS A_PK, B.PK AS B_PK, A.Value AS A_Value, B.Value AS B_Value FROM Table_A A LEFT JOIN Table_B B ON A.PK = B.PK;

 -- 查询结果
 +------+------+---------+---------+
 | A_PK | B_PK | A_Value | B_Value |
 +------+------+---------+---------+
 |    1 |    1 | both ab | both ab |
 |    2 | NULL | only a  | NULL    |
 +------+------+---------+---------+
 2 rows in set (0.02 sec)
 ```
 
* RIGHT JOIN

  RIGHT JOIN 一般被译作右连接，也写作 RIGHT OUTER JOIN。右连接查询会返回右表（表 B）中所有记录，不管左表（表 A）中有没有关联的数据。在左表中找到的关联数据列也会被一起返回。
  
``` sql
-- 查询语句
SELECT A.PK AS A_PK, B.PK AS B_PK, A.Value AS A_Value, B.Value AS B_Value FROM Table_A A RIGHT JOIN Table_B B ON A.PK = B.PK;

-- 查询结果
+------+------+---------+---------+
| A_PK | B_PK | A_Value | B_Value |
+------+------+---------+---------+
|    1 |    1 | both ab | both ab |
| NULL |    3 | NULL    | only b  |
+------+------+---------+---------+
2 rows in set (0.00 sec)
```

* FULL OUTER JOIN
  FULL OUTER JOIN 一般被译作外连接、全连接，实际查询语句中可以写作 FULL OUTER JOIN 或 FULL JOIN。外连接查询能返回左右表里的所有记录，其中左右表里能关联起来的记录被连接后返回。（注：MySQL不支持该用法）
  
 ``` sql
 -- 查询语句
SELECT A.PK AS A_PK, B.PK AS B_PK, A.Value AS A_Value, B.Value AS B_Value FROM Table_A A FULL OUTER JOIN Table_B B ON A.PK = B.PK;
 
 -- 查询结果
+------+---------+------+---------+
| PK   | Value   | PK   | Value   |
+------+---------+------+---------+
|    1 | both ab |    1 | both ba |
|    2 | only a  | NULL | NULL    |
| NULL | NULL    |    3 | only b  |
+------+---------+------+---------+
3 rows in set (0.00 sec)
 ```
 
 MySQL不支持该方法，故用其他语法模拟：
 
 ```
 -- MySQL查询
 SELECT * FROM Table_A LEFT JOIN Table_B ON Table_A.PK = Table_B.PK UNION ALL SELECT * FROM Table_A RIGHT JOIN Table_B ON Table_A.PK = Table_B.PK WHERE Table_A.PK IS NULL;
 
 -- MySQL结果
 +------+---------+------+---------+
| PK   | Value   | PK   | Value   |
+------+---------+------+---------+
|    1 | both ab |    1 | both ab |
|    2 | only a  | NULL | NULL    |
| NULL | NULL    |    3 | only b  |
+------+---------+------+---------+
3 rows in set (0.16 sec)
 
 ```
## 参考
* https://blog.csdn.net/moakun/article/details/80429267
* https://blog.csdn.net/ys_code/article/details/79497294
* https://blog.csdn.net/ys_code/article/details/79497294
* https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins

![SQL_JOIN图列](https://img-blog.csdnimg.cn/20181107162131341.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM4MDYzMTcy,size_16,color_FFFFFF,t_70)

![SQL_JOIN_1](https://img-blog.csdn.net/20170426144430691?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZnJ5Y24=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![SQL_JOIN_2](https://img-blog.csdn.net/20170426144540551?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZnJ5Y24=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
