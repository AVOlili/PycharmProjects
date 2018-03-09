  ###
    #
    # @Author AVOli
    # @Date 2018/2/21 17:47
    # @Description  骰子可视化
    # 六面骰子(Die)命名为D6,八面命名为D8
    #
    ###
import pygal
from die import Die
# 创建一个D6
die = Die() # 默认D6

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = [] # 频率
for value in range(1,die.num_sides+1):
    # 计算每种点数在results出现次数
    frequcy = results.count(value)
    frequencies.append(frequcy)

# 对结果进行可视化,hist=histogram(直方图)
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


