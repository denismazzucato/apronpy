"""
APRON Intervals on Scalars - Unit Tests
=======================================

:Author: Caterina Urban
"""
import unittest
from ctypes import c_int, c_double

from apronpy.interval import PyInterval
from apronpy.mpfr import PyMPFR
from apronpy.mpq import PyMPQ
from apronpy.scalar import PyDoubleScalar, PyMPQScalar, PyMPFRScalar


class TestInterval(unittest.TestCase):

    def test_init(self):
        self.assertEqual(str(PyInterval(-9, 9)), '[-9/1,9/1]')
        self.assertEqual(str(PyInterval(c_int(-9), c_int(9))), '[-9/1,9/1]')
        self.assertEqual(str(PyInterval(-0.5, 0.5)), '[-0.5,0.5]')
        self.assertEqual(str(PyInterval(c_double(-0.5), c_double(0.5))), '[-0.5,0.5]')
        self.assertEqual(str(PyInterval(PyMPQ(-1, 2), PyMPQ(1, 2))), '[-1/2,1/2]')
        self.assertEqual(str(PyInterval(PyMPFR(-0.5), PyMPFR(0.5))), '[-0.5,0.5]')
        self.assertEqual(str(PyInterval(PyDoubleScalar(-0.5), PyDoubleScalar(0.5))), '[-0.5,0.5]')
        self.assertEqual(str(PyInterval(PyMPQScalar(-1, 2), PyMPQScalar(1, 2))), '[-1/2,1/2]')
        self.assertEqual(str(PyInterval(PyMPFRScalar(-0.5), PyMPFRScalar(0.5))), '[-0.5,0.5]')

    # def test_infty(self):
    #     self.assertEqual(PyDoubleScalar(9).infty(), 0)
    #     self.assertEqual(PyDoubleScalar.init_infty(-9).infty(), -1)
    #     self.assertEqual(PyDoubleScalar.init_infty(0).infty(), 0)
    #     self.assertEqual(PyDoubleScalar.init_infty(9).infty(), 1)
    #
    # def test_cmp(self):
    #     self.assertTrue(PyDoubleScalar(0.5) < PyDoubleScalar(9))
    #     self.assertTrue(PyDoubleScalar(9) == PyDoubleScalar(9))
    #     self.assertTrue(PyDoubleScalar(9) > PyDoubleScalar(0.5))
    #
    # def test_sign(self):
    #     self.assertEqual(PyDoubleScalar(-9).sign(), -1)
    #     self.assertEqual(PyDoubleScalar(c_double(-9)).sign(), -1)
    #     self.assertEqual(PyDoubleScalar(9).sign(), 1)
    #     self.assertEqual(PyDoubleScalar(c_double(9)).sign(), 1)
    #     self.assertEqual(PyDoubleScalar(0).sign(), 0)
    #     self.assertEqual(PyDoubleScalar(c_double(0)).sign(), 0)
    #     self.assertEqual(PyDoubleScalar.init_infty(-9).sign(), -1)
    #     self.assertEqual(PyDoubleScalar.init_infty(0).sign(), 0)
    #     self.assertEqual(PyDoubleScalar.init_infty(9).sign(), 1)
    #
    # def test_neg(self):
    #     self.assertEqual(-PyDoubleScalar(-9), PyDoubleScalar(9))
    #     self.assertEqual(-PyDoubleScalar(c_double(-9)), PyDoubleScalar(c_double(9)))
    #     self.assertEqual(-PyDoubleScalar(9), PyDoubleScalar(-9))
    #     self.assertEqual(-PyDoubleScalar(c_double(9)), PyDoubleScalar(c_double(-9)))
    #     self.assertEqual(-PyDoubleScalar(0), PyDoubleScalar(0))
    #     self.assertEqual(-PyDoubleScalar(c_double(0)), PyDoubleScalar(c_double(0)))
    #     self.assertEqual(-PyDoubleScalar.init_infty(-9), PyDoubleScalar.init_infty(9))
    #     self.assertEqual(-PyDoubleScalar.init_infty(0), PyDoubleScalar.init_infty(0))
    #     self.assertEqual(-PyDoubleScalar.init_infty(9), PyDoubleScalar.init_infty(-9))


if __name__ == '__main__':
    unittest.main()