# _*_coding : utf-8 _*_
# @Time : 2022/9/23 15:34
# @Author : SunShine
# @File : pandas_读取数据
# @Project : python_SQL
import pandas as pd
import numpy as np
# DataFrame是Series的容器
t1=pd.DataFrame(np.arange(12).reshape(3,4))
# print(t1)
# print(type(t1))

# 指定行列索引
t2=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
# print(t2)
# []里写 数字 表示对 行 进行操作
# []里写 字符串 表示对 列 进行操作
# print(df[:20])     #取前20行
# print(df[:20]["Row_Labels"])    #Series类型，因为只有一列
# print(t2.loc["a"])   #df.loc 通过标签索引行数据
# print(t2.loc[["a","c"],"Y"])

# print(t2.iloc[:,[2,1]])
t2.iloc[:2,2:]=np.nan
print(t2)

# 由字典构建DataFrame
dict={"name":["s","x"],"age":[20,30],"sex":["w","b"]}
t3=pd.DataFrame(dict)
# print(t3)
# print(t3.values)

# 读取csv中的文件
df=pd.read_csv("./datasourse/狗的名字的统计数据/dogNames2.csv")
# print(df)
df=df.sort_values(by="Count_AnimalName",ascending=False)
# print(df.head(10))
# print(df[(df["Count_AnimalName"]>700)&(df["Count_AnimalName"]<800)])

# print(pd.isnull(t2))
# print(t2[pd.notnull(t2["Y"])])  #输出Y列不是NAN的那一行
#

# print(t2.dropna(axis=0,how="any"))  # 输出没有NAN的行
# print(t2.dropna(axis=0,how="all"))  # 输出没有全是NAN的行
# t2.dropna(axis=0,how="any",inplace=True)  # 删除有NAN的行
# print(t2)
# t2=t2.fillna(t2.mean())  # 用平均值填充数据
t2["Y"]=t2["Y"].fillna(t2["Y"].mean())   # 把Y列用Y列平均值填充数据

print(t2)








