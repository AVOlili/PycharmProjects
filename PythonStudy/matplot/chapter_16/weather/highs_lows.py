  ###
    #
    # @Author AVOli
    # @Date 2018/2/24 11:10
    # @Description   测试csv文件读取
    #
    ###
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取最高温度,最低温度和日期
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # next()返回一行,header_row代表头行
    header_row = next(reader)

    # enumerate(枚举),打印文件头及其位置
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    highs,lows,dates = [],[],[]
    for row in reader:
        #把每一行第二列添加到highs列表
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
    #print(highs)

# 根据数绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs ,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 设置图形的格式
plt.title("Daily high and low temperatures - 2004",fontsize = 24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() #绘制倾斜的日期标签
plt.ylabel("Temperature (F)",fontsize = '16')
plt.tick_params(axis='both',which='major',labelsize=12)
plt.show()
