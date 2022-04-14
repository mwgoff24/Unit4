'''
############
Lab 4.04
############

Part 1
-----------
The goal of this lab is to practice using and accessing items from lists of lists.

You have a few errands to run and have created a few shopping lists to help you remember what to buy. 
You stored your notes in a nested list, shopping_cart. This program will allow the user to ask for a 
specific item by its index or update what items are in the cart. The user can request to view list to 
see the items in a specific shopping list.

Shopping Lists
    shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]
User Inputs
1 - Update

The program asks which shopping list the user wants to update, which position it should update, and the new value to update.

2 - View Item

The program asks which shopping list the item is on and which position it occupies, then prints the item's name.

3 - View List

The program asks which shopping list the user wants and prints all of the items associated with that shopping list.

Functions
update_list

Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, 
and a string representing the new value for that item. Does not alter the length of the list.

print_item

Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.

print_list

Takes an int representing the index of the shopping list to print.

Feel free to add more functions as you see fit.

Example
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 1
    Which shopping list would you like to update? 1
    Which item would you like to change? 2
    New value for item #2? cheese
    toothpaste, cheese, milk
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 2
    Which shopping list do you want to choose? 2
    Which item on list #2 do you want to see? 3
    apples
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 3
    Which shopping list would you like to see? 3
    planner, pencils, q-tips

Part 2
------------
In this part of the lab you will go through your shopping list program and perform a few different calculations.

Create a function, all_in_one, that will put all the shopping lists into a single combined list using a for loop.

Create a function, count_q_tips, which will go through all items of the list and keep a count of how many times 
'q-tips' occurs.

In order to make the shopping lists more calcium rich, write a function, drink_more_milk, that adds 'milk' to each 
of the lists (unless it's already there).

You can't have milk without cookies. Write a function if_you_give_a_moose_a_cookie, that will go through every 
element of shopping_cart and update 'milk' to be 'milk and cookies'.

Extension
-------------
Write a function to reverse the order of the lists, and also reverse the order of the items in each list, in the shopping_cart nested list.

The new reversed list should look like the following when printed (newlines and spacing added for clarity):

    shopping_cart = [
        ['q-tips', 'pencils', 'planner'],
        ['apples', 'candy', 'milk'],
        ['milk', 'q-tips', 'tooth paste']
    ]
Tip
Last item can be gotten by my_list[-1]

Second to last element: my_list[-2]

Third to last element: my_list[-3]
'''
# shopping lists

shopping_lists = [
    ['toothpaste', 'q-tips', 'milk'],
    ['milk', 'candy', 'apples'],
    ['planner', 'pencils', 'q-tips']
]
'''
Different way to print out items in a list
for list in shopping_lists:
    for item in list:
        if item == 'q-tips':
            print(item)

for i in range(len(shopping_lists)):
    for j in range(len(shopping_lists[i])):
        print(shopping_lists[i][j])
'''

# functions

# update list, user updates whatever item from whatever list they choose
def update_list(list_num, item_num, new_item):
    shopping_lists[int(list_num)-1][int(item_num)-1] = new_item
    print('\n')
    print(shopping_lists)
    print('\n')

# print item, prints whatever item from whatever list the user chooses
def print_item(list_num, item_num):
    print('\n')
    print(shopping_lists[int(list_num)-1][int(item_num)-1])
    print('\n')
    
# print list, prints whatever list the user chooses
def print_list(list_num):
    print('\n')
    print(shopping_lists[int(list_num)-1])
    print('\n')

# all in one, combines all lists into one
def all_in_one():
    new_list = []
    for list in shopping_lists:
        for item in list:
            new_list.append(item)
    print('\n')
    print(new_list)
    print('\n')

# count q-tips, displays a count of how many q-tips are in shopping_lists
def count_qtips():
    qtip_count = 0
    for list in shopping_lists:
        for item in list:
            if item == 'q-tips':
                qtip_count += 1
    print('\n')
    print(f"You have {qtip_count} q-tips.")
    print('\n')

# drink more milk, adds milk to lists that don't already contain it
def drink_more_milk():
    for list in shopping_lists:
        if 'milk' not in list:
            list.append('milk')
    print('\n')
    print(shopping_lists)
    print('\n')

# if you give a mouse a cookie, updates each milk to say milk and cookies
def if_you_give_a_mouse_a_cookie():
    for list in shopping_lists:
        if 'milk' in list:
            list.pop(list.index('milk'))
            list.append('milk and cookies')
    print('\n')
    print(shopping_lists)
    print('\n')

# reverse all, reverses lists and items in lists
def reverse_all(list):
    for lists in list:
        list.reverse()
        for items in lists:
            lists.reverse()
    print('\n')
    print(list)
    print('\n')

# inputs
while True:
    choice = input("Choose either: 1 = update item, \n"
    "2 = view item, \n"
    "3 = view list, \n"
    "4 = combine lists, \n"
    "5 = count q-tips, \n"
    "6 = add milk to lists that don't have it, \n"
    "7 = make milk say milk and cookies, \n"
    "8 = reverse everything, \n"
    "9 = quit program: ")
    if choice == '1':
        list_choice = input("What list number, 1, 2, or 3, contains the item you would like to update? ")
        item_choice = input("What item number would you like to update? ")
        new_item = input("What item do you want to add? ")
        update_list(list_choice, item_choice, new_item)
    elif choice == '2':
        list_choice = input("What list would you like to view, 1, 2, or 3? ")
        item_choice = input("What item would you like to view from this list, 1, 2, or 3? ")
        print_item(list_choice, item_choice)
    elif choice == '3':
        list_choice = input("What list would you like to view, 1, 2, or 3? ")
        print_list(list_choice)
    elif choice == '4':
        all_in_one()
    elif choice == '5':
        count_qtips()
    elif choice == '6':
        drink_more_milk()
    elif choice == '7':
        if_you_give_a_mouse_a_cookie()
    elif choice == '8':
        reverse_all(shopping_lists)
    elif choice == '9':
        break
    else:
        print("That's not an available command.")