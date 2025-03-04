"""
Une fonction qui imite le comportement de tqdm,
affichant une barre de progression
pour une itération.

Cette fonction est un générateur qui affiche
une barre de progression dans le style de tqdm,
montrant le progrès actuel (x/total)
"""


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i in lst:
        percentage = ((i + 1) / total) * 100

        nb_bars = int(((i + 1) / total) * 20)
        bar = "█████" * nb_bars + "     " * (20 - nb_bars)

        print(f"\r{int(percentage)}%|{bar}| {i + 1}/{total}", end="")

        yield i
