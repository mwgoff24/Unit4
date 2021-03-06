'''Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? 
Write down how you would update multi_fruit.

The list multi_fruit had each item from single_fruit appended with an s at the end to make each item plural.
For 100 items in single_fruit, you would need to do this 100 times.


2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers?

It printed each number preceded by 'num is'. The code wouldn't change if 100 items were added.


3. In your console
Rewrite the code from part 1 using knowledge from part 2.'''
single_fruit = ['apple', 'banana', 'watermelon', 'grape']
for item in single_fruit:
    print(item)