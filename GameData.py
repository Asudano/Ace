class GameData(object):
	"""
	GameData stores constraints defined by the game itself and not by the 
		Player.

	GameData is a singleton class that stores values that are read from a .csv 
		file and used to model characters in our tracker.

	Attributes:
		__game_characters : a list<CharacterData> containing all of the usable 
			characters in the game
		__max_stats : a dict<str, dict<Stat, int>> which defines a mapping 
			from a class name onto a mapping between the various stats defined 
			in the game and the maximum values a character of the define class 
			can have
			Ex: __max_stats["A"][HP] = 50 means that a character of class A can
				have an HP that is <= 50
		__base_classes : a list<str> containing all base classes defined in the
			game
		__promoted_classes: a list<str> containing all promoted classes defined
			in the game
		__promotion_gains : a dict<(str, str), dict<Stat, int>> that maps a 
			tuple of a base class and a promoted class onto a dictionary
			containing the stat increases/decreases a character is affected by
			when promoting from the base class to the promoted class
	"""

	def __init__(self, infile_name):
		"""Inits GameData object 
			
		Reads game constraints from .csv file

		Args:
			infile_name : a str defining the name of the file to read from

		Returns:
			GameData object
		"""
		pass

	def get_character_data(self, name):
		"""Retrieves a CharacterData object with __name == name

		Args:
			name : a str with the name of the character we wish to retrieve

		Returns:
			CharacterData object from __game_characters with __name == name
		"""
		pass

	def max_stats(self, game_class):
		"""Retrieves max stats for a given class

		Args:
			game_class : a str with the name of an in game class we want the 
				max_stats for

		Returns:
			dict<Stat, int> describing the max value for each stat for a 
				character with the in game class of game_class
		"""
		pass

	def promotion_gains(self, base_class, promoted_Class):
		"""Retrieves the promotion gains/losses associated with promotion from
			base_class to promoted_class

		Args:
			base_class : a str with name of the base class
			promoted_class : a str with name of the class to promote to

		Returns:
			a dict<a, int> describing gains/losses from a character
				promoting from base_class to promoted_class if possible
		"""
		pass

	def is_base_class(self, game_class):
		"""Determines if a class is a valid base class

		Args:
			game_class : a str with name of a class

		Returns:
			a bool describing whether game_class is in __base_classes
		"""
		pass

	def is_promoted_class(self, game_class):
		"""Determines if a class is a valid promoted class

		Args:
			game_class : a str with name of a class

		Returns:
			a bool describing whether game_class is in __promoted_classes
		"""