#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

	def test_narmal (self):
		self.assertEqual (21, calc(3,7))

	def test_min (self):
		self.assertEqual (1, calc(1,1))

	def test_max (self):
		self.assertEqual (999*999, calc(999,999))

	def test_zero (self):
		self.assertEqual (-1, calc(0,1))
		self.assertEqual (-1, calc(1,0))
		self.assertEqual (-1, calc(0,0))

	def test_over (self):
		self.assertEqual (-1, calc(1000,1))
		self.assertEqual (-1, calc(1,1000))
		self.assertEqual (-1, calc(1000,1000))

	def test_str (self):
		self.assertEqual (-1, calc("a",1))
		self.assertEqual (-1, calc(1,"a"))
		self.assertEqual (-1, calc("a","b"))

	def test_float (self):
		self.assertEqual (-1, calc(0.1,999))
		self.assertEqual (-1, calc(999,0.1))
		self.assertEqual (-1, calc(0.1,0.1))

	def test_special_character (self):
		self.assertEqual (-1, calc("@",1))
		self.assertEqual (-1, calc(1,"@"))
		self.assertEqual (-1, calc("@","@"))
