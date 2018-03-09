import json

# 将数据加载到一个列表
filename = 'C:\/Users\AVOli\PycharmProjects\PythonStudy\matplot\chapter_16\population\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的数量(dictionary)
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + "：" +str(population))
