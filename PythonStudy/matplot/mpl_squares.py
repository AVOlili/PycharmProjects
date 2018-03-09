import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体,黑体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
input_values  = [1,2,3,4,5]
squares  = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 1)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)
plt.show()
