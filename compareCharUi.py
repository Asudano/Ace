from tkinter import *


class compareCharUi(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.charattribute = []
        self.createwidgets()

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

    def compare_f(self):
        pass

    def createwidgets(self):
        master = self.master
        self.createlabels("Character 1 Name", 0)
        self.createtextbox("",0)

        self.createlabels("Character 2 Name", 1)
        self.createtextbox("", 1)
        compare = Button(master, text="Compare", command=self.compare_f)
        compare.grid(row=2, column=0, columnspan=2, sticky=E+W)



if __name__ == "__main__":
    root = Tk()
    app = compareCharUi(master=root)
    app.mainloop()
    root.destroy()

