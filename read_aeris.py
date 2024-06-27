import os
import glob
import pandas as pd
from tqdm import tqdm

def get_raw_aeris_data(raw_data_path: str, csv_data_path = None):
    """
    process raw aeris csvs
    """

    if csv_data_path is not None:
        if isinstance(csv_data_path, str) and os.path.isfile(f"{csv_data_path}/aeris.csv"):
            final = pd.read_csv(f"{csv_data_path}/aeris.csv", parse_dates=['Timestamp'])
            return final

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

    final = pd.concat(df_list)

    if isinstance(csv_data_path, str):
        if not os.path.exists(csv_data_path):
            os.makedirs(csv_data_path)
        final.to_csv(f"{csv_data_path}/aeris.csv")

    return final

