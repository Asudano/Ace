from CharacterData import CharacterData
from State import State
import StatEnum


class GameData(object):
	"""Stores constraints defined by the game itself and not by the
	Player.

	GameData is a singleton class that stores values that are read from a 
	.csv file and used to model characters in our tracker.

	Attributes:
	    instance : a __GameData object encapsulating all data for the GameData
	"""
	class __GameData(object):
		"""Stores the data required for an instance of the GameData
		singleton class

			Attributes:
	    __game_characters : a dict<str, CharacterData> mapping character 
	        names onto CharacterData objects. This contains all usable 
		characters in the game
		__max_stats : a dict<str, dict<Stat, int>> which defines a 
		    mapping from a class name onto a mapping between the various
		    stats defined in the game and the maximum values a character
		    of the define class can have
		    Ex: __max_stats["A"][HP] = 50 means that a character of 
		        class A can have an HP that is <= 50
		__base_classes : a list<str> containing all base classes defined
		    in the game
		__promoted_classes: a list<str> containing all promoted classes 
		    defined in the game
		__promotion_gains : a dict<(str, str), dict<Stat, int>> that 
		    maps a tuple of a base class and a promoted class onto a 
		    dictionary containing the stat increases/decreases a 
		    character is affected by when promoting from the base class 
		    to the promoted class
		"""
		def __init__(self, infile_name):
			"""Inits GameData object

			Reads game constraints from .csv file

			Args:
		        infile_name : a str defining the name of the file to read 
			    from
			"""
			self.__game_characters = {}
			self.__max_stats = {}
			self.__base_classes = []
			self.__promoted_classes = []
			self.__promotion_gains = {}
			infile = ''
			try:
				infile = open(infile_name, "r")
			except IOError:
				# TODO: Make a better error handler
				return

			state = 0

			for line in infile:
				# separators
				# Character,Class,HP GR,Str GR,Mag GR,Skl GR,Spd GR,
				# Lck GR,Def GR,Res GR,
				#  - characters, their classes, and growth rates
				# Class_Max,HP,Str,Mag,Skl,Spd,Lck,Def,Res,, 
				# - max stats for specific classes
				# Base_Class,Promoted_Class,HP,Str,Mag,Skl,Spd,Def,Res,, 
				# - promotion gains
				# Character_Bases,Class,Level,HP,Str,Mag,Skl,Spd,Lck,
				# Def,Res - character base stats
				array = line.split(',')
				if (array[0] == 'Character'):
					state = 1
					continue
				elif (array[0] == 'Class_Max'):
					state = 2
					continue
				elif (array[0] == 'Base_Class'):
					state = 3
					continue
				elif (array[0] == 'Character_Bases'):
					state = 4
					continue

				if (state == 1):
					# start reading in characters and growth rates
					# name, class, HP, Str, Mag, Skl, Spd, Lck, Def, 
					# Res
					if array[0] in self.__game_characters.keys():
						self.__game_characters[array[0]].add_class_and_growth_rates(
							array[1],
							StatEnum.stat_dict(array[2:]))
					else:
						new_char = CharacterData(array[0])
						new_char.add_class_and_growth_rates(
							array[1],
							StatEnum.stat_dict(array[2:]))
						self.__game_characters[array[0]] = new_char
				elif (state == 2):
					# start reading in max stats for specific classes
					class_name = array[0]
					stat_dict = StatEnum.stat_dict(array[1:])
					(self.__max_stats)[class_name] = stat_dict
				elif (state == 3):
					# start reading in promotion gains
					base_class_name = array[0]
					if (base_class_name not in self.__base_classes):
						self.__base_classes.append(
						        base_class_name)
					promo_class_name = array[1]
					if (promo_class_name not in self.__promoted_classes):
						self.__promoted_classes.append(promo_class_name)
					stat_dict = StatEnum.stat_dict(array[2:10])
					self.__promotion_gains[(base_class_name, promo_class_name)] = stat_dict
				elif (state == 4):
					game_class = array[1]
					level = int(array[2])
					stat_dict = StatEnum.stat_dict(array[3:11])
					initial_state = State(level, game_class, stat_dict)
					self.__game_characters[array[0]].add_initial_state(initial_state)

			infile.close()

	instance = None

	def __init__(self, infile_name):
		"""Inits GameData object

		Reads game constraints from .csv file

		Args:
		    infile_name : a str defining the name of the file to read 
			from
		"""
		GameData.instance = GameData.__GameData(infile_name)


	def get_local_variables(self):
		"""Retrieves all local variables of the class

		Args:

		Returns:
			An array of [__game_characters, __max_stas, __base_classes, __promoted_classes, __promotion_gains]
		"""

		return [self.instance.__game_characters, self.instance.__max_stats, self.instance.__base_classes, self.instance.__promoted_classes, self.instance.__promotion_gains]

	def get_character_data(self, name):
		"""Retrieves a CharacterData object with __name == name

		Args:
		    name : a str with the name of the character we wish to 
		        retrieve

		Returns:
		    CharacterData object from __game_characters with 
		        __name == name
		"""
		return self.instance.__game_characters[name]

	def max_stats(self, game_class):
		"""Retrieves max stats for a given class

		Args:
		    game_class : a str with the name of an in game class we want
		        the max_stats for

		Returns:
		    dict<Stat, int> describing the max value for each stat for a
			character with the in game class of game_class
		"""
		return self.instance.__max_stats[game_class]

	def promotion_gains(self, base_class, promoted_class):
		"""Retrieves the promotion gains/losses associated with 
		    promotion from base_class to promoted_class

		Args:
		    base_class : a str with name of the base class
		    promoted_class : a str with name of the class to promote to

		Returns:
		    a dict<Stat, int> describing gains/losses from a character
		    promoting from base_class to promoted_class if possible
		"""
		return self.instance.__promotion_gains[(base_class, promoted_class)]

	def is_base_class(self, game_class):
		"""Determines if a class is a valid base class

		Args:
		    game_class : a str with name of a class

		Returns:
		    a bool describing whether game_class is in __base_classes
		"""
		if((game_class == 'Lord') or (game_class == 'Ballistician') or 
			(game_class == 'Chameleon') or (game_class == 'Manakete') or 
			(game_class == 'Thief')):
			return True
		return game_class in self.instance.__base_classes

	def is_promoted_class(self, game_class):
		"""Determines if a class is a valid promoted classe

		Args:
		    game_class : a str with name of a class

		Returns:
		    a bool describing whether game_class is in __promoted_classes
		"""
		return game_class in self.instance.__promoted_classes
