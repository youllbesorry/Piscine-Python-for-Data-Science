class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is: ", sum(x * y for x, y in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add Vector is : ", [x + y for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is: ", [x - y for x, y in zip(V1, V2)])
