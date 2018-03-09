  ###
    #
    # @Author AVOli
    # @Date 2018/2/19 16:34
    # @Description   rw(RandomWalk)可视化（visual）
    #
    ###
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态， 就不断地模拟随机漫步
while True:
    #创建一个RandomWalk实例,并将其包含的点都绘制出来
    rw = RandomWalk(50)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))
    #ponint_numbers点的编号，颜色随编号加深
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)

    # 突出起点和终点
    plt.scatter(0, 0, c='yellow', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    keep_running = input("继续吗？(y/n):")
    if keep_running == "n":
        break