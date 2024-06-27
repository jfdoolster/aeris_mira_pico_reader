
if __name__ == "__main__":
    import os, sys
    import pandas as pd
    from read_aeris import get_raw_aeris_data

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, type=str,
        help='path to csv directory containing one or more raw, timestamped Aeris Mira Pico *.txt files')
    args = parser.parse_args()
    argdict = vars(args)

    data_dir=os.path.abspath(argdict['directory'])

    if not os.path.isdir(data_dir):
        print(f"ERROR : '{data_dir:s}' does not exist or is not a directory")
        sys.exit()

    df0 = get_raw_aeris_data(data_dir)

    pd.set_option('display.precision', 1)
    print(df0)





