# Programmers:  Hazel, Antonio
# Course:  CS151, Zelalem Yalew
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: This program is designed to compute the cost of gas required
# to travel a certain distance.
# Data In: Distance Traveled (in miles), Price per gallon, Miles per gallon
# Data Out:  Cost of trip
# Credits: Float codes from Zy-books assignment 1.


#Prompt user to enter Miles, Miles per Gallon, and Price per gallon
distance = float(input("Enter distance you will travel(in miles):" ))
miles_per_gallon = float(input("Enter gas mileage:"))
price_per_gallon = float(input("Enter gas price:"))

#Compute total cost using the variables above

total_cost = (distance / miles_per_gallon) * price_per_gallon

#Output total_price to user rounded to the second decimal point.

print("Your trip's total cost is $", f'{total_cost:.2f}', ".")