from tkinter import *


class suggestteamUi(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidgets()

    def suggest_f(self):
        pass

    def createwidgets(self):
        master = self.master
        num_char = Label(master, text="Number of Charachters")
        num_char.grid(row=0, column=0, columnspan=1, sticky=E + W)

        num_char_inp = Entry(master)
        num_char_inp.grid(row=0, column=1, columnspan=1, sticky=E + W)

        compare = Button(master, text="Suggest", command=self.suggest_f)
        compare.grid(row=2, column=0, columnspan=2, sticky=E+W)



if __name__ == "__main__":
    root = Tk()
    app = suggestteamUi(master=root)
    app.mainloop()
    root.destroy()

