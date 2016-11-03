class UserLogs(object):
    """
    UserLogs stores all the CharacterLogs that have been entered by the player

    UserLogs is a singleton class used to store the information logged by the
        player and stored in a .csv file.

    Attributes:
        __character_instances : a dict<str, CharacterInstance> maping chaacter
        names to CharacterInstance objects
        __log_file : file object describing location logs are stored
    """

    def __init__(self, infile_name):
        """Inits UserLogs object

        Reads player logs from .csv file

        Args:
            infile_name : a str defining the name of the file to read from

        Returns:
            UserLogs object
        """
        pass

    def get_char_instance(self, name):
        for char in self.__character_instances:
            if (char.name == name):
                return char

    def update_logs(self, new_character_instance):
        """Updates logs with new CharacterInstance

        Updates UserLogs object and writes data to __log_file as a
            CharacterInstance object is updated
        """
        pass

    def sort_by_stat_sum(self, char_1, char_2):
        """Comparator for list of CharacterInstances

        Sorts CharacterInstances by the sum of their most recent stats,
            in ascending order

        Args:
            char_1 : first CharacterInstance to compare
            char_2 : second CharacterInstance to compare

        Returns:
            -1 if char_1 has a lower stat sum than char_2
            0 if char_1 has the same stat sum as char_2
            1 if char_1 has a higher stat sum than char_2
        """
        stats_1 = char_1.get_current_state().stats
        stats_2 = char_2.get_current_state().stats
        sum_1 = 0
        sum_2 = 0
        for stat in stats_1:
            sum_1 += stats_1[stat]
        for stat in stats_2:
            sum_2 += stats_2[stat]
        if (sum_1 < sum_2):
            return -1
        elif (sum_1 > sum_2):
            return 1
        return 0

    def recommend_team(self, num_characters):
        """Recommends a team for the user

        Uses sorted list of CharacterInstances to determine characters with
            highest stat sum, chooses 12 of them

        Args:
            num_characters : number of CharacterInstances to choose

        Returns: List of top num_characters CharacterInstances to use
        """
        sorted_characters = sorted(self.__character_instances, cmp=sort_by_stat_sum)
        best_characters = []
        for i in range(0, num_characters):
            best_characters.append(sorted_characters[i])
        return best_characters
