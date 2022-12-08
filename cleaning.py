import pandas as pd
import os
import numpy as np

def clean_data():

    # turn csv file into dataframe
    df = pd.read_csv(os.path.join('data','dataset.csv'), sep=';')

    # drop duplicate uuid
    df.drop_duplicates(subset=['uuid'], inplace=True)

    # drop rows with NaN values (this dropped all but 9k rows, so went against it)
    # df.dropna(inplace=True)

    print(f"The number of defaults == 1: {len(df[df['default'] == 1])}")
    print(f"The number of defaults == 0: {len(df[df['default'] == 0])}")

    return print(df)

clean_data()
