## load modules
import argparse
import os, sys

sys.path.append("../utils")
from utils.functions import check_file_path, check_overwrite
from utils.methods import Methods

# define configures
description = "feature engineering"
parameters = ['-input', '-output', '-method']

# add parameters
parser = argparse.ArgumentParser(description=description)
for param in parameters:
    parser.add_argument(param)

args = parser.parse_args()


def do_featureengineering(input_file_path, output_file_path, method):
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

    # Now do feature engineering
    if overwrite_output:
        print("Extract features: %s" % input_file_path)
        if method in Methods.keys():
            feature_engineering = Methods[method]
            feature_engineering(input_file_path, output_file_path)
        else:
            feature_engineering = None
            print("Haven't define feature engineering method: %s" % method)
            raise KeyError

    else:
        print("Choose not to overwrite %s, processing work stopped" % output_file_path)
        return False


if __name__ == "__main__":
    do_featureengineering(args.input, args.output, args.method)