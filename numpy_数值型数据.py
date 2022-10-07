# _*_coding : utf-8 _*_
# @Time : 2022/9/20 21:42
# @Author : SunShine
# @File : numpy_01
# @Project : python_SQL

import numpy as np
import random
# 使用numpy生成数组，得到ndarray的类型
t1=np.array([1,2,3])
# print(t1)
# print(type(t1))
# [1 2 3]
# <class 'numpy.ndarray'>
t2=np.array(range(10),dtype=bool)
# print(t2)
# print(t2.dtype)      #数据的类型
# 等价于
t3=np.arange(10)
# print(t3)

t4=np.arange(2,10,2)
# print(t4)
# print(t4.dtype)

t5=np.array([random.random() for i in range(10)])   # 用于生成10个一个0到1的随机浮点数: 0 <= n < 1.0\
# print(t5)

t6=np.round(t5,2)  #保留两位小数
# print(t6)

t7=np.random.rand(2,4)
# print(10*t7)

np.random.seed(10)   #数字是个种子编号，随便写
t8=np.random.randint(10,20,(4,5))   #创建4行5列的整数数组，整数范围是10~20
print(t8)
print(np.argmax(t8,axis=0))   #每一列最大值的位置
print(np.argmax(t8,axis=1))   #每一行最大值的位置


