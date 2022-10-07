# _*_coding : utf-8 _*_
# @Time : 2022/9/18 10:43
# @Author : SunShine
# @File : matplotlib_01
# @Project : python_SQL
import random
from matplotlib import pyplot as plt

#设置图像大小
fig= plt.figure(figsize=(20,28),dpi=80)

# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'

# x=range(2,26,2)
x=range(0,120)

# 生成一个具有50个20~35之间的整数
y=[random.randint(20,35) for i in range(120)]
y1=[random.randint(20,35) for i in range(120)]

# 绘图
plt.plot(x,y,label="自己")
plt.plot(x,y1,label="同座")

#设置x轴的刻度
# plt.xticks(range(2,26,5))
# plt.xticks(x[::2])
# x=list(x)[::10]   # 强制类型转换
xticks_lable=['10点{}分'.format(i) for i in range(60)]
xticks_lable+=['11点{}分'.format(i) for i in range(60)]

# 取步长，数字和字符串对应，数据的长度一样
plt.xticks(list(x)[::3],xticks_lable[::3],rotation=90)  # rotation为旋转的度数

#设置y轴的刻度
plt.yticks(range(min(y),max(y)+1))

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点每分钟的气温变化情况")

# 绘制网格
plt.grid(alpha=0.4)

# 添加图例
plt.legend(loc="upper left")


# 保存
# plt.savefig('./ti.png')
# plt.savefig('./ti.svg')   #矢量图

# 展示图
plt.show()

