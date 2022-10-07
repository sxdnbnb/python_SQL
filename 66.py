# _*_coding : utf-8 _*_
# @Time : 2022/7/12 16:47
# @Author : SunShine
# @File : 66
# @Project : python_SQL
import pymysql
import pandas as pd

host='localhost'
port=3306
user='root'
password='6446530'
db='db1'
charset='utf8'
db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db)
print('连接成功')

#用于数据库查询结果以及执行sql语句
cursor = db.cursor()
sql1 = 'SELECT * from user;'
cursor.execute(sql1)
data1 = cursor.fetchall()
# print((type(data1)))
print("原")
print(data1)

#将获取的数据转化为dataframe格式
infor = cursor.description  # 获取连接对象的描述信息
print("描述信息")
print(infor)

columnNames = [infor[i][0] for i in range(len(infor))]  # 获取列名
# print(data1[1])
df = pd.DataFrame([list(i) for i in data1], columns=columnNames)  #得到的data为二维元组，逐行取出，转化为列表df
print("列表")
print(df)

#对取出的数根据applydate这列进行排序
data2 = df.sort_values(by='applydata', axis = 0,ascending = False)#降序
print("降序")
print(data2)

#排序后根据applydate这列进行去重  drop_duplicates()默认保留重复值，不保留重复值设置参数keep为False
data3 = data2.drop_duplicates('applydata')

# data3 = data2.drop_duplicates(subset=['applydate'],keep='last', inplace=True)

print("去重")
print(data3)

#取列表dataframe的最后一行的count值
print('列表dataframe的最后一行的count值')
print(df.iloc[-1,1])

#删掉applydate这列所有行的后三个字符，只保留年份
print("只保留年份")
# data5 = df['applydata'].str[:-3]
df['applydata'] = df['applydata'].map(lambda x: str(x)[:-3])
# b1 = df['count']
# data6=data5.append(b1)
print(df)
#提交数据
db.commit()
cursor.close()
db.close()
