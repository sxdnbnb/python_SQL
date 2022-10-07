# _*_coding : utf-8 _*_
# @Time : 2022/10/1 10:46
# @Author : SunShine
# @File : pandas_PM2.5
# @Project : python_SQL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'
plt.rcParams['font.size'] = 15
pd.set_option("display.max_columns", None)  # 不省略的显示

file_path = "./datasourse/城市空气质量数据/BeijingPM20100101_20151231.csv"
data = pd.read_csv(file_path)
print(data.info())
# print(data.head(5))

# 绘制出5个城市的PM2.5随时间的变化情况
# 将分开的时间字符串合并为一个字符串，类型为PeriodIndex
periods = pd.PeriodIndex(year=data["year"], month=data["month"], day=data["day"], hour=data["hour"], freq="H")
# print(periods)

data["datetime"] = periods  # 添加一列
# 把datetime设置为索引

data.set_index("datetime", inplace=True)

# print(data.head())
# 处理缺失数据，删除缺失数据 .dropna()
data_US = data["PM_US Post"]
data_china = data["PM_Dongsi"]

# 进行降采样,算每月的平均值
data_US = data_US.resample("7D").mean()
data_china = data_china.resample("7D").mean()
# 画图
# 设置图像大小
fig = plt.figure(figsize=(20, 28), dpi=80)
_x = data_US.index
_y = data_US.values
plt.plot(range(len(_x)), _y, label="美国")
# _x = [i.strftime("%Y-%m") for i in _x]
# plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)

_x1 = data_china.index
_y1 = data_china.values
plt.plot(range(len(_x1)), _y1, label="中国")
# _x = [i.strftime("%Y-%m") for i in _x]
plt.xticks(range(0, len(_x1), 10), list(_x1)[::10], rotation=45)

# 添加图例
plt.legend(loc="best")

plt.show()
