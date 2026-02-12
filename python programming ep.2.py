# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 09:55:25 2026

@author: User
"""

year = int(input("Enter year:"))
if (year % 400 ==0) or (year % 4 ==0 and year % 100 !=0):
    print("Leap Year")
else:

    print("not a leap year")
