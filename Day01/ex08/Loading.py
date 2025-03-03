def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i in lst:
        percentage = (i / total) * 100

        nb_bars = int((i / total) * 20)
        bar = "=" * nb_bars + "-" * (20 - nb_bars)

        print(f"\r{int(percentage)}%|{bar}| {i}/{total}", end="")