import unittest
from GameData import GameData
from UserLogs import UserLogs
from StatEnum import Stat
from CharacterInstance import CharacterInstance
from State import State
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

		test_gd = GameData("shadow_dragon.csv")
		test_ul = UserLogs("user_log.csv", test_gd)
		number_of_characters = 59
		number_of_max_stats = 31
		number_of_base_classes = 13
		number_of_promoted_classes = 13
		number_of_promotion_gains = 14

		test_gd_locals = test_gd.get_local_variables()
		nc = len(test_gd_locals[0])
		ms = len(test_gd_locals[1])
		bc = len(test_gd_locals[2])
		pc = len(test_gd_locals[3])
		pg = len(test_gd_locals[4])

		# ensure that we've correctly parsed the input file
		self.assertEqual(number_of_characters, nc)
		self.assertEqual(number_of_max_stats, ms)
		self.assertEqual(number_of_base_classes, bc)
		self.assertEqual(number_of_promoted_classes, pc)
		self.assertEqual(number_of_promotion_gains, pg)

		# test an example character - Marth
		marth = test_gd.get_character_data("Marth")

		# test Marth's base level and class
		self.assertEqual(marth.base_level, 1)
		self.assertEqual(marth.get_base_class(), "Lord")

		# test Marth's base stats
		marth_base_HP = marth.get_base_value(Stat.HP)
		marth_base_Str = marth.get_base_value(Stat.Str)
		marth_base_Mag = marth.get_base_value(Stat.Mag)
		marth_base_Skl = marth.get_base_value(Stat.Skl)
		marth_base_Spd = marth.get_base_value(Stat.Spd)
		marth_base_Lck = marth.get_base_value(Stat.Lck)
		marth_base_Def = marth.get_base_value(Stat.Def)
		marth_base_Res = marth.get_base_value(Stat.Res)

		self.assertEqual(marth_base_HP, 18)
		self.assertEqual(marth_base_Str, 5)
		self.assertEqual(marth_base_Mag, 0)
		self.assertEqual(marth_base_Skl, 3)
		self.assertEqual(marth_base_Spd, 7)
		self.assertEqual(marth_base_Lck, 7)
		self.assertEqual(marth_base_Def, 7)
		self.assertEqual(marth_base_Res, 0)


	def test_nonexistent_file_read(self):
		"""Tests handling of a request for a non-existent file"""

		test_gd = GameData("./inputTests/nonExistent.csv")
		test_gd_locals = test_gd.get_local_variables()

		nc = len(test_gd_locals[0])
		ms = len(test_gd_locals[1])
		bc = len(test_gd_locals[2])
		pc = len(test_gd_locals[3])
		pg = len(test_gd_locals[4])

		self.assertEqual(0, nc)
		self.assertEqual(0, ms)
		self.assertEqual(0, bc)
		self.assertEqual(0, pc)
		self.assertEqual(0, pg)



	def test_empty_file_read(self):
		"""Tests handling of a request for an empty file"""

		test_gd = GameData("./inputTests/empty.csv")
		test_gd_locals = test_gd.get_local_variables()

		nc = len(test_gd_locals[0])
		ms = len(test_gd_locals[1])
		bc = len(test_gd_locals[2])
		pc = len(test_gd_locals[3])
		pg = len(test_gd_locals[4])

		self.assertEqual(0, nc)
		self.assertEqual(0, ms)
		self.assertEqual(0, bc)
		self.assertEqual(0, pc)
		self.assertEqual(0, pg)


class TestModeling(unittest.TestCase):
	"""
	TestModeling contains tests for modeling of character growth and growth 
	comparison functions
	"""

	def test_comparison(self):
		"""Tests the team recommendation feature"""
		test_gd = GameData("shadow_dragon.csv")
		user_logs = UserLogs("test_log.csv", test_gd)
		test_gd_locals = test_gd.get_local_variables()

		# test an example character - Marth
		marth = test_gd.get_character_data("Marth")

		# create a character instance with more than one state
		marth_base_HP = marth.get_base_value(Stat.HP)
		marth_base_Str = marth.get_base_value(Stat.Str)
		marth_base_Mag = marth.get_base_value(Stat.Mag)
		marth_base_Skl = marth.get_base_value(Stat.Skl)
		marth_base_Spd = marth.get_base_value(Stat.Spd)
		marth_base_Lck = marth.get_base_value(Stat.Lck)
		marth_base_Def = marth.get_base_value(Stat.Def)
		marth_base_Res = marth.get_base_value(Stat.Res)

		stat_dict_marth_1 = {Stat.HP: marth_base_HP,
					   Stat.Str: marth_base_Str,
					   Stat.Mag: marth_base_Mag,
					   Stat.Skl: marth_base_Skl,
					   Stat.Spd: marth_base_Spd,
					   Stat.Lck: marth_base_Lck,
					   Stat.Def: marth_base_Def,
					   Stat.Res: marth_base_Res}

		stat_dict_marth_10 = {Stat.HP: 24.4,
						Stat.Str: 9,
						Stat.Mag: 0,
						Stat.Skl: 6,
						Stat.Spd: 11,
						Stat.Lck: 12,
						Stat.Def: 8,
						Stat.Res: .1}

		marth_1 = State(1, "Lord", stat_dict_marth_1)
		marth_10 = State(10, "Lord", stat_dict_marth_10)

		marth_instance = CharacterInstance(test_gd.get_character_data("Marth"), marth_1)
		# test the update function
		marth_instance.add_new_state(marth_10)

		# create the average state for marth at level 10 to test the predict function
		marth_avg_10_HP = marth.predict_state(10, "Lord", Stat.HP, test_gd)
		marth_avg_10_Str = marth.predict_state(10, "Lord", Stat.Str, test_gd)
		marth_avg_10_Mag = marth.predict_state(10, "Lord", Stat.Mag, test_gd)
		marth_avg_10_Skl = marth.predict_state(10, "Lord", Stat.Skl, test_gd)
		marth_avg_10_Spd = marth.predict_state(10, "Lord", Stat.Spd, test_gd)
		marth_avg_10_Lck = marth.predict_state(10, "Lord", Stat.Lck, test_gd)
		marth_avg_10_Def = marth.predict_state(10, "Lord", Stat.Def, test_gd)
		marth_avg_10_Res = marth.predict_state(10, "Lord", Stat.Res, test_gd)

		self.assertEqual(marth_avg_10_HP, 25.2)
		self.assertEqual(marth_avg_10_Str, 9.5)
		self.assertEqual(marth_avg_10_Mag, 0)
		self.assertEqual(marth_avg_10_Skl, 6.6)
		self.assertEqual(marth_avg_10_Spd, 11.5)
		self.assertEqual(marth_avg_10_Lck, 13.3)
		self.assertEqual(marth_avg_10_Def, 8.8)
		self.assertEqual(marth_avg_10_Res, 0.18)

		# create two other character instances to test the comparison function
		stat_dict_Frey_10 = {Stat.HP: 25.2,
							 Stat.Str: 10.15,
							 Stat.Mag: 0,
							 Stat.Skl: 10.95,
							 Stat.Spd: 10.95,
							 Stat.Lck: 6.05,
							 Stat.Def: 8.8,
							 Stat.Res: 0}
		frey_10 = State(10, "Cavalier", stat_dict_Frey_10)
		frey_instance = CharacterInstance(test_gd.get_character_data("Frey"), frey_10)

		stat_dict_Abel_10 = {Stat.HP: 25.85,
							 Stat.Str: 9.6,
							 Stat.Mag: 0,
							 Stat.Skl: 11.5,
							 Stat.Spd: 11.5,
							 Stat.Lck: 4.25,
							 Stat.Def: 8.8,
							 Stat.Res: 0}

		abel_10 = State(10, "Cavalier", stat_dict_Abel_10)
		abel_instance = CharacterInstance(test_gd.get_character_data("Abel"), abel_10)

		instance_list = [marth_instance, frey_instance, abel_instance]
		user_logs.update_logs(marth_instance)
		user_logs.update_logs(frey_instance)
		user_logs.update_logs(abel_instance)

		# test the recommendations
		recommendations = user_logs.recommend_team(2)
		self.assertEqual(recommendations[0], "Frey")
		self.assertEqual(recommendations[1], "Abel")


if __name__ == '__main__':
	unittest.main()