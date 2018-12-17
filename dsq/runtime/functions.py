import os

def check_overwrite():
    ask_overwrite = input("The output path already exists, overwrite?(y/n)")
    if ask_overwrite in ['y', 'yes']:
        return True
    elif ask_overwrite in ['n', 'no']:
        return False
    else:
        print("type 'y' to overwrite, 'n' not overwrite.")
        check_overwrite()
def check_file_path(file_path):
    if os.path.exists(file_path):
        return True
    else: return False