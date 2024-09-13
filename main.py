# Programmers:  Hazel, Antonio
# Course:  CS151, Zelalem Yalew
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: This program is designed to compute the cost of gas required
# to travel a certain distance.
# Data In: Distance Traveled (in miles), Price per gallon, Miles per gallon
# Data Out:  Cost of trip
# Credits: [Is your code based on an example in the book, in class, or something else?]


#Prompt user to enter Miles, Miles per Gallon, and Price per gallon
miles_traveled = float(input("Enter miles you will travel: "))
miles_per_gallon = float(input("Enter gas mileage of your vehicle: "))
gas_price = float(input('Enter gas price: '))

#Compute total cost using the variables above
total_price = (miles_traveled / miles_per_gallon) * gas_price

#Output total_price to user rounded to the second decimal point.
print("The total cost of gas for your trip is: $", f'{total_price:.2f}',".")

