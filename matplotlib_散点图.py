# _*_coding : utf-8 _*_
# @Time : 2022/9/18 16:49
# @Author : SunShine
# @File : matplotlib_散点图
# @Project : python_SQL

from matplotlib import pyplot as plt

#设置图像大小
fig= plt.figure(figsize=(20,28),dpi=80)

# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'

y1=[11,22,33,44,66,22,44,23,42,33,55,22,78,54,12,34,56,78]
y2=[61,82,73,94,76,92,54,33,72,43,25,12,28,74,12,84,56,78]

x=range(len(y1))

# 散点图
plt.scatter(x,y1,label="3月份")
plt.scatter(x,y2,label="10月份")

#设置x轴的刻度
xticks_lable=['10点{}分'.format(i) for i in range(len(y1))]

# 取步长，数字和字符串对应，数据的长度一样
plt.xticks(list(x)[::2],xticks_lable[::2])

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点每分钟的气温变化情况")

# 绘制网格
plt.grid(alpha=0.4)

# 添加图例
plt.legend(loc="upper left")

plt.show()