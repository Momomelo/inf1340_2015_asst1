#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#name_that_shape() will tell you the name of a shape based on the number of sides! It has a limit of three to ten for sides.
def name_that_shape():
	sides = raw_input("How many sides does your shape have?").lower()
	if sides == "3" or sides =="three":
		print ("triangle")
	elif sides == "4" or sides == "four":
		print ("quadrilateral")
	elif sides == "5" or sides == "five":
		print ("pentagon")
	elif sides == "6" or sides == "six":
		print ("hexagon")
	elif sides == "7" or sides == "seven":
		print ("heptagon")
	elif sides == "8" or sides =="eight":
		print ("octagon")
	elif sides == "9" or sides == "nine":
		print ("nonagon")
	elif sides == "10" or sides == "ten":
		print ("decagon")
	else:
		print ("Error")

#name_that_shape()

#Notes:
# Capitals is irrelevant due to the usage of the .lower() function.

# Testing:
# If the user inputs "5", the code will return "pentagon"
# If the user inputs "200", the code will return "Error"
# If the user inputs "5.0", the code will return "Error"
# If the user inputs "-5", the code will return "Error"
# If the user inputs "nine", the code will return "nonagon"
# If the user inputs "FOUR", the code will return "quadrilateral"
# If the user inputs "FoUr", the code will return "quadrilateral"
# If the user inputs "asdf123" the code will return "Error"

# Example Outputs:

# How many sides does your shape have?10
# decagon

# How many sides does your shape have?NiNE
# nonagon

# How many sides does your shape have?over9000!
# Error

#How many sides does your shape have?5.00
# Error