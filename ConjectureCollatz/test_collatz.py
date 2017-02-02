# -*- coding: utf-8 -*-

import unittest

import collatz


class CollatzBaseTestCase(object):

    @classmethod
    def setUpClass(cls):
        collatz._cache = {}

    def test_collatz_conjecture_with_number_zero(self):
        """
            0                   - 1 steps
        """
        self.assertEqual(1, self.collatz(0))

    def test_collatz_conjecture_with_number_one(self):
        """
            1                   - 1 steps
        """
        self.assertEqual(1, self.collatz(1))

    def test_collatz_conjecture_with_number_two(self):
        """
            2 / 2 = 1           - 1 steps
            1                   - 2 steps
        """
        self.assertEqual(2, self.collatz(2))

    def test_collatz_conjecture_with_number_three(self):
        """
            3 * 3 + 1 = 10      - 1 steps
            10 / 2 = 5          - 2 steps
            5 * 3 + 1 = 16      - 3 steps
            16 / 2 = 8          - 4 steps
            8 / 2 = 4           - 5 steps
            4 / 2 = 2           - 6 steps
            2 / 2 = 1           - 7 steps
            1                   - 8 steps
        """
        self.assertEqual(8, self.collatz(3))

    def test_collatz_conjecture_with_number_four(self):
        """
            4 / 2 = 2           - 1 steps
            2 / 2 = 1           - 2 steps
            1                   - 3 steps
        """
        self.assertEqual(3, self.collatz(4))

    def test_collatz_conjecture_with_number_13(self):
        self.assertEqual(10, self.collatz(13))

    def collatz(self, n):
        return collatz.collatz(n, cached=self.CACHED)


class CollatzCachedTestCase(CollatzBaseTestCase, unittest.TestCase):

    CACHED = True

    def test_should_create_cache_for_numbers(self):
        self.assertTrue(collatz._cache)


class CollatzNotCachedTestCase(CollatzBaseTestCase, unittest.TestCase):

    CACHED = False

    def test_should_not_create_cache_for_numbers(self):
        self.assertFalse(collatz._cache)


class CollatzRunTestCase(unittest.TestCase):

    def test_get_better_result_with_100(self):
        self.assertEqual((97, 119), collatz.run(100 + 1))

    def test_get_better_result_with_1000(self):
        self.assertEqual((871, 179), collatz.run(1000 + 1))

    def test_get_better_result_with_10000(self):
        self.assertEqual((6171, 262), collatz.run(10000 + 1))

    def test_get_better_result_with_100000(self):
        self.assertEqual((77031, 351), collatz.run(100000 + 1))

    def test_get_better_result_with_1000000(self):
        self.assertEqual((837799, 525), collatz.run(1000000 + 1))
