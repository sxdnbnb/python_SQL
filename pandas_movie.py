# _*_coding : utf-8 _*_
# @Time : 2022/9/23 20:53
# @Author : SunShine
# @File : pandas_movie
# @Project : python_SQL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path="./datasourse/100电影/IMDB-Movie-Data.csv"
df=pd.read_csv(file_path)
# print(df.info())
# print(df.head(1))
# print(df["Actors"])

# 获取电影的平均评分
print(df["Rating"].mean())

# 导演的人数
# print(df["Director"].tolist())  #转换成列表
# print(set(df["Director"].tolist()))  # 用集合去重
print(len(set(df["Director"].tolist())))
# 或者
print(len(df["Director"].unique()))

# 演员的人数
temp_actor=df["Actors"].str.split(",").tolist()  #分割之后列表里含列表
# print(temp_actor)
actors_list=[i for j in temp_actor for i in j]  # 转换成一个列表
# 或者用flatten()，展成一维的
# actors_list=np.array(actors_list).flatten()
# print(actors_list)
print(len(set(actors_list)))

# # (1) Rating，Runtime分布情况
# # 先取值
# runtime_data=df["Runtime (Minutes)"].values
# # print(runtime_data)
# max_runtime_data=runtime_data.max()
# min_runtime_data=runtime_data.min()
#
# # 组距
# d=5
# #组数
# num_bin=(max_runtime_data-min_runtime_data)//d
# print(max_runtime_data-min_runtime_data)
#
# 绘图
# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'
plt.rcParams['font.size'] = 15

#设置图像大小
fig= plt.figure(figsize=(20,28),dpi=80)

# # 绘制直方图
# plt.hist(runtime_data,num_bin)
#
# #设置x轴的刻度
# plt.xticks(range(min_runtime_data,max_runtime_data+d,d))
#
# # 绘制网格
# plt.grid(alpha=0.4)
#
# plt.show()

# # (2) Rating，Runtime分布情况
# # 先取值
# rating_data=df["Rating"].values
# # print(rating_data)
# max_rating_data=rating_data.max()
# min_rating_data=rating_data.min()
# # print(max_rating_data)
# # print(min_rating_data)
# # 组距
# d=0.5
# #组数
# num_bin1=int((max_rating_data-min_rating_data)//d)
# # print(max_rating_data-min_rating_data)
#
# # 绘图
#
# #设置图像大小
# fig= plt.figure(figsize=(20,28),dpi=80)
#
# # 绘制直方图
# plt.hist(rating_data,num_bin1)
#
# #设置x轴的刻度
# _x=np.arange(min_rating_data,max_rating_data+d,0.5)
# # _x=np.linspace(min_rating_data,max_rating_data,num_bin1)
# # print(_x)
# plt.xticks(_x)
#
# # 绘制网格
# plt.grid(alpha=0.4)
# #
# plt.show()

# 统计电影分类(genre)的情况
# 思路：将电影类别作为列，电影为行，构造一个全0矩阵，再将电影对应类别的置为1，最后再将把每一列求和

temp_list=df["Genre"].str.split(",").tolist() #分割之后列表里含列表
# print(temp_list)
genre_list=list(set(i for j in temp_list for i in j)) # 变成一个列表并去重
print(genre_list)
# print(df["Genre"].unique())      # 不是一个效果

# 构造一个全为0的数组
row=df.shape[0]     #行数为电影个数
column=len(genre_list)   #列数为电影类别数
zeros_df=pd.DataFrame(np.zeros((row,column)),columns=genre_list)
# print(zeros_df)
for i in range(row):
    zeros_df.loc[i,temp_list[i]]=1
# print(zeros_df.head(3))
genre_count=zeros_df.sum(axis=0)   #得到一个series类型的数据（一维的）
# print(genre_count)
# 排序
genre_count=genre_count.sort_values(ascending=False)
# print(genre_count)
plt.bar(range(column),genre_count.values)

#设置x轴的刻度
xticks_lable=genre_count.index
plt.xticks(range(column),xticks_lable,rotation=20)

plt.show()




