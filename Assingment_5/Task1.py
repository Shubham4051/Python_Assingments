'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

dict = {'shubham':100, 'soumya':95, 'sahil':80, 'alice':85}


name = input("Enter the student's name: ")
name_low = name.lower()

# if name_low in dict:
#     print(name+"'s marks:",dict[name_low])
# else:
#     print("Student not found.")

# print(f'{name}\' marks: {dict[name_low]}' if name_low in dict.keys() else "Student not found.")
print('{0}\' marks: {1}'.format(name,dict[name_low]) if name_low in dict.keys() else "Student not found.")