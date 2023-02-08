# Python script to remove newlines from a text file

import sys

def change_file(values):
    output_filename = "./remove_newlines_output.txt"
    open(output_filename, "w").close()

    with open(output_filename, "a") as file:
        for word in values:
            if word != "":
                file.write(word + "\n")

    print("File generated!")


def main():
    values = []
    file_name = sys.argv[1]

    with open("./" + file_name , "r") as file:
        lines = file.readlines()
        for word in lines:
            values.append(word.strip())
        print(values)

    change_file(values)

if __name__ == "__main__":
    main()
