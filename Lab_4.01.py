'''
Lab 4.01

Remove the Vowels
Create a function, de_vowel, which will take a string as input and return a copy of that string with all the vowels removed. Otherwise, the string should be the same. 'Y' does not count as a vowel for the purposes of this function.

Create the function contract for de_vowel.

Write de_vowel using a for loop

Provide a few examples that confirm de_vowel works as expected:

What if the string is all vowels?

What if there are no vowels?

What if there is a mix of vowels and non-vowels and spaces?

What if some vowels are capitalized, e.g., the first letter in a sentence?

Example
Example of the file:

    # contract goes here
    def de_vowel(a_string):
        # your code goes here
        
    no_vowels = de_vowel("This sentence has no vowels")
    print(no_vowels)
    # examples go here
Example output:

    >>> python3 de_vowel_lab.py
    Ths sntnc hs n vwls

Bonus
Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function count_vowels.

count_vowels takes in a string and returns an int representing the number of vowels in the string.

Can you think of an alternate way to do complete this task without any loop or counter, by making use of your new de_vowel() function instead?
'''
# remove the vowels
vowels = 'AaEeIiOoUu'

def de_vowel(str):
    no_vowels = ''
    global vowels
    for letter in str:
        if letter not in vowels:
            no_vowels += letter

    return no_vowels

# count the vowels
def count_vowels(str):
    global vowels
    count = 0
    for letter in str:
        if letter in vowels:
            count += 1

    return count

new_str = input("Give a string to devowel: ")
print(f"There are {count_vowels(new_str)} vowels. \n"
f"Your devoweled string is: {de_vowel(new_str)}")