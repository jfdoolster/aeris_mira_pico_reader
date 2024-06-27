
if __name__ == "__main__":
    import os, sys
    import pandas as pd
    from read_aeris import get_raw_aeris_data

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, type=str,
        help='path to csv directory containing one or more raw, timestamped Aeris Mira Pico *.txt files')
    parser.add_argument('-o', '--output', default="data/output.csv", type=str,
        help="output csv filename or directory. Default to ./data/output.csv")
    args = parser.parse_args()
    argdict = vars(args)

    data_dir=os.path.abspath(argdict['directory'])
    out_dir=os.path.abspath(argdict['output'])

    if not os.path.isdir(data_dir):
        print(f"ERROR : '{data_dir:s}' does not exist or is not a directory")
        sys.exit()

    df0 = get_raw_aeris_data(data_dir)

    pd.set_option('display.precision', 1)
    print(df0)

    if (os.path.splitext(out_dir)[-1] not in ['.csv']) or (not os.path.isdir(os.path.dirname(out_dir))):
        print(f"ERROR : '{out_dir}' is not valid *.csv filename")
        sys.exit()

    df0.to_csv(out_dir)
    print(f"PASS  : '{out_dir}' created")







