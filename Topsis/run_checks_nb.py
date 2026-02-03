from topsis_gaurika_dua_102303271.core import run_topsis
import pandas as pd

data = {
    "P1": [0.84, 0.91, 0.79, 0.78, 0.94, 0.88, 0.66, 0.93],
    "P2": [0.71, 0.83, 0.62, 0.61, 0.88, 0.77, 0.44, 0.86],
    "P3": [6.7, 7, 4.8, 6.4, 3.6, 6.5, 5.3, 3.4],
    "P4": [42.1, 31.7, 46.7, 42.4, 62.2, 51.5, 48.9, 37],
    "P5": [12.59, 10.11, 13.23, 12.55, 16.91, 14.91, 13.83, 10.55],
}

pd.DataFrame(data).to_csv('nb_input.csv', index=False)
run_topsis('nb_input.csv','1,1,1,1,1','+,+,-,+,+','nb_output.csv')
print('WROTE nb_output.csv')
print(pd.read_csv('nb_output.csv').head())
