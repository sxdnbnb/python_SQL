# _*_coding : utf-8 _*_
# @Time : 2022/9/30 19:46
# @Author : SunShine
# @File : pandas_时间序列
# @Project : python_SQL
import pandas as pd
import numpy as np

index = pd.date_range("20170101", periods=10)
print(type(index))  # DatetimeIndex
df = pd.DataFrame(np.random.rand(10), index=index)
print(df)
