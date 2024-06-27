# aeris_mira_pico_reader

Read timestamped data *.txt files exported from MIRA Pico. Must specify directory with one or more datafiles as shown below.

Developed and tested with python 3.11

### Usage:

```bash
python main.py -d /path/to/dir/

python main.py -d data
```

### Output:

pandas dataframe with
* original data timestamp ('Timestamp')
* Seconds from starting timestamp ('Sec')
* Inlet Number ('Inlet')
* Electronics/Battery Temperature ('T_a') in C
* Methane, Water Vapor, and Ethane concentrations ('CH4' ppm, 'H2O' ppm, and 'C2H6' **ppb**)
* Methane and Ethane Correlation ('C2C1')
* Battery Voltage ('Battery') in mV
* Power Consumption ('Power') in mW
* Current Draw ('Current') in mA
* Geographic Coordinates ('Lat_a' and 'Lon_a') in degrees (requires external GPS module)

### Contact:

jonathan.dooley@student.nmt.edu
