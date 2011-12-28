
import unittest

import ackermann

class TestAckermannPeter(unittest.TestCase):

    standard_error_string = "%s(%d, %d) returned %d rather than expected %d."

    def basic_execution(self, m, n, expected):
        """
        Calculate the function, compare to expected, error if unequal.
        
        """
        result = self.ap(m, n)
        self.assertTrue(result)
        self.assertEquals(expected,
                          result,
                          self.standard_error_string % (self.test_name,
                                                        m, n, 
                                                        result,
                                                        expected))
        
    def setUp(self):
        self.ap = ackermann.ackermann_peter
        self.test_name = self.ap.__name__

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


class TestAckermannPeterFaster(TestAckermannPeter):

    def setUp(self):
        self.ap = ackermann.ackermann_peter_faster
        self.test_name = self.ap.__name__

    def test_m_three_n_under_10(self):
        for x in xrange(10):
            expected = (2 ** (x + 3)) - 3
            self.basic_execution(3, x, expected)

    def test_m_4_n_1(self):
        expected = 65533
        self.basic_execution(4, 1, expected)


class TestAckermannPeterFasterMemo(TestAckermannPeterFaster):

    def setUp(self):
        self.ap = ackermann.ackermann_peter_faster_memo
        self.test_name = self.ap.__name__
    
    def test_m_4_n_2(self):
        expected = (1 << 65536) - 3
        self.basic_execution(4, 2, expected)

    def test_m_4_n_3(self):
        intermediate = self.ap(4, 2)
        expected = (2 ** intermediate) - 3
        self.basic_execution(4, 3, expected)

if __name__ == "__main__":
    unittest.main()
