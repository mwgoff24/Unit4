'''
#############
Do Now 4.03
#############

Type in your console:
----------------------
    def print_6_stars():
        my_string = ''
        for i in range(0, 6):
            my_string += ' *'
        print(my_string)

In your notebook
-----------------
Write down what the output of the function print_6_stars is.
 * * * * * *

Write a function  print_star_square that calls print_6_stars in a loop to produce the following output.

    >>>python print_stars.py
    * * * * * *
    * * * * * *
    * * * * * *
    * * * * * *
    * * * * * *
    * * * * * *

    # write you code for this function below:
    def print_star_square():
        #your code goes here

Rewrite the function print_star_square without using print_6_stars.
    # write you code for this function below:
        def print_star_square():
            #your code goes here

Note that there are two ways (at least) to get the above output, so just try doing both!
'''
# print_6_stars
def print_6_stars():
    my_string = ''
    for i in range(0, 6):
        my_string += ' *'
    print(my_string)
print_6_stars()
print("\n")

# print_star_square with print_6_stars
def print_star_square():
    my_string = print_6_stars
    for i in range(0, 6):
        print_6_stars()
    print(my_string)
    
print_star_square()
print("\n")

# print_star_square without print_6_stars
def print_star_square1():
    my_string = ''
    for i in range(0, 6):
        my_string += ' * * * * * * \n'
    print(my_string)

print_star_square1()