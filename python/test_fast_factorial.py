

import unittest

import fast_factorial

SMALL_VALUES = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


class TestNaive(unittest.TestCase):

    standard_error_message = ("Algorithm %s should have " 
                              "returned %d given argument %d " 
                              "but instead returned %s.")

    def setUp(self):
        self.algorithm_name = "Naive/Simple-minded"
        self.fact_fun = fast_factorial.naive
    
    def base_case(self, argument, expected, 
                  error_message=''):
        if error_message == '':
            error_message = self.standard_error_message
        test_res = self.fact_fun(argument)
        self.assertEqual(expected, 
                         test_res,
                         error_message % (self.algorithm_name,
                                          expected,
                                          argument,
                                          test_res))

    def testZero(self):
        self.base_case(0, 1)

    def testOne(self):
        self.base_case(1, 1)
                       
    def testSmallValues(self):
        for x in xrange(len(SMALL_VALUES)):
            self.base_case(x, SMALL_VALUES[x])


class TestMoessner(TestNaive):

    def setUp(self):
        self.algorithm_name = "Moessner Additive"
        self.fact_fun = fast_factorial.moessner


if __name__ == '__main__':
    unittest.main()
