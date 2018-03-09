  ###
    #     
    # @Author AVOli  
    # @Date 2018/2/11 15:39  
    # @Description   绘制一个图形，显示5000个整数的立方值
    # 并用颜色映射，参考scatter_squares()
    #
    ###

import matplotlib.pyplot as plt
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

#plt.scatter(x_values, y_values,c='red',edgecolors='none', s=40)#s=?代表大小
plt.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none', s=40)#颜色映射
#设置图表标题并给坐标轴加上标签
plt.title("Cube Numbers",fontsize = 24)
plt.xlabel("Value", fontsize = 24)
plt.ylabel("Cube of Value", fontsize = 14)
#设置刻度标记的大小
# which一共3个参数[‘major’ | ‘minor’ | ‘both’]
# 默认是major表示主刻度，后面分布为次刻度及主次刻度都显示
plt.tick_params(axis='both',which = 'major',labelsize=14)
#设置每个坐标轴的取值范围
#plt.axis([0,1100,1,1100000])
plt.savefig('cube_plot.png',bbox_inches='tight') #保存图标并裁掉空白区域
plt.show()
