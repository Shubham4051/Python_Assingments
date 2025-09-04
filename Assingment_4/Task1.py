'''Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

# try 1
# If file exist:

# file_1 = open("Some_text.txt", "r")
# reading_file = file_1.readlines()
# for lines in reading_file:
#     print(lines)
#
# file_1.close()

# If file not exist:

try:
    file_2 = open("sample.txt", "r")
    read1 = file_2.readlines()
    for lines in read1:
        print(lines)

    file_2.close()

except FileNotFoundError:
    print('Error: The file "sample.text" was not found')