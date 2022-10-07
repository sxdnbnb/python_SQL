# _*_coding : utf-8 _*_
# @Time : 2022/9/29 20:28
# @Author : SunShine
# @File : pandas_books
# @Project : python_SQL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'
plt.rcParams['font.size'] = 20

#设置图像大小
fig= plt.figure(figsize=(20,28),dpi=80)

pd.set_option("display.max_columns", None)    # 不省略的显示

file_path="./datasourse/10000本书/books.csv"
df=pd.read_csv(file_path)
print(df.info())
# print(df.head(1))
# 去除original_publication_year中nan的行
# 不同年份书的数量
# 不同年份书的平均评分情况
data1=df[pd.notnull(df["original_publication_year"])]
data=data1.groupby(by="original_publication_year")["title"].count()
# print(data)
# _x=data.index
# _y=data.values
# plt.bar(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x,rotation=0)
# plt.show()
data2=data1.groupby(by="original_publication_year")["average_rating"].mean()
print(data2)
_x=data2.index
_y=data2.values
plt.plot(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)
plt.show()