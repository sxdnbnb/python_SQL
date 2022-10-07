# _*_coding : utf-8 _*_
# @Time : 2022/9/26 20:23
# @Author : SunShine
# @File : pandas_分组和聚合
# @Project : python_SQL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'
plt.rcParams['font.size'] = 20

# 设置图像大小
fig = plt.figure(figsize=(20, 28), dpi=80)

pd.set_option("display.max_columns", None)  # 不省略的显示
file_path = "./datasourse/星巴克/directory.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(1))
# 调用分组方法,根据国家分组
grouped = df.groupby(by="Country")
# print(grouped)
# DataFrameGroupBy类型,元组里面第一个元素是国家名，第二个元素是一个DataFrame
# 可以进行遍历,
# for i,j in grouped:
#     print(i)    # 元组里面第一个元素是国家名
#     print(type(i))
#     print("__"*100)
#     print(j)   # 第二个元素是一个DataFrame
#     print(type(j))
#     print("*"*100)
# print(df[df["Country"]=="US"])
# 调用聚合方法,将每个组的数据根据标签聚合
# print(grouped.count())
country_count = grouped["Brand"].count()  # series类型
# print(type(country_count))
# 统计中国和美国店铺的数量
# print(country_count)   # series类型
# print(country_count["US"])
# print(country_count["CN"])

# 统计中国每个省份店铺的数量
china_data = df[df["Country"] == "CN"]
grouped = china_data.groupby(by="State/Province")["Brand"].count()
# print(grouped)

# 数据按照多个条件分组,返回类型为series
grouped = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
# grouped=df.groupby(by=["Country","State/Province"])["Brand"].count()
# print(grouped)    # 两个索引，类型为series

# 数据按照多个条件分组,返回类型为DateFrame
grouped = df[["Brand", ]].groupby(by=[df["Country"], df["State/Province"]]).count()
# grouped=df.groupby(by=[df["Country"],df["State/Province"]])[["Brand",]].count()
# print(grouped)    # 两个索引，类型为DateFrame

# 使用matplotlib呈现出店铺总数排名前10的国家
# 使用matplotlib呈现出每个中国每个城市的店铺数量
data1 = country_count.sort_values(ascending=False)[:10]

_x = data1.index
_y = data1.values
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=0)
plt.show()

grouped1 = china_data.groupby(by="City")["Brand"].count().sort_values(ascending=False)[:10]
_x = grouped1.index
_y = grouped1.values
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=0)
plt.show()
