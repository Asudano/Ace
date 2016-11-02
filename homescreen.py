from tkinter import *
from NewCharachterUi import NewCharachterUI
from compareCharUi import compareCharUi
from suggestteamUi import suggestteamUi
from updateUi import updateUi
from visualizeprogressUI import visualizeprogressUi

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidgets()

    def myteam(self):
        print("Hello")
        # TODO: Create Level UP logic

    def browse_character_f(self):
        root = Tk()
        app = NewCharachterUI(master=root)
        app.mainloop()
        root.destroy()

    def compare_char_f(self):
        root = Tk()
        app = compareCharUi(master=root)
        app.mainloop()
        root.destroy()

    def suggest_team_f(self):
        root = Tk()
        app = suggestteamUi(master=root)
        app.mainloop()
        root.destroy()

    def update_f(self):
        root = Tk()
        app = updateUi(master=root)
        app.mainloop()
        root.destroy()

    def visualize_progress_f(self):
        root = Tk()
        app = visualizeprogressUi(master=root)
        app.mainloop()
        root.destroy()

    def createwidgets(self):
        master = self.master

        browse_character = Button(master, text="New Characters", command=self.browse_character_f)
        browse_character.grid(row=0, column=0, columnspan=2, sticky=E+W)

        compare_char = Button(master, text="Compare Character", command=self.compare_char_f)
        compare_char.grid(row=0, column=3, columnspan=2, sticky=E+W)

        suggest_team = Button(master, text="Suggest Team", command=self.suggest_team_f)
        suggest_team.grid(row=1, column=3, columnspan=2, sticky=E+W)

        update = Button(master, text="Update", command=self.update_f)
        update.grid(row=1, column=0, columnspan=2, sticky=E+W)

        visualize_progress = Button(master, text="Visualize Progress", command=self.visualize_progress_f)
        visualize_progress.grid(row=2, column=0, columnspan=2, sticky=E+W)



root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
