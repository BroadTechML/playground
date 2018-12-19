# load modules
import argparse
import os
from functions import check_file_path, check_overwrite
## define configures
description="example preprocessing"
parameters = ['-input', '-output']

## add parameters
parser = argparse.ArgumentParser(description=description)
for param in parameters:
    parser.add_argument(param)

args = parser.parse_args()



def preprocessing(input_file_path, output_file_path):
    pass

def do_preprocessing(input_file_path, output_file_path):
    # check file:
    if not check_file_path(input_file_path):
        print("%s doesn't  exist." % input_file_path)
        return False

    # check overwrite choice
    overwrite_output = True
    if os.path.exists(output_file_path):
        overwrite_output = check_overwrite()
    else:
        pass
    print("Input: ", input_file_path)
    print("Output:  ", output_file_path)

    ## Now do preprocessing
    if overwrite_output:
        ## write preprocessing codes
        print("Processing data: %s" % input_file_path)
        preprocessing(input_file_path, output_file_path)
    else:
        print("Chose not to overwrite %s, processing work stopped" % output_file_path)
        return False

if __name__ == "__main__":
    do_preprocessing(args.input, args.output)
