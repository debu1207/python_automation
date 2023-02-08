# python script to find a file in a directory

import sys
import os

def check_directory(path, file_to_find):
    # List of all the files in the directory
    files = os.listdir(path) 

    # check whether the file is present in the directory
    if file_to_find in files:
        print("File found at: " , path +"/" + file_to_find) 
        return True

    result = False

    # Recursively checking all the directories for the file to find
    for f in files:
        if os.path.isdir(path + "/" + f):
            result = result or check_directory(path + "/" + f, file_to_find) 
            if result:
                return True

    return result

def main():
    path = sys.argv[1] # path - where to find the file
    file_to_find = sys.argv[2] # file name
    result = check_directory(path, file_to_find)
    if result :
        print("File found!")
    else:
        print("File not found!")


if __name__ == "__main__":
    main()
