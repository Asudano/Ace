from State import State


class CharacterData(object):
	"""Contains constant values set by the game for a character

	Attributes:
		__name : a str giving the character's name
		__game_class_options : a list<str> describing all in game classes this
			character can be
		__growth_rate_class: a dict<str, GrowthRate> mapping class names onto
			GrowthRate objects associated with that character/class combination
		__base_stats : a State describing the character's State when they are
			first encountered
	"""

	class GrowthRates(object):
		"""
		GrowthRates wraps a dictionary of growth rates for a given
			character/class combination

		Attributes:
			__rates : a dict<Stat, float> mapping stats onto their growth rates
		"""

		def __init__(self, rates):
			"""Inits GrowthRates with rates

			Args:
				rates : a dict<Stat, float> mapping stats onto their
					growth rates
			"""
			self.__rates = rates
		@property
		def rates(self):
			return self.__rates

	def __init__(self, name):
		"""Inits CharacterData with name

		Args:
			name : a str describing the name of the character
		"""

		self.__name = name
		self.__game_class_options = []
		self.__growth_rate_class = {}
		self.__base_stats = []

	@property
	def name(self):
		return self.__name

	@property
	def rates(self):
		return self.__rates

	def add_initial_state(self, state):
		"""Sets the initial state for CharacterData

		Args:
			state : State object for character's initial state
		"""
		self.__base_stats.append(state)

	def get_growth_rates(self, game_class):
		"""Retrieves GrowthRates object for given in game class

		Args:
			game_class : a str describing an in game class

		Returns:
			GrowthRates object associated with the desired in game class
		"""
		return self.__growth_rate_class[game_class].rates

	def predict_state(self, level, game_class, stat, game_data):
		"""Creates a state for the average stats for a character with a given
		in game class and level

		Args:
			level : an int representing an in game level
			game_class: a str describing an in game class
			stat : a str representing an in game stat
			game_data : the GameData singleton object

		Returns:
			A float representing the value for this character at the
			given class and level for the specified stat.
		"""
		# if character is in a base class
		if(game_data.is_base_class(game_class)):
			level_diff = level - int(self.base_level)
			expected_stat = self.get_base_stats()[stat]
			growth_rates = self.get_growth_rates(game_class)
			expected_stat = (expected_stat + level_diff*(float(growth_rates[stat])/100))
		
		# if character is in a promoted class
		
		# deal with prepromotes
		
		if(game_data.is_promoted_class(self.get_base_class())):
			level_diff = level - int(self.base_level)
			expected_stat = self.get_base_stats()[stat]
			growth_rates = self.get_growth_rates(self.get_base_class())
			expected_stat = (expected_stat + level_diff*(float(growth_rates[stat])/100))
				
		# non-prepromotes
		elif(game_data.is_promoted_class(game_class)):
			base_class = self.get_base_class()
						
			# add up levels to base level 20
			level_diff = 20 - int(self.base_level)
			base_expected_stat = self.get_base_stats()[stat]
			base_growth_rates = self.get_growth_rates(base_class)
			base_expected_stat = base_expected_stat + level_diff*(float(base_growth_rates[stat])/100)
			expected_stat = base_expected_stat
			
			# make sure base class isn't over max stats
			max_stats = game_data.max_stats(base_class)
			if(expected_stat > max_stats[stat]):
				expected_stat = max_stats[stat]
			
			# add promotion gains
			promotion_gains = game_data.promotion_gains(base_class, game_class)
			expected_stat = expected_stat + promotion_gains[stat]
				
			# now do same for levels in promoted class
			level_diff = level - 1
			growth_rates = self.get_growth_rates(game_class)
			expected_stat = (expected_stat + level_diff*(float(growth_rates[stat])/100))
		
		# make sure expected stats are not over the max stats for that class
		max_stats = game_data.max_stats(game_class)
		if(expected_stat > max_stats[stat]):
			expected_stat = max_stats[stat]
		return expected_stat

	@property
	def base_level(self):
		return (self.__base_stats)[0].level

	def get_base_stats(self):
		return (self.__base_stats)[0].get_stats()

	def get_base_value(self, stat):
		return (self.__base_stats)[0].get_stat_value(stat)

	def get_base_class(self):
		return (self.__base_stats)[0].game_class
		
	def get_game_class_options(self):
		return (self.__game_class_options)

	def add_class_and_growth_rates(self, game_class, rates):
		"""Adds a potential class and the associated growth rates to

		Args:
			game_class : a str describing a game class this character can
				become
			rates : a dict<Stat, float> mapping in game stats onto the
				growth rates for that stat when this character is of the 
				class specified by game_class
		"""
		self.__game_class_options.append(game_class)
		self.__growth_rate_class[game_class] = self.GrowthRates(rates)
