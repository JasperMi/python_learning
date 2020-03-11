import unittest
from test.chapter_11.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # 以test打头的方法都将自动运行
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
