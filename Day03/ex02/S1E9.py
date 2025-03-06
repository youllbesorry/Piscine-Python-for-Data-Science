from abc import ABC, abstractmethod


class Character(ABC):
    """
    Your docstring for Class Character
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        The constructor of Character class how take
        first_name and is_alive=True as parameter
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        This methode make the character die by setting is_alive to False
        """
        self.is_alive = False


class Stark(Character):
    """
    Your docstring for Class Stark
    """
    def __init__(self, first_name, is_alive=True):
        """
        The constructor of Character class how take
        first_name and is_alive=True as parameter
        """
        self.first_name = first_name
        self.is_alive = is_alive
