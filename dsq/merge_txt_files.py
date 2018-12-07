import os
import argparse
parser = argparse.ArgumentParser(prog="merge_files", 
                                 description="Merge files under a directory to one single file")

parser.add_argument("-d", required=True, type=str, help="input target directory")
parser.add_argument("-o", required=True, type=str, help="output file path")
args = parser.parse_args()

def merge_files(directory, output):
    files = [os.path.join(directory, i) for i in os.listdir(directory) if len(i.split("."))==1]
    with open(output, "w") as output_file:
        for f in files:
            with open(f, "r") as input_file:
                p = input_file.read()
                output_file.write(p)
            print("File:" ,f, "has been writen into ", output)
    return True

if __name__ == "__main__":
    print(args.d)
    print(args.o)
    merge_files(args.d, args.o)
