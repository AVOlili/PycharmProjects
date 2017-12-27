import unittest
from name_function import get_formatted_name

class MyTestCase(unittest.TestCase):
    def test_something(self):
        formatted_name = get_formatted_name('AVO','123')
        self.assertEqual(formatted_name, 'Avo Li')

if __name__ == '__main__':
    unittest.main()