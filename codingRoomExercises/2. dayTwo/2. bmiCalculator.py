# Instructions:
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Given:
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# My Plan:
# Declare Variable for users Height
# Declare Variable for users Weight
# Declare BMI variable using BMI Formula (BMI = w/h^2)
# Convert BMI variable to integer
# Print BMI integer value

# My Solution:
bmi = (weight/(height*height))
bmiValue = int(bmi)
print(bmiValue)

# Results: 
