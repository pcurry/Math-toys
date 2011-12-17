#!/usr/bin/python

import unittest

import tail_recursive

class TestCollatz_Orbit_List(unittest.TestCase):

    def setUp(self):
        self.c_o_l = tail_recursive.collatz_orbit_list

    def testOne(self):
        self.assertEquals(self.c_o_l(1), [1])
    
class TestCollatz_Orbit_T_R_M(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
