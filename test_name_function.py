import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','carver','joplin')
        self.assertEqual(formatted_name, 'Janis Carver Joplin')

if __name__=='__main__':
    unittest.main()