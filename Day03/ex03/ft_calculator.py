class calculator:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        print(f'[{[x + object  for x in self.vector]}]')

    def __mul__(self, object) -> None:
        print(f'[{[x * object  for x in self.vector]}]')

    def __sub__(self, object) -> None:
        print(f'[{[x - object  for x in self.vector]}]')

    def __truediv__(self, object) -> None:
        try:
            print(f'[{[x / object  for x in self.vector]}]')
        except ZeroDivisionError as e:
            print("ZeroDivisionError ", e)
