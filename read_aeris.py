import os, sys
import glob
import pandas as pd
import numpy as np
from tqdm import tqdm

def get_raw_aeris_data(raw_data_path: str) -> pd.DataFrame:
    """
    process raw aeris csvs
    """

    df_list = []
    files = sorted(glob.glob(f"{raw_data_path}/Pico*.txt"))
    pbar = tqdm(range(len(files)), leave=False)
    for i in pbar:
        pbar.set_description("Reading Aeris Files")
        fname = files[i]
        dataframe = pd.read_csv(fname, na_values=["No Data"])
        dataframe.columns = ["Timestamp", "Inlet",
                      "T_a", "CH4", "H2O",
                      "C2H6", "R", "C2C1",
                      "Battery", "Power",
                      "Current", "SOC",
                      "Lat_a", "Lon_a"
                     ]
        dataframe["Timestamp"] = pd.to_datetime(dataframe["Timestamp"])
        dataframe = dataframe.astype(float, errors="ignore")
        df_list.append(dataframe)

    final = pd.concat(df_list, ignore_index=True)
    seconds = np.array(final["Timestamp"] - final["Timestamp"].min()) / np.timedelta64(1,'s')
    final.insert(1, 'Seconds_a', seconds)

    return final

