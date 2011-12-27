
import unittest

import ackermann

class TestAckermannPeter(unittest.TestCase):

    def basic_execution(self, m, n, expected):
        """
        Calculate the function, compare to expected, error if unequal.
        
        """
        result = self.ap(m, n)
        self.assertTrue(result)
        self.assertEquals(expected,
                          result,
                          self.error_string % (self.test_name,
                                               m, n, 
                                               result,
                                               expected))
        
    def setUp(self):
        self.ap = ackermann.ackermann_peter
        self.test_name = self.ap.__name__
        self.error_string = "%s(%d, %d) returned %d rather than expected %d."


    def test_m_zero_n_under_10(self):
        for x in xrange(10):
            expected = x + 1
            self.basic_execution(0, x, expected)
            
    def test_m_one_n_under_10(self):
        for x in xrange(10):
            expected = x + 2
            self.basic_execution(1, x, expected)

    def test_m_two_n_under_10(self):
        for x in xrange(10):
            expected = (2 * x) + 3
            self.basic_execution(2, x, expected)

if __name__ == "__main__":
    unittest.main()
