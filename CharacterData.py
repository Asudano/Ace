class CharacterData(object):
	"""
	CharacterData contains constant values set by the game for a character

	Attributes:
		name: A string describing a character's name
		game_class_options: A list of strings describing the in game classes
			a character can choose from
		growth_rate_class: A dicitonary mapping class names (from 
			game_clas_options) onto GrowthRates objects  
	"""
	class GrowthRates(object):
		"""
		GrowthRates wrap a dictioanry of individual growth rates for a given
			character/class combination

		Attributes:
			rates: A dictionary mapping stats onto growth rates
		"""

		def __init__(self):
			"""Inits GrowthRates with rates"""
			pass

	def __init__(self):
		"""Inits CharacterData with name, game_class_options and 
		growth_rate_class"""
		pass