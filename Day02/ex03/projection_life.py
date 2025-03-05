from load_csv import load


def main():
    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = load("life_expectancy_years.csv")

if __name__ == "__main__":
    main()