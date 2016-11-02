from tkinter import *


class visualizeprogressUi(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.charattribute = []
        self.createwidgets()

    def visualize_f(self):
        pass

    def createlabels(self, charachter_name, grideN):
        master = self.master
        charname = Label(master, text=charachter_name)
        charname.grid(row=grideN, column=0, columnspan=1, sticky=E + W)
        self.charattribute.append(charname)

    def createtextbox(self, attribute, gridN):
        master = self.master
        textbox = Entry(master)
        textbox.grid(row=gridN, column=1, columnspan=1, sticky=E + W)
        textbox.insert(0, attribute)

    def createwidgets(self):
        master = self.master

        self.createlabels("Character Name", 0)
        self.createtextbox("",0)

        stat_var = StringVar(master)
        stat_var.set("HP")
        stat_var_drop = OptionMenu(master, stat_var, "HP", "Str", "Mag", "Skl", "Spd", "Lck", "Def", "Res")
        stat_var_drop.grid(row=1, column=0, columnspan=2, sticky=E + W)

        visualize = Button(master, text="Visualize", command=self.visualize_f)
        visualize.grid(row=2, column=0, columnspan=2, sticky=E+W)


if __name__ == "__main__":
    root = Tk()
    app = visualizeprogressUi(master=root)
    app.mainloop()
    root.destroy()

