import csv
from pathlib import Path


def read_bands(file_path):
    """Read the bands from a csv file"""

    bands = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)

            for band in reader:
                bands.append(band)
    except FileNotFoundError:
        print(f"{file_path} not found.")

    return bands


def sort_bands_by_stat(bands, column, reverse=True, top_n=3):

    sorted_bands = sorted(bands, key=lambda entry: entry[column], reverse=reverse)
    return sorted_bands[:top_n]


def main():
    local_path = Path(__file__).parent
    file_name = 'data/bands.csv'

    file_path = local_path / file_name
    bands = read_bands(file_path)

    columns = list(bands[0].keys())
    print('Available stats:')
    for i, col in enumerate(columns):
        print(f"{i}. {col}")

    choice = int(input("Enter option: "))
    result_count = int(input("How many results would you like?"))
    column = columns[choice]
    top_bands = sort_bands_by_stat(bands=bands, column=column, top_n=result_count)
    for i, band in enumerate(top_bands):
        print(f"{i + 1}. {band['band_name']} - {band[column]}")


if __name__ == '__main__':
    main()
