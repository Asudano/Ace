from tkinter import *
from UserLogs import UserLogs

class suggestteamUi(Frame):
    def __init__(self, user_logs, master=None):
        Frame.__init__(self, master)
        self.user_logs = user_logs
        self.num_char_inp = Entry(master)
        self.createwidgets()

    def suggest_f(self):
        list_char_inst = self.user_logs.recommend_team(int(self.num_char_inp.get()))
        for i in range(0, int(self.num_char_inp.get()) - 1):
            char_inst_label = Label(master, text=list_char_inst[i].name())
            char_inst_label.grid(row=3 + i, column=0, columnspan=1, sticky=E + W)

    def createwidgets(self):
        master = self.master
        num_char = Label(master, text="Number of Charachters")
        num_char.grid(row=0, column=0, columnspan=1, sticky=E + W)

        self.num_char_inp.grid(row=0, column=1, columnspan=1, sticky=E + W)

        compare = Button(master, text="Suggest", command=self.suggest_f)
        compare.grid(row=2, column=0, columnspan=2, sticky=E+W)


if __name__ == "__main__":
    root = Tk()
    user_logs = UserLogs("log.csv")
    app = suggestteamUi(user_logs, master=root)
    app.mainloop()
    root.destroy()

