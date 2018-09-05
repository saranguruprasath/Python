# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:27:09 2018

@author: saran
"""

class Circle():
    
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    
    def get_circumference(self):
        return 2 * self.pi * self.radius
    

my_circle = Circle()
my_circle1 = Circle(12)


print(my_circle.area)
print(my_circle.get_circumference())
print("\n"*2)
print(my_circle1.area)
print(my_circle1.get_circumference())
