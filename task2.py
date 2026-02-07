filename = "output.txt"

text = input("Enter text to write to the file: ")

with open(filename, "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.")

additional_text = input("\nEnter additional text to append: ")

with open(filename, "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.")

print("\nFinal content of output.txt:")

with open(filename, "r") as file:
    print(file.read())