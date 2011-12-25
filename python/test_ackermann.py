
import unittest

import ackermann

class TestAckermannPeter(unittest.TestCase):

    def setUp(self):
        self.ap = ackermann.ackermann_peter
        self.test_name = self.ap.__name__
        
        
    def test_m_zero_n_under_10(self):
        for x in xrange(10):
            result = self.ap(0, x)
            self.assertTrue(result)
            self.assertEquals(x, 
                              result,
                              "%s(0, %d) returned %d rather than expected %d." % (self.test_name, x, result, x))
    


if __name__ == "__main__":
    unittest.main()
