import xarray as xr
import argparse
import sys
 
def convert(input, output):
 
    try:
        ds = xr.open_dataset(
                        input,
                        engine='cfgrib',
                        backend_kwargs={'indexpath':''}
                        )
 
    except FileNotFoundError:
        sys.exit("File was not found : {}".format(input))
 
    ds.to_netcdf(output)
 
 
if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description='GRIB to NetCDF converter\n',
            formatter_class=argparse.RawTextHelpFormatter)
     
    parser.add_argument('-i', dest='input', metavar='INPUT_FILE', required=True, help='INPUT_FILE')
    parser.add_argument('-o', dest='output', metavar='OUTPUT_FILE', required=True, help='OUTPUT_FILE')
     
    args = parser.parse_args()
 
    convert(args.input,args.output)