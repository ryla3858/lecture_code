import unittest
import random
import os
import sys

sys.path.append("orig/unit_testing/")  # noqa

import math_lib
import math


class TestMathLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_lib.add(10, -5), 5)

    def test_sub(self):
        self.assertEqual(math_lib.sub(10, -5), 15)

    def test_div_by_zero_raises(self):
        self.assertRaises(ZeroDivisionError, math_lib.div, 10, 0)

    def test_div_by_underflowed_float_raises(self):
        self.assertRaises(ZeroDivisionError, math_lib.div, 10, 1e-400)

#    def test_div_by_zero_returns_none(self):
#        self.assertIsNone(math_lib.div(10, 0))
#
#    def test_div_by_underflowed_float_returns_none(self):
#        self.assertIsNone(math_lib.div(10, 1e-400))


"""
    def test_add_floats_exact_equal_fails(self):
        # intentionally fails, run this one
        # live to show why == is risky with floats
        self.assertEqual(math_lib.add(0.1, 0.2), 0.3)

    def test_div_by_zero_returns_none(self):
        self.assertIsNone(math_lib.div(10, 0))

    def test_div_by_underflowed_float_returns_none(self):
        self.assertIsNone(math_lib.div(10, 1e-400))

    def test_add_floats_approx_equal_passes(self):
        self.assertAlmostEqual(math_lib.add(0.1, 0.2), 0.3)

    def test_add_nan_exact_equal_fails(self):
        self.assertEqual(math_lib.add(float('nan'), 1), float('nan'))
        self.assertTrue(math.isnan(math_lib.add(float('nan'), 1)))

    def test_rand_norm_returns_float(self):
        value = math_lib.rand_norm(0, 1)
        self.assertIsInstance(value, float)

    def test_rand_norm_is_deterministic_with_seed(self):
        random.seed(42)
        first = math_lib.rand_norm(0, 1)
        random.seed(42)
        second = math_lib.rand_norm(0, 1)
        self.assertEqual(first, second)
"""


class TestFileAdd(unittest.TestCase):
    def setUp(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')
        self.direct_sum = 0
        for i in range(100):
            rand_int = random.randint(1, 100)
            self.direct_sum += rand_int
            f.write(str(rand_int) + '\n')
        f.close()

    def tearDown(self):
        os.remove(self.test_file_name)

    def test_file_add(self):
        file_sum = math_lib.file_add(self.test_file_name)
        self.assertEqual(file_sum, self.direct_sum)


if __name__ == '__main__':
    unittest.main()
