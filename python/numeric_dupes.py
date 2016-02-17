#!/usr/bin/env python2.7

import unittest


def general_dupes(lyst):
    initial = set()
    dupes = set()
    for item in lyst:
        if item in initial:
            dupes.add(item)
        else:
            initial.add(item)
    return sorted(list(dupes))


def is_number(item):
    return type(item) in (int, long, float)


def numeric_dupes(lyst):
    initial = set()
    dupes = set()
    for item in lyst:
        if item in initial and is_number(item):
            dupes.add(item)
        else:
            initial.add(item)
    return sorted(list(dupes))


class TestGeneralDupes(unittest.TestCase):

    def test_empty_list(self):
        result = general_dupes([])
        self.assertEqual(result, [])

    def test_single_element(self):
        source = [15]
        result = general_dupes(source)
        self.assertEqual(result, [])

    def test_several_items_no_dupes(self):
        source = range(10)
        result = general_dupes(source)
        self.assertEqual(result, [])

    def test_identical_pair(self):
        source = [15, 15]
        result = general_dupes(source)
        self.assertEqual(result, [15])

    def test_many_identical_dupes(self):
        source = [15, 15, 15, 15, 15]
        result = general_dupes(source)
        self.assertEqual(result, [15])

    def test_several_distinct_dupes(self):
        source = [12, 4, 67, 9, 4, 35, 12, 4, 99, 7, 5, 5, 5, 5]
        result = general_dupes(source)
        self.assertEqual(result, [4, 5, 12])


class TestNumericDupes(unittest.TestCase):

    def test_empty_list(self):
        result = numeric_dupes([])
        self.assertEqual(result, [])

    def test_single_element(self):
        source = [15]
        result = numeric_dupes(source)
        self.assertEqual(result, [])

    def test_several_items_no_dupes(self):
        source = range(10)
        result = numeric_dupes(source)
        self.assertEqual(result, [])

    def test_identical_pair(self):
        source = [15, 15]
        result = numeric_dupes(source)
        self.assertEqual(result, [15])

    def test_many_identical_dupes(self):
        source = [15, 15, 15, 15, 15]
        result = numeric_dupes(source)
        self.assertEqual(result, [15])

    def test_several_distinct_dupes(self):
        source = [12, 4, 67, 9, 4, 35, 12, 4, 99, 7, 5, 5, 5, 5]
        result = numeric_dupes(source)
        self.assertEqual(result, [4, 5, 12])

    def test_non_number_dupes(self):
        source = [12, 'foo', 11, 'foo']
        result = numeric_dupes(source)
        self.assertEqual(result, [])

    def test_several_dupe_types(self):
        source = [1, 'too', 3.5, 'too', 1, 4, 7.0, 3.5]
        result = numeric_dupes(source)
        self.assertEqual(result, [1, 3.5])


if __name__ == "__main__":
    unittest.main()
