# _*_coding : utf-8 _*_
# @Time : 2022/7/12 15:56
# @Author : SunShine
# @File : mysql
# @Project : python_SQL

# -*- coding:utf-8 -*-
import pymysql
import json
def get_loan_number(file):
    connect = pymysql.connect(
        host='localhost',
        port = 3306,
        user = 'root',
        password = '6446530',
        db = 'book',
        charset = 'utf8',
    )
    # print("写入中，请等待……")
    cursor = connect.cursor()
    sql = "SELECT * from book_inf;"
    cursor.execute(sql)
    number = cursor.fetchall()
    print(number)
    # data = json.dumps(number)
    fp = open(file, "w")
    loan_count = 0
    for loanNumber in number:
        loan_count += 1
        fp.write(loanNumber[0] + " "+loanNumber[1]+"\n")
    # for loanNumber in number:
    #     loan_count += 1
    #     fp.write(data)
    fp.close()
    cursor.close()
    connect.close()
    print("写入完成,共写入%d条数据……" % loan_count)


if __name__ == "__main__":
    file = r"1.txt"
    get_loan_number(file)
    fp = open('1.txt', 'r')
    content = fp.read()
    fp.close()
    print(content)
    fp = open('1.txt', "w")
    sorted = sorted(content, reverse=True)
    # print(sorted)