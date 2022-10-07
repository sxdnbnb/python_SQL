# _*_coding : utf-8 _*_
# @Time : 2022/9/18 17:26
# @Author : SunShine
# @File : matplotlib_条形图
# @Project : python_SQL
from matplotlib import pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = 'DengXian'
plt.rcParams['font.size'] = 20

#设置图像大小
fig= plt.figure(figsize=(20,28),dpi=80)

bar_width=0.3
x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇",]
x1=[i+bar_width for i in range(len(x))]
x2=[i+bar_width*2 for i in range(len(x))]


y1 =[56.01,26.4,7.53,16.9,]
y2 =[56.01,2.94,17.53,16.49,]
y3 =[6.01,26.94,1.53,6.49,]

# plt.barh(range(len(x)),y,height=0.3,color="orange")   #横着

plt.bar(range(len(x)),y1,width=bar_width,color="orange",label="9月")    #竖着
plt.bar(x1,y2,width=bar_width,color="green",label="10月")
plt.bar(x2,y3,width=bar_width,label="11月")

#设置x轴的刻度
xticks_lable=x
plt.xticks(range(len(x)),xticks_lable,rotation=0)

# 绘制网格
plt.grid(alpha=0.4)

# 添加图例
plt.legend(loc="upper right")

plt.show()


