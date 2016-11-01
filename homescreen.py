from tkinter import *
from NewCharachterUi import NewCharachterUI

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidgets()

    def myteam(self):
        print("Hello")
        # TODO: Create Level UP logic

    def newcharachter(self):
        print("browse")
        root = Tk()
        app = NewCharachterUI(master=root)
        app.mainloop()
        root.destroy()

    def compare_char_f(self):
        pass

    def suggest_team_f(self):
        pass

    def update_f(self):
        pass

    def createwidgets(self):
        master = self.master

        browseCharachter = Button(master, text="New Characters", command=self.newcharachter)
        browseCharachter.grid(row=0, column=0, columnspan=2, sticky=E+W)

        compare_char = Button(master, text="Compare Character", command=self.compare_char_f)
        compare_char.grid(row=0, column=3, columnspan=2, sticky=E+W)

        suggest_team = Button(master, text="Suggest Team", command=self.suggest_team_f)
        suggest_team.grid(row=1, column=3, columnspan=2, sticky=E+W)

        update = Button(master, text="Update", command=self.update_f)
        update.grid(row=1, column=0, columnspan=2, sticky=E+W)


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
