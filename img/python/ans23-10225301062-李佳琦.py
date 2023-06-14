#pro1.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
#以上代码不得改动

#（1）读取文件student_score.csv(gbk编码) 中的学生语文、数学、英语三列成绩数据,注意csv文件中的分隔符，且数据中含中文字符
df = pd.read_csv(student_score.csv)
print(df[:,[2,5]])

#（2）数据清洗：将成绩中的"缺考"替换为NaN，清除三门课全部缺考的学生，将部分缺考的学生成绩设为0
df.reshape('缺考',NaN)
x = df. dropna(axis=0, how='all', inplace=True) 
y = df. fillna(value=0,inplace=True) 
print(x)
print(y)

#（3）数据统计和分析：输入一个总成绩，输出比这个总成绩高的人数。
ascore=int(input("输入一个总成绩：\n"))

#（4）绘制出数学成绩各成绩段的饼图并保存为"pie.png"。
a=sum(df.数学<60)
b = sum((df.数学>60)%(df.数学<69))
c = sum((df.数学>70)%(df.数学<79))
d = sum((df.数学>80)%(df.数学<89))
e = sum((df.数学>90)%(df.数学<100))
labels = ['不及格','60~69分','70~79分','80~89分','90~100分']
sizes = [a,b,c,d,e] #各个值 (最重要的数据 )

#以下代码不得改动
plt.savefig('pie.png')
plo.show
