import json
def get_stored_username():
    """如果存储了用户，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("请输入你的用户名：")
    filename = 'username.json'
    #'w'模式写入 ，会覆盖
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("你的名字是否是："+username+"!")
        validate =  input("Y/N:")
        if validate == 'Y':
            print("欢迎回来，"+username+"!")
        else:
            get_new_username()
    else:
        username = get_new_username()
        print(username+"，你下次回来时我会记住你！")
greet_user()
