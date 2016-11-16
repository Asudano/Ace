from tkinter import *
from UserLogs import UserLogs
from GameData import GameData


class SuggestTeamUi(Frame):
    """Manages the team suggestion screen
    """

    def __init__(self, user_logs, index=0, master=None):
        """inits a new SuggestTeamUi object to suggest a team of
        CharacterInstances for a user

        Args:
            user_logs : the UserLogs singleton
            master : tkinter.widget identifying the parent widget
        """
        Frame.__init__(self, master)
        self.index = index
        self.components = []
        self.__user_logs = user_logs
        self.__num_char_inp = Entry(master)
        self.create_widgets()

    def suggest_f(self):
        """Suggests a team based on the highest sum of scores in the
        most recent State and displays the names
        """
        master = self.master
        list_char_inst = self.__user_logs.recommend_team(int(
            self.__num_char_inp.get()))
        for i in range(0, len(list_char_inst)):
            char_inst_label = Label(master, text=list_char_inst[i])
            char_inst_label.grid(
                row=3 + i,
                column=self.index,
                columnspan=1,
                sticky=E + W)
            self.components.append(char_inst_label)

    def create_widgets(self):
        """Creates display elements
        """
        master = self.master
        num_char = Label(master, text="Number of Charachters")
        num_char.grid(row=0, column=self.index, columnspan=1, sticky=E + W)

        self.__num_char_inp.grid(
            row=0,
            column=self.index + 1,
            columnspan=1,
            sticky=E + W)
        self.components.append(num_char)

        suggest = Button(master, text="Suggest", command=self.suggest_f)
        suggest.grid(row=2, column=self.index, columnspan=2, sticky=E + W)
        self.components.append(suggest)

    def end(self):
        """
        This function destroys all of the elements created
        """
        for i in self.components:
            i.destroy()

if __name__ == "__main__":
    root = Tk()
    game_data = GameData("shadow_dragon.csv")
    user_logs = UserLogs("log.csv", game_data)
    app = SuggestTeamUi(user_logs, master=root)
    app.mainloop()
    root.destroy()
