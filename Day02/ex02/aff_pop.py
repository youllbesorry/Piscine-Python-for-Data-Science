from load_csv import load
import matplotlib.pyplot as plt


def convert_data(value):
    """
    Converts a population value from a string format to a floating-point
    number.

    The suffixes 'k', 'M', and 'B' are converted to thousands, millions,
    and billions, respectively.

    Parameters:
    value (str or float): The population value to convert.

    Returns:
    float: The numeric value of the population.
    """
    if isinstance(value, str):
        if value.endswith('k'):
            return float(value[:-1]) * 1e3
        elif value.endswith('M'):
            return float(value[:-1]) * 1e6
        elif value.endswith('B'):
            return float(value[:-1]) * 1e9
    return float(value)


def country_data(country):
    """
    Loads population data for a given country and converts it to numeric
    values.

    Parameters:
    country (str): The name of the country for which to retrieve
    population data.

    Returns:
    pandas.Series: The population data for the specified country,
    indexed by year.
    """
    try:
        df = load("population_total.csv")
    except TypeError as e:
        print(e)

    for column in df.columns[1:]:
        df[column] = df[column].apply(convert_data)

    country_data = df[df['country'] == country].iloc[0, 1:]
    print(country_data)
    return country_data


def main():
    """
    Main function that generates a graph of population trends for France
    and Belgium.

    This function loads population data, filters it up to the year 2050,
    and displays a graph comparing the population trends of the two
    countries.
    """
    first_country = country_data("France")
    second_country = country_data("Belgium")

    first_country = first_country[first_country.index <= '2050']
    second_country = second_country[second_country.index <= '2050']

    plt.figure(figsize=(10, 6))
    plt.xlabel('Year')
    plt.ylabel('Population (in millions)')
    plt.title('Population Trends')

    plt.plot(first_country.index, first_country.values, label="France")
    plt.plot(second_country.index, second_country.values, label="Belgium")
    plt.xticks(ticks=range(0, len(first_country.index), 40))
    plt.yticks(ticks=range(20_000_000, 100_000_000, 20_000_000))
    plt.gca().set_yticklabels([str(i // 1_000_000) for i in
                               range(20_000_000, 100_000_000, 20_000_000)])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
