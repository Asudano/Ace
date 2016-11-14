from tkinter import *
from State import State
from StatEnum import Stat
from UserLogs import UserLogs
from GameData import GameData


class UpdateUi(Frame):
	"""Manages the character update scren
        """

	def __init__(self, user_logs, master=None):
		"""inits a new UpdateUi object to handle updating of a 
		CharacterInstance with a new state

		Args:
		    user_logs : the UserLogs singleton
		    master : tkinter.widget identifying the parent widget
		"""
		Frame.__init__(self, master)
		self.__char_attribute = []
		self.user_logs = user_logs
		self.create_widgets()

	def update_f(self):
		"""Updates and existing CharacterInstance
		
		Updates an existing character with a new state given by then user
		"""
		# 1. select character instance from UserLogs
		char_instance = self.user_logs.get_char_instance(str(self.__char_attribute[0].get()))

		# 2. Create new State
		stat_dict = {Stat.HP: int(self.__char_attribute[3].get()),
		             Stat.Str: int(self.__char_attribute[4].get()),
		             Stat.Mag: int(self.__char_attribute[5].get()), 
		             Stat.Skl: int(self.__char_attribute[6].get()),
		             Stat.Spd: int(self.__char_attribute[7].get()), 
		             Stat.Lck: int(self.__char_attribute[8].get()),
		             Stat.Def: int(self.__char_attribute[9].get()),
		             Stat.Res: int(self.__char_attribute[10].get()), }
		state = State(int(self.__char_attribute[2].get()), 
		              str(self.__char_attribute[1].get()), stat_dict)

		# 3. Add state to character instance
		char_instance.add_new_state(state)

		# 4. Add character Instance to user logs
		self.user_logs.update_logs(char_instance)

	def create_labels(self, character_name, grideN):
		"""Creates a label for a UI element

		Args:
		    character_name : str that specifies the name of the character
		    gridN : int that specifies the number of rows
		"""
		master = self.master
		char_name = Label(master, text=character_name)
		char_name.grid(row=grideN, column=0, columnspan=1, sticky=E + W)

	def create_textbox(self, attribute, gridN):
		"""Creates a text box element

		Args:
		    attribute : str that specifies the attribute for text box
		    gridN : int that specifies number of rows
		"""
		master = self.master
		textbox = Entry(master)
		textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
		textbox.insert(0, attribute)
		self.__char_attribute.append(textbox)#

	def create_widgets(self):
		"""Creates display elements
		"""
		master = self.master

		self.create_labels("Character Name", 0)
		#self.create_textbox("", 0)
		name = StringVar(master)
		list_of_names = self.user_logs.get_all_names()
		name.set(list_of_names[0])
		name_drop = OptionMenu(
			master, 
			name, 
			*list_of_names)
		name_drop.grid(row=0, column=1, columnspan=2, sticky=E + W)
		self.__char_attribute.append(name)

		self.create_labels("Class", 1)
		self.create_textbox("", 1)

		self.create_labels("Level", 2)
		self.create_textbox("", 2)

		self.create_labels("HP", 3)
		self.create_textbox("", 3)

		self.create_labels("Str", 4)
		self.create_textbox("", 4)

		self.create_labels("Mag", 5)
		self.create_textbox("", 5)

		self.create_labels("Skl", 6)
		self.create_textbox("", 6)

		self.create_labels("Spd", 7)
		self.create_textbox("", 7)

		self.create_labels("Lck", 8)
		self.create_textbox("", 8)

		self.create_labels("Def", 9)
		self.create_textbox("", 9)

		self.create_labels("Res", 10)
		self.create_textbox("", 10)

		update = Button(master, text="update", command=self.update_f)
		update.grid(row=11, column=0, columnspan=2, sticky=E + W)

if __name__ == "__main__":
	root = Tk()
	game_data = GameData("shadow_dragon.csv")
	user_logs = UserLogs("user_log.csv", game_data)
	app = UpdateUi(user_logs, master=root)
	app.mainloop()
	root.destroy()
