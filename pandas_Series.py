# _*_coding : utf-8 _*_
# @Time : 2022/9/23 14:51
# @Author : SunShine
# @File : pandas_可非数值
# @Project : python_SQL

import pandas as pd

# Series 带标签的一维数组
t1 = pd.Series([1, 21, 31, 23, 55])
# print(t1)
# print(type(t1))

# 自定义索引
t2 = pd.Series([1, 21, 31, 23, 55], index=list("abcde"))
# print(t2)
# print(type(t2))

# 用字典创建
temp_dict = {"name": "sss", "age": 18, "number": 10086}
t3 = pd.Series(temp_dict)
print(t3)
print(t3["age"])
print(t3[1])
print(list(t3.index))
print(t3.values)

# 读取csv中的文件
df = pd.read_csv("./datasourse/狗的名字的统计数据/dogNames2.csv")
print(df)
