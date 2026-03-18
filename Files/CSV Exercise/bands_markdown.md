# Battle of the Bands Contest with CSVs

The `bands.csv` file in the `data` directory contains data related to a battle of the bands contest and its results. Use Python's `csv` package to read data from the `bands.csv` file and print different fields.

Use proper __relative file pathing__ (using the `Path` object) so that the python file can be executed from any directory.
## Requirements

Create the following functions:

1. `main()`:
    - The main function of the program where all the program code will go. It must:
        - load the `bands.csv` using relative file pathing.
        - present the user with a list of columns they can choose.
        - ask the user to choose one of the columns
        - ask the user the number of results they want to return
        - present the requested results to the user
2. `read_csv(file_path)`:
    - A function that accepts a file path as a parameter
    - returns a list of entries (as dictionaries)
    - Handles any possible errors using a try/except
3. `sort_bands_by_stat(bands, column, reverse, top_n)`
    - A function that will sort a list of bands in reverse order based on a specified column
    - By default it gets the top 3 results and sorts in reverse

## Sample Output
```python
Available stats:
0. band_name
1. genre
2. crowd_score
3. judge_score
4. songs_performed
5. stage_energy
Enter option: 1
How many results would you like?10
1. Neon Serpents - Synthwave
2. Lunar Static - Synthwave
3. Midnight Formula - Synthwave
4. Neon Psalms - Synthwave
5. The Pale Machine - Synthwave
6. The Phantom Riffs - Rock
7. The Burning Halos - Rock
8. Savage Lullaby - Rock
9. The Iron Chorus - Rock
10. Voltage Saints - Rock
```