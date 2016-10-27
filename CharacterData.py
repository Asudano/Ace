class CharacterData(object):

	"""
	CharacterData contains constant values set by the game for a character

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

		def __init__(self, stat_values):
			"""Inits GrowthRates with rates

			Args:
				stat_values : a list<float> containing the values associated
					with Stats in the following order
					[HP, Str, Mag, Skl, Spd, Lck, Def, Res]

			Returns:
				GrowthRates object
			"""
			pass

		@property
		def rates(self):
			return self.__rates

		if False:
			"""
			GrowthRates wrap a dictioanry of individual growth rates for a given
				character/class combination

			Attributes:
				__rates: A dictionary mapping stats onto growth rates
			"""
			__rates = {}

			def __init__(self, array):
				"""Inits GrowthRates with rates"""
				self.rates = {}
				self.rates['HP'] = int(array[2])
				self.rates['Str'] = int(array[3])
				self.rates['Mag'] = int(array[4])
				self.rates['Skl'] = int(array[5])
				self.rates['Spd'] = int(array[6])
				self.rates['Lck'] = int(array[7])
				self.rates['Def'] = int(array[8])
				self.rates['Res'] = int(array[9])
				pass
				
			def __str__(self):
				"""Creates string for GrowthRates object"""
				rt_str = ''
				for key in self.rates:
					rt_str += '\t' + str(key) + ' : '
					rt_str += str(self.rates[key]) + '\n'
				return rt_str
				
			def getRates(self):
				return self.rates


	def __init__(self, name):
		"""Inits a CharacterData object 

		Args:
			name : a str of the character's name

		Returns:
			CharcterData object
		"""
		pass

	def add_initial_state(self, state):
		"""Sets the initial state for CharacterData

		Args:
			state : State object for character's initial state
		"""
		pass

	def get_growth_rate(self, game_class):
		"""Retrieves GrowthRates object for given in game class

		Args:
			game_class : a str describing an in game class

		Returns:
			GrowthRates object associated with the desired in game class
		"""
		pass

	def predict_state(self, level, game_class):
		"""Creates a state for the average stats for a character with a given 
			in game class and level

		Args:
			level : an int representing an in game level
			game_class: a str describing an in game class

		Returns:
			A state object representing the average for this character at the
				given class and level.
		"""
		pass

	if False:
		"""
		CharacterData contains constant values set by the game for a character

		Attributes:
			name: A string describing a character's name
			game_class_options: A list of strings describing the in game classes
				a character can choose from
			growth_rate_class: A dicitonary mapping class names (from 
				game_clas_options) onto GrowthRates objects  
			base_stats: A dictionary mapping stat names to the character's base class stats
			base_class: The class this character is in when they join in the game
		"""		

		def __init__(self, array):
			"""Inits CharacterData with name, game_class_options and 
			growth_rate_class"""
			self.name = array[0]
			self.game_class_options = []
			self.growth_rate_class = {}
			self.base_stats = {}
			self.base_class = ""
			self.add_class_and_growth_rates(array)
			pass
			
		def __str__(self):
			"""Creates string for CharacterData object"""
			rt_str = ''
			rt_str += 'Name: ' + str(self.name) + '\n'
			rt_str += 'Base Level: ' + str(self.base_level) + '\n'
			rt_str += 'Base Class: ' + str(self.base_class) + '\n'
			rt_str += str(self.base_stats) + '\n'
			for key in self.game_class_options:
				rt_str += key + '\n'
				rt_str += str(self.growth_rate_class[key]) + '\n'
			rt_str += '\n'
			return rt_str
			
		def get_name(self):
			return self.name
			
		def get_base_level(self):
			return self.base_level
			
		def get_base_stats(self):
			return self.base_stats
		
		def get_base_class(self):
			return self.base_class
			
		def get_growth_rates(self, class_name):
			return self.growth_rate_class[class_name].get_rates()
			
		def set_base_class_and_stats(self, array):
			self.base_class = array[1]
			self.base_level = array[2]
			array[10] = array[10].strip()
			self.base_stats['HP'] = int(array[3])
			self.base_stats['Str'] = int(array[4])
			self.base_stats['Mag'] = int(array[5])
			self.base_stats['Skl'] = int(array[6])
			self.base_stats['Spd'] = int(array[7])
			self.base_stats['Lck'] = int(array[8])
			self.base_stats['Def'] = int(array[9])
			self.base_stats['Res'] = int(array[10])
			pass	
			
		def add_class_and_growth_rates(self, array):
			self.game_class_options.append(array[1])
			gr = self.GrowthRates(array)
			self.growth_rate_class[array[1]] = gr		
			pass
			
		
