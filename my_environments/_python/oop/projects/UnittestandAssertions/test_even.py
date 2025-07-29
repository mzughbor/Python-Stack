# import the python testing framework
import unittest

def isEven(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
class isEvenTest(unittest.TestCase):
    
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # another way to write above is 
        # self.assertTrue(isEven(2)) 
    
    def testThree(self): 
        
        #self.assertEqual(isEven(3), False)
        self.assertEqual(isEven(30), False)
        # another way to write above is 
        # self.assertFalse(isEven(3)) 
    

    def setUp(self): 
        # add the setUp tasks
        print("running setUp") 
    
    def tearDown(self): 
        # add the tearDown tasks
        print("running tearDown tasks")
        
if __name__ == '__main__':
    unittest.main()