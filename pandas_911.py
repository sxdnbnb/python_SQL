# _*_coding : utf-8 _*_
# @Time : 2022/9/30 15:26
# @Author : SunShine
# @File : pandas_911
# @Project : python_SQL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'
plt.rcParams['font.size'] = 15
pd.set_option("display.max_columns", None)  # 不省略的显示

file_path = "./datasourse/911/911.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(5))
data_list = df["title"].str.split(":", expand=True)[0].tolist()  # 一列分解成多列,变为DataFrame
data_list1 = df["title"].str.split(":").tolist()
cate_list = set(data_list)
# print(data_list1)

# 统计出这些数据中不同类型的紧急情况的次数
# 构造一个全为0的数组
row = df.shape[0]  # 行数为电影个数
column = len(cate_list)  # 列数为电影类别数
zeros_df = pd.DataFrame(np.zeros((row, column)), columns=cate_list)
# print(zeros_df)
# for i in range(row):
#     zeros_df.loc[i,data_list1[i][0]]=1
# print(zeros_df.head(3))
# count=zeros_df.sum(axis=0)   #得到一个series类型的数据（一维的）
# print(count)

# 或者
df["cate"] = pd.DataFrame(data_list)  # 新加一列【紧急情况的类型】
group = df.groupby(by="cate")
# print(group["title"].count())
# print(df.head(2))

# 统计出911数据中不同月份电话次数的变化情况
df["timeStamp"] = pd.to_datetime(df["timeStamp"], format="")  # 把时间字符串转化为时间序列
df.set_index("timeStamp", inplace=True)     # 把timeStamp设置为索引

count_by_month = df.resample("M")["title"].count()

# 设置图像大小
fig = plt.figure(figsize=(20, 28), dpi=80)
# print(count_by_month.head())
_x = count_by_month.index
_y = count_by_month.values
plt.plot(range(len(_x)), _y)
_x=[i.strftime("%Y-%m") for i in _x]
plt.xticks(range(len(_x)),_x,rotation=45)
# plt.show()

# 统计出不同月份不同类型紧急电话的次数的变化情况
group = df.groupby(by="cate")     # 里面有三个组，要遍历,group是个元组，每个里面有两项
# print(group["title"].count())
# 设置图像大小
fig = plt.figure(figsize=(20, 28), dpi=80)
for group_name,group_data in group:
    # print(group_name,group_data)
    # print(group_name)
    count_by_month2 = group_data.resample("M")["title"].count()
    _x = count_by_month2.index
    _y = count_by_month2.values
    plt.plot(range(len(_x)), _y,label=group_name)
    _x = [i.strftime("%Y-%m") for i in _x]
    plt.xticks(range(len(_x)), _x, rotation=45)

# 添加图例
plt.legend(loc="upper left")
plt.show()