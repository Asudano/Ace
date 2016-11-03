from tkinter import *


class VisualizeProgressUi(Frame):
    """Manages the progress visualization screen
    """

    def __init__(self, master=None):
        """inits a new VisualizeProgressUi object to show a 
        CharacterInstance's progress throughout multiple states

        Args:
            master : tkinter.widget identifying the parent widget
        """
        Frame.__init__(self, master)
        self.char_attribute = []
        self.create_widgets()

    def visualize_f(self):
        """Creates a graph for character growth visualization
        
        Creats a grapoh of the CharacterInstance's Statses over time vs.
        predicted States
        """
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
        self.char_attribute.append(char_name)

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

        visualize = Button(master, text="Visualize", command=self.visualize_f)
        visualize.grid(row=2, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
    root = Tk()
    app = VisualizeProgressUi(master=root)
    app.mainloop()
    root.destroy()
