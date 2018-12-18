## load modules
import argparse
import os
from functions import check_file_path, check_overwrite
## define configures
description="example ensembling"
parameters = ['-input', '-output']

## add parameters
parser = argparse.ArgumentParser(description=description)
for param in parameters:
    parser.add_argument(param)

args = parser.parse_args()

def get_inputs(input_file_path):
    input_files = []
    ## get input files:
    return input_files

def ensemble(input_files, output_file_path):
    pass

def do_ensemble(input_file_path, output_file_path):
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
        input_files = get_inputs(input_file_path)
        ensemble(input_files, output_file_path)
    else:
        print("Choose not to overwrite %s, processing work stopped" % output_file_path)
        return False