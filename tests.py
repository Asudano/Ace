import unittest
import Reader
import sys

class TestReader(unittest.TestCase):
	"""
	TestReader contains tests for the Reader module
	"""

	# **ISSUE** The following classes are present in max_stats but missing from
	# base_classes and promoted_classes:
	# 	Chameleon, Manakete, Thief, Ballistician, Lord
	# Test documents current output, not desired output  
	def test_file_read(self):
		"""Test to make sure that all of the data from the input file 
		./shadow_dragon.csv is being read into the program"""
		(game_characters, 
			max_stats, 
			promotion_gains, 
			base_classes, 
			promoted_classes) = Reader.read_infile("./shadow_dragon.csv")
		number_of_characters = 59
		number_of_clases = 31
		number_of_base_classes = 13
		number_of_promoted_classes = 13
		self.assertEqual(number_of_characters, len(game_characters))
		self.assertEqual(number_of_clases, len(max_stats.keys()))
		self.assertEqual(number_of_promoted_classes, 
			len(promotion_gains.keys()))
		self.assertEqual(number_of_base_classes, len(base_classes))
		self.assertEqual(number_of_promoted_classes, len(promoted_classes))

	def test_nonexistent_file_read(self):
		"""Tests handling of a request for a non-existent file"""
		(game_characters, 
			max_stats, 
			promotion_gains, 
			base_classes, 
			promoted_classes) = Reader.read_infile("./inputTests/nonExistent.csv")
		self.assertEqual(0, len(game_characters))
		self.assertEqual(0, len(max_stats.keys()))
		self.assertEqual(0, len(promotion_gains.keys()))
		self.assertEqual(0, len(base_classes))
		self.assertEqual(0, len(promoted_classes))

	def test_empty_file_read(self):
		"""Tests handling of a request for an empty file"""
		(game_characters, 
			max_stats, 
			promotion_gains, 
			base_classes, 
			promoted_classes) = Reader.read_infile("./inputTests/empty.csv")
		self.assertEqual(0, len(game_characters))
		self.assertEqual(0, len(max_stats.keys()))
		self.assertEqual(0, len(promotion_gains.keys()))
		self.assertEqual(0, len(base_classes))
		self.assertEqual(0, len(promoted_classes))

	def test_game_characters(self):
		"""Unfinished test for a data file containing only characters block"""
		(game_characters, 
			max_stats, 
			promotion_gains, 
			base_classes, 
			promoted_classes) = Reader.read_infile("./inputTests/Character.csv")
		self.assertEqual(6, len(game_characters))
		self.assertEqual(0, len(max_stats.keys()))
		self.assertEqual(0, len(promotion_gains.keys()))
		self.assertEqual(0, len(base_classes))
		self.assertEqual(0, len(promoted_classes))

		marth = game_characters[0]
		self.assertEqual(marth.getName(), "Marth")
		self.assertEqual(marth.getBaseLevel(), 0)

class TestModeling(unittest.TestCase):
	"""
	TestModeling contains tests for modeling of character growth and growth 
	comparison functions
	"""

if __name__ == '__main__':
	unittest.main()