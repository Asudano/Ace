from StatEnum import Stat
from GameData import GameData
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
		
		self.log_file = infile_name
		try:
			infile = open(infile_name, "r")
		except IOError:
			#TODO: Make a better error handler
			#print("ERROR")
			return (game_characters, 
		                max_stats, 
		                promotion_gains, 
		                base_classes, 
		                promoted_classes)	
		"""
		
		__level : An int describing the character's current level
		__game_class : A str describing the character's current in game class
		__stats : A dict<Stat, float> mapping the elements of the Stat enum onto 
			the values the character currently has for each stat
		
		"""
		write_line = ""
		count = 0
		name = ""
		inst_class = ""
		inst_level = 0
		inst_stats = {}
		
		#dict<Stat, float> 		
		
		for line in infile:
                        
			if count % 9 == 0:
				name = line
				#name
			elif count % 9 == 1:
				#class
				inst_class = line
			elif count % 9 == 2:
				#level
				inst_level = line
			elif count % 9 == 3:
				#stats
				inst_stats[Stat.HP] = float(line)
			elif count % 9 == 4:
				inst_stats[Stat.Str] = float(line)
			elif count % 9 == 5:
				inst_stats[Stat.Mag] = float(line)
			elif count % 9 == 6:
				inst_stats[Stat.Skl] = float(line)
			elif count % 9 == 7:
				inst_stats[Stat.Spd] = float(line)
			elif count % 9 == 8:
				inst_stats[Stat.Def] = float(line)
			elif count % 9 == 0:
				inst_stats[Stat.Res] = float(line)
				new_state = State(inst_level, inst_class, inst_stats)
				c_data = CharacterData.get_character_data(name)
				c_inst = CharacterInstance(c_data, new_state)
				self.character_instances.append(c_inst)
				name = ""
				inst_class = ""
				inst_level = 0
				inst_stats = {}				
			count += 1
			
			
						

	def update_logs(new_character_instance):
		"""Updates logs with new CharacterInstance

		Updates UserLogs object and writes data to __log_file as a 
			CharacterInstance object is updated
		"""

		try:
			outfile = open(self.log_file, "a")
		except IOError:
			#TODO: Make a better error handler
			#print("ERROR")
			return (game_characters, 
		                max_stats, 
		                promotion_gains, 
		                base_classes, 
		                promoted_classes)
	
		# write name, characterdata, states
		
		new_name = new_character_instance.character_data.get_name()
		new_level = (new_character_instance.states)[0].level
		outfile.write(new_name)
		outfile.write(new_level)
		
		new_stats = (new_character_instance.states)[0].stats
		keys = new_stats.keys()		
		count = 0
		for stats_values in new_stats.values():
			outfile.write(keys[count])
			outfile.write(stats_values)
			count += 1

		
		
	def sort_by_stat_sum(char_1, char_2):
		"""Comparator for list of CharacterInstances
		
		Sorts CharacterInstances by the sum of their most recent stats, 
			in ascending order
			
		Args:
			char_1 : first CharacterInstance to compare
			char_2 : second CharacterInstance to compare
			
		Returns:
			-1 if char_1 has a lower stat sum than char_2
			0 if char_1 has the same stat sum as char_2
			1 if char_1 has a higher stat sum than char_2
		"""
		stats_1 = char_1.get_current_state().stats
		stats_2 = char_2.get_current_state().stats
		sum_1 = 0
		sum_2 = 0
		for stat in stats_1:
			sum_1 += stats_1[stat]
		for stat in stats_2:
			sum_2 += stats_2[stat]
		if(sum_1 < sum_2):
			return -1
		elif(sum_1 > sum_2):
			return 1
		return 0
		
	def recommend_team(num_characters):
		"""Recommends a team for the user
		
		Uses sorted list of CharacterInstances to determine characters with 
			highest stat sum, chooses 12 of them
			
		Args:
			num_characters : number of CharacterInstances to choose
			
		Returns: List of top num_characters CharacterInstances to use		
		"""
		sorted_characters = sorted(self.__character_instances, cmp=sort_by_stat_sum)
		best_characters = []
		for i in range(0,num_characters):
			best_characters.append(sorted_characters[i])
		return best_characters		
