'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    

# Write the code for your custom function below:
def my_function():
    # replace 'pass' with your code
    pass
'''
def draw_7():
    # 7 rows of stars
    for item in range(7):
        # row of stars
        my_string = ''
        for item in range(7):
            my_string += ' *'
        print(my_string)

print("\n")
draw_7()
print("\n")

def stars_and_stripes():
    # 3 rows of stars and stripes
    for i in range(3):
        my_string = ""
        # row of stars
        for i in range(7):
            my_string += ' *'
        print(my_string)
        dash_string = ""
        # row of stripes
        for i in range(7):
            dash_string += ' -'
        print(dash_string)
    print(my_string)

stars_and_stripes()
print("\n")

def increasing_triangle():
    triangle_string = ""
    for i in range(1, 8):
        triangle_string += str(i) + " "
        print(triangle_string)

increasing_triangle()
print("\n")

def vertical_stars_and_stripes():
    # 7 rows
    for i in range(7):
        my_string = ""
        # one row
        for i in range(3):
            my_string += ' -'
            my_string += ' *'
        my_string += ' -'
        print(my_string)

vertical_stars_and_stripes()
print("\n")

'''
Since I can't easily explain what this number grouping is, this is how my_function looks:
2 1
2 1 3 2
2 1 3 2 4 3
2 1 3 2 4 3 5 4
'''

def my_function():
    my_string = ""
    for i in range(1, 5):
        my_string += str(i + 1) + " "
        my_string += str(i) + " "
        print(my_string)

my_function()