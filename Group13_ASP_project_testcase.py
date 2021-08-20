import unittest
import Group13_ASP_project as prog

class Group13_ASP_project(unittest.TestCase):
    def test_add(self):
        result=prog.top3.add(self)
        self.assertEqual(result,self)

    def test_mean(self):
        result =prog.top3.mean(self)
        self.assertEqual(result,self)








if __name__ == '__main__':
    unittest.main()