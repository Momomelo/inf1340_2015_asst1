#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#Use nested if / elif / else to make a flowchart of diagnose_car
#What do you think, is this a good solution?

def diagnose_car():

	car_trouble = str(raw_input("Is the car silent when you turn the key?").lower())
	if car_trouble == "yes":
		str(raw_input("Are the battery terminals corroded?"))
	elif car_trouble == "no":
		str(raw_input("Does the car make a clicking noise?"))
	else:
		print ("ERROR")
		car_trouble()


diagnose_car()


#Interactively queries the user with yes/no questions to identify a possible issue with a car.

# Inputs: yes/Yes , no/No , Any String

# Expected Outputs: Clean Terminals, Replace Cables, Replace battery, check spark plug, choke open/close, service check.

# Errors: ERROR (Loop back to question)

#print("The battery cables may be damaged. Replace cables and try again.")
