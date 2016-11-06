from tkinter import *
from NewCharachterUi import NewCharacterUi
from compareCharUi import CompareCharUi
from suggestteamUi import SuggestTeamUi
from updateUi import UpdateUi
from visualizeprogressUI import VisualizeProgressUi
from GameData import GameData
from UserLogs import UserLogs


class Application(Frame):
    """Application manages the homescreen for the application
    """

    def __init__(self, master=None):
        """Starts up application
        
        starts up program, parses game data, and loads in previous 
        CharacterInstances and States

        Args:
            master : tkinter.widget identifying the parent widget
        """
        Frame.__init__(self, master)
        self.game_data = GameData("shadow_dragon.csv")
        self.user_logs = UserLogs("user_log.csv", self.game_data)
        self.create_widgets()

    def new_character_f(self):
        """creates a window to add a new CharacterInstance
        """
        root = Tk()
        app = NewCharacterUi(self.game_data, self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def compare_char_f(self):
        """Creates Compare Characters window
            
        creates a window to compare two CharacterInstances based on current 
        State
        """
        root = Tk()
        app = CompareCharUi(self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def suggest_team_f(self):
        """Creates the Suggest Team window
            
        Creates a window to suggest a team based on CharacterInstance current 
        States
        """
        root = Tk()
        app = SuggestTeamUi(self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def update_f(self):
        """Creates the Update Character window
            
        Creates a window to add a new State to an existing CharacterInstance
        """
        root = Tk()
        app = UpdateUi(self.user_logs, master=root)
        app.mainloop()
        root.destroy()

    def visualize_progress_f(self):
        """Creates the Visualize Progress window
            
        Creates a window to see a graph of the progress of a CharacterInstance 
        throughout all States
        """
        root = Tk()
        app = VisualizeProgressUi(self.user_logs, self.game_data, master=root)
        app.mainloop()
        root.destroy()

    def create_widgets(self):
        """Creates display elements
        """
        master = self.master

        browse_character = Button(
            master, 
            text="New Characters", 
            command=self.new_character_f)
        browse_character.grid(row=0, column=0, columnspan=2, sticky=E + W)

        compare_char = Button(
            master, 
            text="Compare Character", 
            command=self.compare_char_f)
        compare_char.grid(row=0, column=3, columnspan=2, sticky=E + W)

        suggest_team = Button(
            master, 
            text="Suggest Team", 
            command=self.suggest_team_f)
        suggest_team.grid(row=1, column=3, columnspan=2, sticky=E + W)

        update = Button(master, text="Update", command=self.update_f)
        update.grid(row=1, column=0, columnspan=2, sticky=E + W)

        visualize_progress = Button(
            master, 
            text="Visualize Progress", 
            command=self.visualize_progress_f)
        visualize_progress.grid(row=2, column=0, columnspan=2, sticky=E + W)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
