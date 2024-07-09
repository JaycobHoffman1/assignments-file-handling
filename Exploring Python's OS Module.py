# Task 1: Directory Inspector

import os

def list_directory_contents(path):
    print(f"Searching for items in directory \"{path}\":")

    try:
        for item in os.listdir(path):
            item_type = "File" if os.path.isfile(os.path.join(path, item)) else "Directory"

            print(f"{item} - {item_type}")
    except FileNotFoundError:
        print("ERROR: No such path exists.")

def main():
    while True:
        try:
            user_path = input("Enter the file path you wish to inspect: ")

            if len(user_path) == 0 or len(user_path) == user_path.count(" "):
                raise ValueError
        except ValueError:
            print("ERROR: Input cannot be blank.")
        else:
            break

    list_directory_contents(user_path)

if __name__ == "__main__":
    main()