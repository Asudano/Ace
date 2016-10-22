class CharacterData(object):
	"""
	CharacterData contains constant values set by the game for a character

	Attributes:
		name: A string describing a character's name
		game_class_options: A list of strings describing the in game classes
			a character can choose from
		growth_rate_class: A dicitonary mapping class names (from 
			game_clas_options) onto GrowthRates objects  
		base_stats: A list of integers showing the character's base class stats
		base_class: The class this character is in when they join in the game
	"""
	
	name = ""
	game_class_options = []
	growth_rate_class = {}
	base_stats = []
	base_class = ""
	
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
			self.rates['HP'] = array[2]
			self.rates['Str'] = array[3]
			self.rates['Mag'] = array[4]
			self.rates['Skl'] = array[5]
			self.rates['Spd'] = array[6]
			self.rates['Lck'] = array[7]
			self.rates['Def'] = array[8]
			self.rates['Res'] = array[9]
			pass
			
		def printAllData(self):
			for key in self.rates:
				print(key)
				print(self.rates[key])
			pass

	def __init__(self, array):
		"""Inits CharacterData with name, game_class_options and 
		growth_rate_class"""
		self.name = array[0]
		self.game_class_options = []
		self.growth_rate_class = {}
		self.base_stats = []
		self.base_class = ""
		self.addClassAndGrowthRates(array)
		pass
		
	def printAllData(self):
		print('Name: ' + self.name)
		print('Base Class: ' + self.base_class)
		print('Base Stats: ')
		print(self.base_stats)
		''' BIG PROBLEM HERE, CAN'T FIGURE OUT SYNTAX '''
		for key in self.game_class_options:
			print(key)
			self.game_class_options[key].printAllData()
		
		print('\n')
		pass
		
	def getName(self):
		return self.name
		
	def setBaseClassAndStats(self, array):
		self.base_class = array[1]
		array[10] = array[10].strip()
		self.base_stats = array[2:11]
		pass	
		
	def addClassAndGrowthRates(self, array):
		self.game_class_options.append(array[1])
		gr = self.GrowthRates(array)
		self.growth_rate_class[array[1]] = gr		
		pass
		
		
