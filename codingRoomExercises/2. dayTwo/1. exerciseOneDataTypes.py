# Instructions:
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Given:
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Write your code above this line 👆

# My Plan:
# Input String value 0 = number 1
# Input String value 1 = number 2
# Convert both string values into integers
# Ouput Sum value = number 1 + number 2
# Print output sum value

# My Solution:
numberOne = two_digit_number[0]
numberTwo = two_digit_number[1]

evalNumberOne = int(numberOne)
evalNumberTwo = int(numberTwo)

outputSum = evalNumberOne + evalNumberTwo

print(outputSum)

# Result: 100% Match
