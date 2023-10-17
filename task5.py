#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
nums = (5,-2,12,-8,14,16)

for i in nums:
    if i-abs(i) == 0:
        print(f"The square root of {i} is {(i**0.5)}")
