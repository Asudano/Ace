from State import State


class CharacterData(object):
    """
    CharacterData contains constant values set by the game for a character

    Attributes:
        __name : a str giving the character's name
        __game_class_options : a list<str> describing all in game classes this
            character can be
        __growth_rate_class: a dict<str, GrowthRate> mapping class names onto
            GrowthRate objects associated with that character/class combination
        __base_stats : a State describing the character's State when they are
            first encountered
    """

    class GrowthRates(object):
        """
        GrowthRates wraps a dictionary of growth rates for a given
            character/class combination

        Attributes:
            __rates : a dict<Stat, float> mapping stats onto their growth rates
        """

        def __init__(self, rates):
            """Inits GrowthRates with rates

            Args:
                rates : a dict<Stat, float> mapping stats onto their
                    growth rates

            Returns:
                GrowthRates object
            """
            self.__rates = rates
        @property
        def rates(self):
            return self.__rates

    def __init__(self, name):
        """Inits GrowthRates with rates"""

        self.__name = name
        self.__game_class_options = []
        self.__growth_rate_class = {}
        self.__base_stats = []

    @property
    def name(self):
        return self.__name

    def add_base_stats(self, array):
        pass

    @property
    def rates(self):
        return self.__rates

    def add_initial_state(self, state):
        """Sets the initial state for CharacterData

        Args:
            state : State object for character's initial state
        """
        self.__base_stats.append(state)

    def get_growth_rates(self, game_class):
        """Retrieves GrowthRates object for given in game class

        Args:
            game_class : a str describing an in game class

        Returns:
            GrowthRates object associated with the desired in game class
        """
        return self.__growth_rate_class[game_class].rates

    def predict_state(self, level, game_class):
        """Creates a state for the average stats for a character with a given
            in game class and level

        Args:
            level : an int representing an in game level
            game_class: a str describing an in game class

        Returns:
            A state object representing the average for this character at the
                given class and level.
        """
        pass

    def get_base_level(self):
        return (self.__base_stats)[0].level

    def get_base_stats(self):
        return (self.__base_stats)[0].get_stats()

    def get_base_class(self):
        return (self.__base_stats)[0].game_class

    def add_class_and_growth_rates(self, game_class, rates):
        # TOOD: doctstring
        self.__game_class_options.append(game_class)
        self.__growth_rate_class = self.GrowthRates(rates)
