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

def main():
    df = load("life_expectancy_years.csv")
    
    # Convertir les valeurs de population
    for column in df.columns[1:]:
        df[column] = df[column].apply(convert_data)

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