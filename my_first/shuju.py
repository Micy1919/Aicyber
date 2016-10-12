#coding:utf-8
import csv
import pandas as pd
from matplotlib import pyplot as plt
shuju = csv.reader(file('shuju.csv','rb'))
#读取csv
df = pd.read_csv('shuju.csv')
#提取顾客信息
df2 = df.iloc[:,2]
df2_5 = df2.value_counts()
df2_5 = df2_5[df2_5 > 5]
price = 0
for i in range(1000000):
	if df.loc[i][2] in  df2_5.index:
		price += df.loc[i][3]
	print i
print price,len(df2_5)
		
#提取交易价格:
df3 = df.iloc[:,3]
df3l = list(df3)
#提取店铺数量
df5 = df.iloc[:,5]
df5 = df5.value_counts()
#print df5
#提取产品数目
df6 = df[df.iloc[:,5]=='宝洁官方旗舰店']
df6 = df6.iloc[:,6]
df6 = df6.value_counts()
df6_1000 = df6
df6L = list(df6_1000[df6_1000>1000])
#print len(df6),sum(list(df6)),len(df6L),sum(df6L)
#print df6.head(10)
'''
plt.plot(df6L)
plt.show()
plt.clf()
print 647266/852938
'''
'''
num = {}
sum_num = 0
for line in shuju:
	sum_num += 1
	if line[2] not in num:
		num[line[2]]=0
	if sum_num < 3:
		print line[2]
	print sum_num
print sum_num,len(num)
'''
