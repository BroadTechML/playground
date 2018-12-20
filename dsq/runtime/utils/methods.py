# predict function, write predicting process here
def predict_wjh(input_file_path, ouptut_file_path, models):
    pass

def ensemble_wjh(input_file_path, ouptut_file_path):
	# do ensemble
	return None


Methods = {
    "predict_wjh": predict_wjh,
    "ensemble_wjh": ensemble_wjh
}

if __name__ == "__main__":
    print(Methods['predict_wjh'])
