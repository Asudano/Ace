class CharacterInstance(object):
	"""
	CharacterInstance defines a character as it exists in a player's game

	CharacterInstance uses the information stored in CharacterData as well as 
	data logged by the player to describe their progress

	Attributes:
		__character_data: CharacterData object relevant to this character
		__states : a list<State> describing all of the states that have been 
			logged for this character
	"""
	def __init__(self, character_data, initial_state):
		"""Inits CharacterInstance with initial state values

		Args:
			character_data : the CharacterData object for the associated game 
				character
			initial_state : State object for the character at the time a player
				begins logging data about this character

		Returns:
			CharacterInstance object
		"""
		pass

	def add_new_state(self, state):
		"""Adds a new State to __states

		Args:
			state : A State object that has not yet been logged for this 
				charcter
		"""
		pass

	def get_current_state(self):
		"""Retrieves the most recent state object for this character

		Returns:
			State object with highest level/most recently logged
		"""
		pass

	def get_all_states(self):
		"""Retrieves all states for this character
	
		Returns:
			list<states> logged for this character
		"""
		return self.__states

	def get_predicted_states(self):
		"""Retrieves list of states for average values at logged levels
	
		Returns:
			list<states> created by CharacterData object for levels at which 
				there exists States for this charcter
		"""
		pass