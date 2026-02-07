filename = "sample.txt"

try:
    print("Reading file content:")
    
    with open(filename, "r") as file:
        line_number = 1
        line = file.readline()
        
        while line:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
            line = file.readline()

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")