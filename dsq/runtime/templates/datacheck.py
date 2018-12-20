## load modules
import argparse
import os, sys
sys.path.append("../utils")
from utils.functions import check_file_path, check_overwrite
from utils.methods import *

# define configures

description="data checking"
parameters = ["-input", "-log", "-method"]

# add parameters
parser = argparse.ArgumentParser(description=description)
for param in parameters:
    parser.add_argument(param)

args = parser.parse_args()

def do_datachecking(input_file_path, output_log_path, method):
    if not check_file_path(input_file_path):
        print("%s doesn't  exist.")
        return False

    # check overwrite choice
    overwrite_output = True
    if os.path.exists(output_log_path):
        overwrite_output = check_overwrite()
    else:
        pass
    print("Input: ", input_file_path)
    print("Output:  ", output_log_path)

    ## Now do data check
    if overwrite_output:
        ## write ensembling codes
        print("Checking data: %s" % input_file_path)
        if method in Methods.keys():
            datacheck = Methods[method]
            datacheck(input_file_path, output_log_path)
        else:
            datacheck = None
            print("Haven't define data check method: %s" % method)
            raise KeyError

    else:
        print("Choose not to overwrite %s, processing work stopped" % output_file_path)
        return False

if __name__ == "__main__":
    do_datachecking(args.input, args.log, args.method)