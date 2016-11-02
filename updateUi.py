from tkinter import *


class updateUi(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.charattribute = []
        self.createwidgets()

    def update_f(self):
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

        self.createlabels("Class", 1)
        self.createtextbox("", 1)

        self.createlabels("Level", 2)
        self.createtextbox("", 2)

        self.createlabels("HP", 3)
        self.createtextbox("", 3)

        self.createlabels("STR", 4)
        self.createtextbox("", 4)

        self.createlabels("MAG", 5)
        self.createtextbox("", 5)

        self.createlabels("Skl", 6)
        self.createtextbox("", 6)

        self.createlabels("Spd", 7)
        self.createtextbox("",7)

        self.createlabels("Lck", 8)
        self.createtextbox("", 8)

        self.createlabels("Def", 9)
        self.createtextbox("", 9)

        self.createlabels("Res", 10)
        self.createtextbox("",10)

        update = Button(master, text="update", command=self.update_f)
        update.grid(row=11, column=0, columnspan=2, sticky=E+W)



if __name__ == "__main__":
    root = Tk()
    app = updateUi(master=root)
    app.mainloop()
    root.destroy()