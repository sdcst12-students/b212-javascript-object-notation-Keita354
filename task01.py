#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

file_paths = ["task01a.txt", "task01b.txt", "task01c.txt"]

def find_largest_num(data):
    if len(data)== 0:
        return None
    else:
        return max(data)
    
for file_path in file_paths:
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)

        if isinstance(json_data, list) and all(isinstance(num,(int,float)) for num in json_data):
            largest_num = find_largest_num(json_data)
            if largest_num is not None:
                print(f"The largest number in {file_path} is:", largest_num)

            else:
                print(f"{file_path} is empty.")
        else:
            print(f"The JSON data in {file_path} is not a list of numbers. ")
    except FileNotFoundError:
        print("File not found:", file_path)
    except json.JSONDecodeError:
        print(f"Error decoding JSON data in {file_path}")