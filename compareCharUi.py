from tkinter import *
from UserLogs import UserLogs
from StatEnum import Stat
from GameData import GameData


class CompareCharUi(Frame):
	"""Manages the UI for the character comparison screen.
	"""

	def __init__(self, user_logs, index=0, master=None):
		"""inits a new CompareCharUi object to compare two
		user-specified characters
		Args:
			user_logs : UserLogs variable containing user data
			master : tkinter.widget identifying the parent widget
		"""

		self.components = []
		self.index = index
		Frame.__init__(self, master)
		self.char_attribute = []
		self.user_logs = user_logs
		self.create_widgets()

	def create_labels(self, character_name, grid_n, col_n):
		"""Creates a label for a UI element

		Args:
            character_name : str that specifies the name of the
                character
            grid_n : int that specifies the number of rows
            col_n : int that specifies the number of columns
        """

		master = self.master
		char_name = Label(master, text=character_name)
		char_name.grid(row=grid_n, column=self.index + col_n, columnspan=1,
					   sticky=E + W)
		self.components.append(char_name)

	def create_text_box(self, attribute, grid_n):
		"""Creates a text box element

        Args:
            attribute : str that specifies the attribute for text box
            grid_n : int that specifies number of rows
        """

		master = self.master
		textbox = Entry(master)
		textbox.grid(row=grid_n, column=self.index + 1, columnspan=1, 
			sticky=E + W)
		textbox.insert(0, attribute)
		self.char_attribute.append(textbox)
		self.components.append(textbox)

	def compare_f(self):
		"""Shows the stats of two different characters for comparison
        """
		character_1 = self.user_logs.get_char_instance(
			str(self.char_attribute[0].get()))
		character_2 = self.user_logs.get_char_instance(
			str(self.char_attribute[1].get()))
		curr_state1 = character_1.get_current_state()
		curr_state2 = character_2.get_current_state()

		master = self.master

		# names
		self.create_labels(self.char_attribute[0].get(), 4, 0)
		self.create_labels(self.char_attribute[1].get(), 4, 1)
		# HP
		self.create_labels(curr_state1.get_stat_value(Stat.HP), 5, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.HP), 5, 1)
		# Str
		self.create_labels(curr_state1.get_stat_value(Stat.Str), 6, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Str), 6, 1)
		# Mag
		self.create_labels(curr_state1.get_stat_value(Stat.Mag), 7, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Mag), 7, 1)
		# Skl
		self.create_labels(curr_state1.get_stat_value(Stat.Skl), 8, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Skl), 8, 1)
		# Spd
		self.create_labels(curr_state1.get_stat_value(Stat.Spd), 9, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Spd), 9, 1)
		# Lck
		self.create_labels(curr_state1.get_stat_value(Stat.Lck), 10, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Lck), 10, 1)
		# Def
		self.create_labels(curr_state1.get_stat_value(Stat.Def), 11, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Def), 11, 1)
		# Res
		self.create_labels(curr_state1.get_stat_value(Stat.Res), 12, 0)
		self.create_labels(curr_state2.get_stat_value(Stat.Res), 12, 1)

	def create_widgets(self):
		"""Creates display elements for update screen
        """
		master = self.master
		self.create_labels("Character 1 Name", 0, 0)
		name1 = StringVar(master)
		list_of_names = self.user_logs.get_all_names()
		name1.set(list_of_names[0])
		name1_drop = OptionMenu(
			master,
			name1,
			*list_of_names)
		name1_drop.grid(row=0, column=self.index+1, columnspan=2, sticky=E + W)
		self.char_attribute.append(name1)
		self.components.append(name1_drop)

		self.create_labels("Character 2 Name", 1, 0)
		name2 = StringVar(master)
		list_of_names = self.user_logs.get_all_names()
		name2.set(list_of_names[0])
		name2_drop = OptionMenu(
			master,
			name2,
			*list_of_names)
		name2_drop.grid(row=1, column=self.index+1, columnspan=2, sticky=E + W)
		self.char_attribute.append(name2)
		self.components.append(name2_drop)

		compare = Button(master, text="Compare", command=self.compare_f)
		compare.grid(row=2, column=self.index, columnspan=2, sticky=E + W)
		self.components.append(compare)

	def end(self):
		"""
        This function destroys all of the elements created
        """
		for i in self.components:
			i.destroy()


if __name__ == "__main__":
	root = Tk()
	user_logs = UserLogs("log.csv")
	app = CompareCharUi(user_logs, master=root)
	app.mainloop()


