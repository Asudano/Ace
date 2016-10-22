import unittest
import Reader

class TestReader(unittest.TestCase):
	"""
	TestReader contains tests for the Reader module
	"""

	def test_file_read(self):
		"""Test to make sure that all of the data from the input file 
		./shadow_dragon.csv is being read into the program"""
		infile = open("./shadow_dragon.csv", "r")
		(game_characters, max_stats, promotion_gains) = Reader.read_infile(infile)
		number_of_characters = 59
		number_of_clases = 31
		number_of_base_classes = 13
		self.assertEqual(number_of_characters, len(game_characters))
		self.assertEqual(number_of_clases, len(max_stats.keys()))
		self.assertEqual(number_of_base_classes, len(promotion_gains.keys()))

class TestModeling(unittest.TestCase):
	"""
	TestModeling contains tests for modeling of character growth and growth 
	comparison functions
	"""

if __name__ == '__main__':
	unittest.main()