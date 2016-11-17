class State(object):
	"""Stores the values of a character at the time a player logged

	Attributes:
	    __level : An int describing the character's current level
	    __game_class : A str describing the character's current in game 
	        class
	    __stats : A dict<Stat, float> mapping the elements of the Stat enum 
	        onto the values the character currently has for each stat
	"""
	
	__stats = {}
	
	def __init__(self, level, game_class, stats):
		"""Inits a State object
		
		Args:
		    level : an int describing the character's current level
		    game_class : a str describing the character's current in 
		        game class
		    stats : A dict<Stat, float> mapping the elements of the Stat
		        enum onto the values the character currently has for 
			each stat
		"""
		self.__level = int(level)
		self.__game_class = game_class
		self.stats = stats
		

	@property
	def level(self):
		return self.__level

	@property
	def game_class(self):
		return self.__game_class
	
	def get_stats(self):
		return self.stats

	def get_stat_value(self, stat):
		"""Retrieves the value associated with a Stat

		Args:
			stat: a Stat

		Returns:
			A float associated with the Stat value for this state
		"""
		if (stat in (self.stats).keys()):
			return ((self.stats)[stat])
		else:
			#TODO: error handle
			return self.stats
				

