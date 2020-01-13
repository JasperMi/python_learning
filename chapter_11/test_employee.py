import unittest
from chapter_11.employee import Employee


class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """
        创建一个Employee类的对象，供使用的测试方法使用
        """
        self.employee = Employee('Frank', 'Jack', 2000000)

    def test_give_default_raise(self):
        """测试增加默认年薪"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 2005000)

    def test_give_custom_raise(self):
        """测试增加自定义年薪"""
        self.employee.give_raise(100000)
        self.assertEqual(self.employee.annual_salary, 2100000)


if __name__ == "__main__":
    unittest.main()
