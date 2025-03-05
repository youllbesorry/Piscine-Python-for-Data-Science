from load_csv import load

try:
    # print(load("life_expectancy_years.csv"))
    load(0)
except (TypeError, FileNotFoundError) as e:
    print(e)
