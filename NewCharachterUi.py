from tkinter import *
from GameData import GameData
from State import State
from StatEnum import Stat
from CharacterInstance import CharacterInstance
from UserLogs import UserLogs


class NewCharacterUi(Frame):

	"""
		NewCharacterUi manages the New Character creation screen

		Attributes:
				__char_attribute : a list<str> that contains the entry objects
					to be referency when creating a new character.
				__game_data : the GameData singleton
				__user_logs : the UserLogs singleton
	"""

	def __init__(self, game_data, user_logs, master=None):
		"""
			inits a new NewCharacterUi object to add a new Character to user's saved CharacterInstances

			 Args:
			 	game_data : the GameData singleton
			 	user_logs : the UserLogs singleton
			 	master : tkinter.widget identifying the parent widget
		"""
		Frame.__init__(self, master)
		self.__char_attribute = []
		self.create_widgets()
		self.__game_data = game_data
		self.__user_logs = user_logs

	def create(self):
		"""
			creates a new CharacterInstance and an initial state based on user data
		"""
		character_data = self.__game_data.get_character_data(str(self.__char_attribute[0].get()))
		stat_dict = {Stat.HP: int(self.__char_attribute[3].get()), Stat.Str: int(self.__char_attribute[4].get()),
					 Stat.Mag: int(self.__char_attribute[5].get()), Stat.Skl: int(self.__char_attribute[6].get()),
					 Stat.Spd: int(self.__char_attribute[7].get()), Stat.Lck: int(self.__char_attribute[8].get()),
					 Stat.Def: int(self.__char_attribute[9].get()), Stat.Res: int(self.__char_attribute[10].get()), }
		state = State(int(self.__char_attribute[2].get()), str(self.__char_attribute[1].get()), stat_dict)
		char_inst = CharacterInstance(character_data, state)
		self.__user_logs.add_character_instance(char_inst)
		self.__user_logs.update_logs(char_inst)

	def create_labels(self, character_name, gridN):
		"""
			create_labels creates a label for a UI element

			Args:
				character_name : str that specifies the name of the character
				gridN : int that specifies the row to create the label at
		"""
		master = self.master
		char_name = Label(master, text=character_name)
		char_name.grid(row=gridN, column=0, columnspan=1, sticky=E + W)

	def create_text_box(self, attribute, gridN):
		"""
			create_textbox creates a text box element

			Args:
				attribute : str that specifies the attribute for text box
				gridN : int that specifies the row to create the label at
		"""
		master = self.master
		textbox = Entry(master)
		textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
		textbox.insert(0, attribute)
		self.__char_attribute.append(textbox)

	def create_widgets(self):
		"""
			create_widgets creates display elements for update screen
		"""
		master = self.master

		self.create_labels("Character Name", 0)
		self.create_text_box("", 0)

		self.create_labels("Class", 1)
		self.create_text_box("", 1)

		self.create_labels("Level", 2)
		self.create_text_box("", 2)

		self.create_labels("HP", 3)
		self.create_text_box("", 3)

		self.create_labels("Str", 4)
		self.create_text_box("", 4)

		self.create_labels("Mag", 5)
		self.create_text_box("", 5)

		self.create_labels("Skl", 6)
		self.create_text_box("", 6)

		self.create_labels("Spd", 7)
		self.create_text_box("", 7)

		self.create_labels("Lck", 8)
		self.create_text_box("", 8)

		self.create_labels("Def", 9)
		self.create_text_box("", 9)

		self.create_labels("Res", 10)
		self.create_text_box("", 10)

		level_up_character = Button(master, text="Create", command=self.create)
		level_up_character.grid(row=11, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
	root = Tk()
	game_data = GameData("shadow_dragon.csv")
	user_logs = UserLogs("log.csv")
	app = NewCharacterUi(game_data, user_logs, master=root)
	app.mainloop()
	root.destroy()
