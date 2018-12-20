## load modules
import argparse
import os,sys
sys.path.append("../utils")
from utils.functions import check_file_path, check_overwrite
from utils.methods import Methods

## define configures
description="example ensembling"
parameters = ['-input', '-output', '-method']

## add parameters
parser = argparse.ArgumentParser(description=description)
for param in parameters:
    parser.add_argument(param)

args = parser.parse_args()

def do_ensemble(input_file_path, output_file_path, method):
    if not check_file_path(input_file_path):
        print("%s doesn't  exist.")
        return False

    # check overwrite choice
    overwrite_output = True
    if os.path.exists(output_file_path):
        overwrite_output = check_overwrite()
    else:
        pass
    print("Input: ", input_file_path)
    print("Output:  ", output_file_path)

    ## Now do ensembling
    if overwrite_output:
        ## write ensembling codes
        print("Ensembling predictions: %s" % input_file_path)
        if method in Methods.keys():
            ensemble = Methods[method]
            ensemble(input_file_path, output_file_path)
        else:
            ensemble = None
            print("Haven't define ensemble method: %s" % method)
            raise KeyError
        
    else:
        print("Choose not to overwrite %s, processing work stopped" % output_file_path)
        return False

if __name__ == "__main__":
    do_ensemble(args.input, args.output, args.method)