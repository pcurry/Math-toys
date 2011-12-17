#!/usr/bin/python

import unittest

import tail_recursive

class TestCollatz_Orbit_List(unittest.TestCase):

    def setUp(self):
        self.c_o_l = tail_recursive.collatz_orbit_list

    def testBaseCases(self):
        self.assertEquals(self.c_o_l(1), [1])
        self.assertEquals(self.c_o_l(2), [2, 1])
        self.assertEquals(self.c_o_l(4), [4, 2, 1])

    
class TestCollatz_Orbit_T_R_M(unittest.TestCase):

    def setUp(self):
        self.cotrm = tail_recursive.collatz_orbit_tail_recursive_memo
        self.test_memo = {1: [1], 2: [2, 1], 4: [4, 2, 1]}

    def testBaseCases(self):
        self.assertEquals(self.cotrm(1, [], self.test_memo), [1])
        self.assertEquals(self.cotrm(2, [], self.test_memo), [2, 1])
        self.assertEquals(self.cotrm(4, [], self.test_memo), [4, 2, 1])


        

if __name__ == '__main__':
    unittest.main()
