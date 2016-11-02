from CharacterData import CharacterData
from State import State
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
		self.game_characters = []
		self.max_stats = {}
		self.base_classes = []
		self.promoted_classes = []
		self.promotion_gains = {}		
		return self.read_infile(infile_name)
		
	def read_infile(self, filepath):
		"""
			MOVED INTO GAMEDATA CLASS
		"""
		state = 0

		
		try:
			infile = open(filepath, "r")
		except IOError:
			#TODO: Make a better error handler
			#print("ERROR")
			return (game_characters, 
				max_stats, 
				promotion_gains, 
				base_classes, 
				promoted_classes)
	
		for line in infile:
			# separators
			# Character,Class,HP GR,Str GR,Mag GR,Skl GR,Spd GR,Lck GR,Def GR,Res GR, - characters, their classes, and growth rates
			# Class_Max,HP,Str,Mag,Skl,Spd,Lck,Def,Res,, - max stats for specific classes
			# Base_Class,Promoted_Class,HP,Str,Mag,Skl,Spd,Def,Res,, - promotion gains
			# Character_Bases,Class,Level,HP,Str,Mag,Skl,Spd,Lck,Def,Res - character base stats
			array = line.split(',')
			if(array[0] == 'Character'):
				state = 1
				continue
			elif(array[0] == 'Class_Max'):
				state = 2
				continue
			elif(array[0] == 'Base_Class'):
				state = 3
				continue
			elif(array[0] == 'Character_Bases'):
				state = 4
				continue
				
			if(state == 1):
				# start reading in characters and growth rates
				index = -1
				count = 0
				for char in self.game_characters:
					if(char.get_name() == array[0]):
						index = count
					count += 1
				# if not, add it
				if(index == -1):
					new_char = CharacterData(array[0])
					new_char.add_class_and_growth_rates(array[1:10])
					self.game_characters.append(new_char)
					
				# otherwise edit it
				else:
					self.game_characters[index].add_class_and_growth_rates(array[1:10])
			elif(state == 2):
				# start reading in max stats for specific classes
				class_name = array[0]
				stat_list = {}
				stat_list['HP'] = int(array[1])
				stat_list['Str'] = int(array[2])
				stat_list['Mag'] = int(array[3])
				stat_list['Skl'] = int(array[4])
				stat_list['Spd'] = int(array[5])
				stat_list['Lck'] = int(array[6])
				stat_list['Def'] = int(array[7])
				stat_list['Res'] = int(array[8])
				(self.max_stats)[class_name] = stat_list
			elif(state == 3):
				# start reading in promotion gains
				base_class_name = array[0]
				if(base_class_name not in self.base_classes):
					self.base_classes.append(base_class_name)
				promo_class_name = array[1]
				if(promo_class_name not in self.promoted_classes):
					self.promoted_classes.append(promo_class_name)
				stat_list = {}
				stat_list['HP'] = int(array[2])
				stat_list['Str'] = int(array[3])
				stat_list['Mag'] = int(array[4])
				stat_list['Skl'] = int(array[5])
				stat_list['Spd'] = int(array[6])
				stat_list['Def'] = int(array[7])
				stat_list['Res'] = int(array[8])
				promo_gains = {}
				promo_gains[promo_class_name] = stat_list
				self.promotion_gains[base_class_name] = promo_gains
			elif(state == 4):
				# start reading in character base stats
				index = -1
				count = 0
				for char in self.game_characters:
					if(char.get_name() == array[0]):
						index = count
					count += 1
				if (index > -1):
					level = int(array[2])
					game_class = array[1]
					temp = array[3:11]
					j = 0
					while (j < len(temp)):
						temp[j] = int(temp[j])
						j += 1
					base_st = {}
					base_st['HP'] = int(array[3])
					base_st['Str'] = int(array[4])
					base_st['Mag'] = int(array[5])
					base_st['Skl'] = int(array[6])
					base_st['Spd'] = int(array[7])
					base_st['Lck'] = int(array[8])
					base_st['Def'] = int(array[9])
					base_st['Res'] = int(array[10])					
					b_state = State(level, game_class, base_st)
					self.game_characters[index].add_initial_state(b_state)

				
		infile.close()
		

		
		#return (game_characters, max_stats, promotion_gains, base_classes, promoted_classes)


	def get_character_data(self, name):
		"""Retrieves a CharacterData object with __name == name

		Args:
			name : a str with the name of the character we wish to retrieve

		Returns:
			CharacterData object from __game_characters with __name == name
		"""
		

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
		if not(game_class in self.base_classes):
			return false
		return true

	def is_promoted_class(self, game_class):
		"""Determines if a class is a valid promoted class

		Args:
			game_class : a str with name of a class

		Returns:
			a bool describing whether game_class is in __promoted_classes
		"""