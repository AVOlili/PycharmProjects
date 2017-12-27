with open('pi_digits.txt ') as file_object:
    contents = file_object.read();
    print(contents.rstrip())#rstrip()是剔除字符串末尾的空白
    print("----------")