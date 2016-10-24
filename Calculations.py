from CharacterData import CharacterData

def math_model(all_characters, max_stats, promotion_gains, base_classes, promoted_classes, char, level, class_name):
	'''
		all_characters: list of all the CharacterData objects
		max_stats: dictionary mapping name of class to list of max stats
		promotion_gains: nested dictionary {base_class: {promoted_class: stat gains/losses}}
		char: specific character to do math modelling for
		level: desired level for the character
		class_name: the class of the character
	'''
	
	expected_stats = []
	index = -1
	count = 0
	for character in all_characters:
		if(character.getName() == char):
			index = count
		count += 1
	if(index == -1):
		print('Error') #@TODO: some better error messaging here
	curr_char = all_characters[index]
	
	# if character is in a base class
	if(class_name in base_classes):
		level_diff = level - int(curr_char.getBaseLevel())
		expected_stats = curr_char.getBaseStats()
		growth_rates = curr_char.getGrowthRates(class_name)		
		for stat in expected_stats:
			expected_stats[stat] = expected_stats[stat] + level_diff*(float(growth_rates[stat])/100)
	
	# if character is in a promoted class
	
	# deal with prepromotes
	if(curr_char.getBaseClass() in promoted_classes):
		level_diff = level - int(curr_char.getBaseLevel())
		expected_stats = curr_char.getBaseStats()
		growth_rates = curr_char.getGrowthRates(curr_char.getBaseClass())
		for stat in expected_stats:
			expected_stats[stat] = expected_stats[stat] + level_diff*(float(growth_rates[stat])/100)
			
	# non-prepromotes
	elif(class_name in promoted_classes):
		base_class = curr_char.getBaseClass()
					
		# add up levels to base level 20
		level_diff = 20 - int(curr_char.getBaseLevel())
		base_expected_stats = curr_char.getBaseStats()
		base_growth_rates = curr_char.getGrowthRates(base_class)
		for stat in base_expected_stats:
			base_expected_stats[stat] = base_expected_stats[stat] + level_diff*(float(base_growth_rates[stat])/100)
		expected_stats = base_expected_stats
		
		# add promotion gains
		stat_dict = promotion_gains[base_class][class_name]
		for stat in stat_dict:
			expected_stats[stat] = expected_stats[stat] + stat_dict[stat]
			
		# now do same for levels in promoted class
		level_diff = level - 1
		growth_rates = curr_char.getGrowthRates(class_name)
		for stat in expected_stats:
			expected_stats[stat] = expected_stats[stat] + level_diff*(float(growth_rates[stat])/100)
			
	# make sure expected stats are not over the max stats for that class
	for stat in expected_stats:
		if(expected_stats[stat] > max_stats[class_name][stat]):
			expected_stats[stat] = max_stats[class_name][stat]
			
	print(expected_stats)
