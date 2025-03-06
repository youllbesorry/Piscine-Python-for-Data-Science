from S1E9 import Character


class Baratheon(Character):
    """
    This class inherit from the Character
    class to create a Bratheon Character
    """

    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = "brown"
        self.hairs = 'dark'

    def __str__(self) -> str:
        return f"{self.family_name}{self.eyes}{self.hairs}"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    This class inherit from the Character
    class to create a Lannister Character
    """

    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    @staticmethod
    def create_lannister(first_name, is_alive):
        return Lannister(first_name, is_alive)

    def __str__(self) -> str:
        return f"{self.family_name}{self.eyes}{self.hairs}"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
