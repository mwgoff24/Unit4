'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])

    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program
len(list)+1 will give an error because the last index is out of range, it also prints from 2 to 6 and not from 1

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program
This program doesn't print anything and doesn't swap stars correctly

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''
# functions

# print numbers, prints a list of numbers
def print_numbers(list):
    for i in range(0, len(list)):
        print(list[i])

num_list = [1, 2, 3, 4, 5, 6]

# swapping stars, prints stars but every other star is a dash
def swapping_stars():
    line_str = ""
    for line in range(0, 6):
        for char in range(0, 6):
            if char % 2 == 0:
                line_str += "*"
            else:
                line_str += "-"
    print(line_str)

# program asking user which function they would like to run
while True:
    user_choice = input("Would you like to either print numbers or swap stars? 1 for the former and 2 for the latter: ")
    if user_choice == '1':
        print_numbers(num_list)
    elif user_choice == '2':
        swapping_stars()
    else:
        print("undefined")
        break