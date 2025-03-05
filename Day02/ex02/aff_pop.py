from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def convert_data(value):
    if isinstance(value, str):
        if value.endswith('k'):
            return float(value[:-1]) * 1e3
        elif value.endswith('M'):
            return float(value[:-1]) * 1e6
        elif value.endswith('B'):
            return float(value[:-1]) * 1e9
    return float(value)

def country_data(country):
    df = load("population_total.csv")
    
    # Convertir les valeurs de population
    for column in df.columns[1:]:
        df[column] = df[column].apply(convert_data)

    country_data = df[df['country'] == country].iloc[0, 1:]
    print(country_data)
    return country_data

def main():
    first_country = country_data("France")
    second_country = country_data("Belgium")
    
    # Filtrer les données jusqu'à l'année 2050
    first_country = first_country[first_country.index <= '2050']
    second_country = second_country[second_country.index <= '2050']
    
    plt.figure(figsize=(10, 6))
    plt.xlabel('Année')
    plt.ylabel('Population (en millions)')
    plt.title('Évolution de la population')

    plt.plot(first_country.index, first_country.values, label="France")
    plt.plot(second_country.index, second_country.values, label="Belgium")
    plt.xticks(ticks=range(0, len(first_country.index), 40))
    plt.yticks(ticks=range(20_000_000, 100_000_000, 20_000_000))
    plt.gca().set_yticklabels([str(i // 1_000_000) for i in range(20_000_000, 100_000_000, 20_000_000)])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()