from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads data from two CSV files,
    'income_per_person_gdppercapita_ppp_inflation_adjusted.csv' and
    'life_expectancy_years.csv', for the year 1900. Creates a scatter plot
    representing the gross domestic product (GDP) per capita against life
    expectancy.

    The GDP data is displayed on a logarithmic scale. The plot is titled
    '1900' and the axes are labeled accordingly. The points on the plot are
    blue and have a size of 100.

    This function does not return any value.
    """
    try:
        df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df2 = load("life_expectancy_years.csv")
    except TypeError as e:
        print(e)

    income = df1['1900'].values
    life_expectancy = df2['1900'].values

    plt.scatter(income, life_expectancy, color="blue", marker=".", s=100)
    plt.title("1900")
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()
