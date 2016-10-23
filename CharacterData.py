class CharacterData(object):
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
	
	name = ""
	game_class_options = []
	growth_rate_class = {}
	base_stats = {}
	base_class = ""
	base_level = 0
	
	class GrowthRates(object):
		"""
		GrowthRates wrap a dictioanry of individual growth rates for a given
			character/class combination

		Attributes:
			rates: A dictionary mapping stats onto growth rates
		"""
		rates = {}

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

	def __init__(self, array):
		"""Inits CharacterData with name, game_class_options and 
		growth_rate_class"""
		self.name = array[0]
		self.game_class_options = []
		self.growth_rate_class = {}
		self.base_stats = {}
		self.base_class = ""
		self.addClassAndGrowthRates(array)
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
		
	def getName(self):
		return self.name
		
	def getBaseLevel(self):
		return self.base_level
		
	def getBaseStats(self):
		return self.base_stats
		
	def getGrowthRates(self, class_name):
		return self.growth_rate_class[class_name].getRates()
		
	def setBaseClassAndStats(self, array):
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
		
	def addClassAndGrowthRates(self, array):
		self.game_class_options.append(array[1])
		gr = self.GrowthRates(array)
		self.growth_rate_class[array[1]] = gr		
		pass
		
		
