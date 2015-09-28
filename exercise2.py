#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#This program will tell you the name of a shape based on the number of sides!
def name_that_shape():
	sides = raw_input("How many sides does your shape have?").lower()
	if sides == "3" or sides =="three":
		print ("triangle")
	elif sides == "4" or sides == "four":
		print ("square")
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
	else:
		print ("Error")

name_that_shape()

#Notes: 
#There has to be a smarter way to do this to cut redundancy...
