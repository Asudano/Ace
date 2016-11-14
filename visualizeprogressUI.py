from tkinter import *
from StatEnum import *


class VisualizeProgressUi(Frame):
	"""Manages the progress visualization screen
	"""

	def __init__(self, user_logs, game_data, master=None):
		"""inits a new VisualizeProgressUi object to show a 
		CharacterInstance's progress throughout multiple states

		Args:
			master : tkinter.widget identifying the parent widget
		"""
		Frame.__init__(self, master)
		self.char_attribute = []
		self.user_logs = user_logs
		self.game_data = game_data
		self.create_widgets()

	def visualize_f(self):
		"""Creates a graph for character growth visualization
		
		Creats a grapoh of the CharacterInstance's States over time vs.
		predicted States
		"""
		master = self.master
		char_name = str(self.char_attribute[0].get())
		stat = str_to_stat(str(self.char_attribute[1].get()))
		char_inst = self.user_logs.get_char_instance(char_name)
		(actual, expected) = self.user_logs.visualize_progress(char_inst, stat, self.game_data)
		for i in range(0,len(actual)):
			stat1 = Label(master, text=actual[i])
			stat1.grid(row=4+i, column=0, columnspan=1)
			stat2 = Label(master, text=expected[i])
			stat2.grid(row=4+i, column=1, columnspan=2)		
		pass

	def create_labels(self, character_name, gridN):
		"""Creates labels for UI elements

		Args:
			character_name : str that specifies the name of the character
			gridN : int that specifies the number of rows
		"""
		master = self.master
		char_name = Label(master, text=character_name)
		char_name.grid(row=gridN, column=0, columnspan=1, sticky=E + W)

	def create_textbox(self, attribute, gridN):
		"""Creates a text box element

		Args:
			attribute : str that specifies the attribute for text box
			gridN : int that specifies number of rows
		"""
		master = self.master
		name = StringVar(master)
		list_of_names = self.user_logs.get_all_names()
		name.set(list_of_names[0])
		name_drop = OptionMenu(
			master, 
			name, 
			*list_of_names)
		name_drop.grid(row=0, column=1, columnspan=2, sticky=E + W)
		self.char_attribute.append(name)

	def create_widgets(self):
		"""Creates display elements
		"""
		master = self.master

		self.create_labels("Character Name", 0)
		self.create_textbox("", 0)

		stat_var = StringVar(master)
		stat_var.set("HP")
		stat_var_drop = OptionMenu(
			master, 
			stat_var, 
			"HP", 
			"Str", 
			"Mag", 
			"Skl", 
			"Spd", 
			"Lck", 
			"Def", 
			"Res")
		stat_var_drop.grid(row=1, column=0, columnspan=2, sticky=E + W)
		self.char_attribute.append(stat_var)

		visualize = Button(master, text="Visualize", command=self.visualize_f)
		visualize.grid(row=2, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
	root = Tk()
	app = VisualizeProgressUi(master=root)
	app.mainloop()
	root.destroy()
