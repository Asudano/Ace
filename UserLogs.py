from StatEnum import Stat
from State import State
from CharacterInstance import CharacterInstance

class UserLogs(object):
	"""Stores all the CharcterInstances that have been entered by the 
	    player

	UserLogs is a singleton class used to store the information logged by 
	    the player and stored in a .csv file.

	Attributes:
	    __character_instances : a dict<str, CharacterInstance> mapping 
	        names onto CharacterInstance objects
	    __log_file : file object describing location logs are stored
	"""
	def __init__(self, infile_name, game_data):
		"""Inits UserLogs object

		Reads player logs from .csv file

		Args:
		    infile_name : a str describing the filepath for the user log
		        file
		    game_data : the GameData singleton
		"""
		self.__character_instances = {}

		self.log_file = infile_name
		infile = ''
		try:
			infile = open(infile_name, "r")
		except IOError:
			# TODO: Make a better error handler
			print("ERROR")

		write_line = ""
		count = 0
		name = ""
		inst_class = ""
		inst_level = 0
		inst_stats = {}

		for line in infile:
			line = line.strip()
			if count % 11 == 0:
				# name
				name = line
			elif count % 11 == 1:
				# class
				inst_class = line
			elif count % 11 == 2:
				# level
				inst_level = line
			elif count % 11 == 3:
				# stats
				inst_stats[Stat.HP] = float(line)
			elif count % 11 == 4:
				inst_stats[Stat.Str] = float(line)
			elif count % 11 == 5:
				inst_stats[Stat.Mag] = float(line)
			elif count % 11 == 6:
				inst_stats[Stat.Skl] = float(line)
			elif count % 11 == 7:
				inst_stats[Stat.Spd] = float(line)
			elif count % 11 == 8:
				inst_stats[Stat.Lck] = float(line)
			elif count % 11 == 9:
				inst_stats[Stat.Def] = float(line)
			elif count % 11 == 10:
				inst_stats[Stat.Res] = float(line)
				new_state = State(
				        inst_level, 
				        inst_class, 
				        inst_stats)
				
				if name in self.__character_instances.keys():
					(self.
					 __character_instances[name].
					 add_new_state(new_state))
				else:
					c_data = game_data.get_character_data(
					        name)
					c_inst = CharacterInstance(
					        c_data, 
					        new_state)
					self.__character_instances[name] = c_inst

				name = ""
				inst_class = ""
				inst_level = 0
				inst_stats = {}
			count += 1
		
	def get_char_instance(self, name):
		"""Fetches the CharacterInstance associated with name
		
		Args:
		    name : a str describing the desired CharacterInstance
		
		Returns:
		    the CharacterInstance with the given name
		"""
		return self.__character_instances[name]
		
	def get_all_names(self):
		"""Returns list of all names of characters in CharacterInstances
		"""
		all_names = []
		for name in self.__character_instances:
			all_names.append(name)
		return all_names

	def update_logs(self, new_character_instance):
		"""Updates logs with new CharacterInstance
		
		Updates UserLogs object and writes data to __log_file as a
			CharacterInstance object is updated
		"""
		outfile = ''
		
		try:
			outfile = open(self.log_file, 'w')
		except IOError:
			# TODO: Make a better error handler
			return (game_characters,
					max_stats,
					promotion_gains,
					base_classes,
					promoted_classes)

		self.__character_instances[new_character_instance.name] = new_character_instance

		# print out all CharacterInstance objects with each state
		# name, class, level, stats
		for char in self.__character_instances:
			for state in self.__character_instances[char].get_all_states():
				outfile.write(
				        self.__character_instances[char].name
				        + '\n')
				outfile.write(state.game_class + '\n')
				outfile.write(str(state.level) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.HP)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Str)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Mag)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Skl)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Spd)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Lck)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Def)) + '\n')
				outfile.write(str(
				        state.get_stat_value(Stat.Res)) + '\n')
		
		outfile.close()

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
		
	def visualize_progress(self, char, stat, game_data):
		"""Fetches the actual values, expected values and levels for
		visualization of character progress

		Crawls through CharacterInstance's States to retrieve the expected 
			value, and actual value to be plotted against level

		Args:
			char : a CharacterInstance to be visualized
		# TODO: Replace with an element of the Stat enum
			stat : a str representing an in game stat
			game_data : GameData singleton

		Returns:
			actual : a list of values for the character's actual stat values
			expected: a list of values for the character's expected stat values
				at each state's level
			levels : a list of values for the character's levels at each state
		"""
		all_states = char.get_all_states()
		char_name = char.name
		actual = []
		expected = []
		levels = []
		for state in all_states:
			level = state.level
			game_class = state.game_class
			actual.append(state.get_stat_value(stat))
			game_character = game_data.get_character_data(char_name)
			expected.append(game_character.predict_state(level, game_class, stat, game_data))
			levels.append(level)
		return (actual,expected, levels)
		
	def recommend_team(self, num_characters):
		"""Recommends a team for the user

		Uses sorted list of CharacterInstances to determine characters 
		    with highest stat sum, chooses 12 of them

		Args:
		    num_characters : number of CharacterInstances to choose

		Returns: List of top num_characters name strings to use
		"""
		# TODO: clean up logic
		name_sum = {}
		for char in self.__character_instances:
			state = self.__character_instances[char].get_current_state()
			sum = 0
			sum += state.get_stat_value(Stat.HP)
			sum += state.get_stat_value(Stat.Str)
			sum += state.get_stat_value(Stat.Mag)
			sum += state.get_stat_value(Stat.Skl)
			sum += state.get_stat_value(Stat.Spd)
			sum += state.get_stat_value(Stat.Lck)
			sum += state.get_stat_value(Stat.Def)
			sum += state.get_stat_value(Stat.Res)
			name_sum[self.__character_instances[char].name] = sum
		all_sums = []
		for key in name_sum:
			all_sums.append(name_sum[key])
		all_sums.sort(reverse=True)
		best_characters = []
		for i in range(0, num_characters):
			# find character with current sum
			for key in name_sum:
				if(name_sum[key] == all_sums[i]):
					# add if not already there
					if(key not in best_characters):
						best_characters.append(key)
						break
		return best_characters