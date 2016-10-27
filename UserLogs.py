class UserLogs(object):
	"""
	UserLogs stores all the CharacterLogs that have been entered by the player

	UserLogs is a singleton class used to store the information logged by the 
		player and stored in a .csv file.

	Attributes:
		__character_instances : a list<CharacterInstance> storing all 
			CharacterInstance objects created by the user
		__log_file : file object describing location logs are stored
	"""
	def __init__(self, infile_name):
		"""Inits UserLogs object 
			
		Reads player logs from .csv file

		Args:
			infile_name : a str defining the name of the file to read from

		Returns:
			UserLogs object
		"""
		pass

	def update_logs(new_character_instance):
		"""Updates logs with new CharacterInstance

		Updates UserLogs object and writes data to __log_file as a 
			CharacterInstance object is updated
		"""
		pass