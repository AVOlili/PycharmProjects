import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousServey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "你的第一语言？"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["英语","西班牙语","泰语"]
    def test_store_single_response(self):
         """测试单个答案会被妥地存储"""
         self.my_survey.store_response(self.responses[0])
         self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
         """测试三个答案是否会被妥善存储"""
         for resopnse in self.responses:
             self.my_survey.store_response(resopnse)
         for resopnse in self.responses:
             self.assertIn(resopnse,self.my_survey.responses)
unittest.main()

