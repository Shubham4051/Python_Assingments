'''Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''




file = open("output.txt", "r+")

a1 = input("Enter Text to the file:")
w1 = file.write(a1 + "\n")
print("Data successfully written to output.txt")

a2 = input("\nEnter additional Text to append:")
w2 = file.write(a2 + "\n")
print("Data successfully appended")

file.close()

print('\nFinal content of the file is:')

file = open("output.txt", "r+")
read_all = file.readlines()
for line in read_all:
    print(line)
file.close()






