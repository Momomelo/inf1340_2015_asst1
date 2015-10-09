#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#The diagnose_car() function queries the user with Y/N questions to identify a possible issue with a car.
def diagnose_car():

	car_trouble = str(raw_input("Is the car silent when you turn the key?").lower())
	if car_trouble == "yes" or car_trouble == "y":
		car_trouble = str(raw_input("Are the battery terminals corroded?").lower())
		if car_trouble == "yes" or car_trouble == "y":
			print ("Clean terminals and try starting again.")
		elif car_trouble == "no" or car_trouble == "n":
			print ("Replace cables and try again.")
		else:
			print ("ERROR")		
	elif car_trouble == "no" or car_trouble == "n":
		car_trouble = str(raw_input("Does the car make a clicking noise?").lower())
		if car_trouble == "yes" or car_trouble == "y":
			print ("Replace the battery.")
		elif car_trouble == "no" or car_trouble == "n":
			car_trouble = str(raw_input("Does the car crank up but fail to start?").lower())	
			if car_trouble == "yes" or car_trouble == "y":
				print ("Check spark plug connections.")
			elif car_trouble == "no" or car_trouble == "n":
				car_trouble = str(raw_input("Does the engine start and then die?").lower())
				if car_trouble == "yes" or car_trouble == "y":
					car_trouble = str(raw_input("Does your car have a fuel injection?").lower())
					if car_trouble == "yes" or car_trouble == "y":
						print ("Get it in for service.")
					elif car_trouble == "no" or car_trouble == "n":
						print ("Check to ensure the choke is opening and closing.")
					else: 
						print ("ERROR")
				elif car_trouble == "no" or car_trouble == "n":
					print ("Engine is not getting enough fuel. Clean fuel pump.")
				else:
					print ("ERROR")		
			else:
				print ("ERROR")		
		else:
			print ("ERROR")
	else:
		print ("ERROR")

# diagnose_car()


# Notes:
# Capitals is irrelevant due to the usage of the .lower() function.

# Testing:
# If the user inputs "asdf123" the code should return "ERROR"
# A Sequence of "N,N,N,N" outputs "Engine is not getting enough fuel. Clean fuel pump." as the test case checks for it.
	# However this was never asked for in the assignment sheet. Perhaps it was cut out due to page margins?
# A Sequence of "N,N,N,Y,N" outputs "Check to ensure the choke is opening and closing."
# Any string that is not a "yes", "no", "Y", "N" will output as errors.

# Example outputs:
# Is the car silent when you turn the key?adsf
# ERROR

# Is the car silent when you turn the key?N
# Does the car make a clicking noise?no
# Does the car crank up but fail to start?No
# Does the engine start and then die?Y
# Does your car have a fuel injection?YeS
# Get it in for service.