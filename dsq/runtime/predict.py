## load modules
import argparse
import os
from functions import check_file_path, check_overwrite
## define configures
description="example predicting"
parameters = ['-input', '-output', '-models']


## add parameters
parser = argparse.ArgumentParser(description=description)
for param in parameters:
    parser.add_argument(param)

args = parser.parse_args()

def get_models(models_path):
    models = []
    ## read models_path and get models list or model object
    return models

## predict function, write predicting process here
def predict(input_file_path, ouptut_file_path, models):
    pass

def do_predict(input_file_path, output_file_path, models_path):
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

    ## Now do preprocessing
    if overwrite_output:
        ## write preprocessing codes
        print("Predicting data: %s" % input_file_path)
        models = get_models(models_path)
        predict(input_file_path, output_file_path, models)
    else:
        print("Choose not to overwrite %s, processing work stopped" % output_file_path)
        return False

