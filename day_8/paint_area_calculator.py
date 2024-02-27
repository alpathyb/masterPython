import math


# Write your code below this line 👇
def paint_calc(height, width, cover):
    number_of_can = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_can)} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Please input height: "))  # Height of wall (m)
test_w = int(input("Please input width: "))  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
