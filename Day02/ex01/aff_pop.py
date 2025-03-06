from load_csv import load
import matplotlib.pyplot as plt

# def convert_data(value):
#     if isinstance(value, str):
#         if value.endswith('k'):
#             return float(value[:-1]) * 1e3
#         elif value.endswith('M'):
#             return float(value[:-1]) * 1e6
#         elif value.endswith('B'):
#             return float(value[:-1]) * 1e9
#     return float(value)


def main():
    """
    Main function to load life expectancy data, filter it for France, and
    plot the life expectancy projections.

    This function performs the following steps:
    1. Loads the life expectancy data from a CSV file named
       "life_expectancy_years.csv".
    2. Filters the data to extract life expectancy values for France.
    3. Prints the life expectancy data for France.
    4. Plots the life expectancy projections for France over the years using
       Matplotlib.

    The plot includes:
    - X-axis labeled as 'Years'.
    - Y-axis labeled as 'Life expectancy'.
    - A title 'France Life expectancy Projections'.
    - X-ticks set at intervals of 50 years.

    Note: The function assumes that the CSV file is structured with a
    'country' column and subsequent columns representing years.
    """
    try:
        df = load("life_expectancy_years.csv")
    except TypeError as e:
        print(e)

    # # Convertir les valeurs de population
    # for column in df.columns[1:]:
    #     df[column] = df[column].apply(convert_data)

    france_data = df[df['country'] == 'France'].iloc[0, 1:]
    print(france_data)

    plt.figure(figsize=(10, 6))
    plt.plot(france_data.index, france_data.values)
    plt.xlabel('Years')
    plt.ylabel('Life expectancy')
    plt.title('France Life expectancy Projections')
    plt.xticks(ticks=range(0, len(france_data.index), 50))

    plt.show()


if __name__ == "__main__":
    main()
