#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

stock_purchase =900*2000
commision1 =0.03*(stock_purchase)
stock_sold =942.75*2000
commision2 =0.03*(stock_sold)
money_left=stock_sold - stock_purchase - commision1 - commision2
if(money_left > 0):
    print("Lakshmi made a profit of:")
    print(money_left)
if(money_left < 0):
    print("Lakshmi lost ")
    print abs(money_left)
    # The amount of money that Lakshmi lost should be a positive figure.

# Lakshmi lost $25065 after he sold the stock



