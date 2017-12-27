from survey  import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你的第一语言是什么"
my_survey = AnonymousSurvey(question)
#显示问题并存储答案
my_survey = AnonymousSurvey(question)
#显示问题并存储答案
my_survey.show_question()
print("输入q就会停止：")
while True:
    response = input("语言：")
    if response == 'q':
        break
    my_survey.store_response(response)
#显示调查结果
print("感谢所有参加调查的人")
my_survey.show_results()