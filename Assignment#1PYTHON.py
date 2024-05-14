"""ASSIGNMENT 1 PYTHON PROGRAMMING Naomi AYU"""
"""Part One"""

#Import math for calculations
import math
class FindArea:                    
    def __init__(self) -> None:    
        pass
    #Functions of class
    def AreaRectangle(self):
        l=int(input("Enter Length:\n"))
        w=int(input("Enter Width:\n"))
        A=l*w
        print("Area of Rectangle is:",A,"cm2")
    
    def AreaTriangle(self):
        b=int(input("Enter base:\n"))
        h=int(input("Enter height:\n"))
        A=0.5*b*h
        print("Area of Triangle is:",A,"cm2")
        
    def AreaCircle(self):
        r=int(input("Enter Radius:\n"))
        A=math.pi*r*r
        print("Area of circle is:",A,"cm2")

#Object Initialization
ARobj=FindArea()
ATobj=FindArea()
ACobj=FindArea()
#Using the Objects
print("Calculating Areas")
ARobj.AreaRectangle()
ATobj.AreaTriangle()
ACobj.AreaCircle()

"""Part Two"""
#Based on your program in part 1, determine if the following is occurring/present in your code.
#Answer Yes/No. If Yes, specify which line of code is responsible for it. State your reason also

#2.1 Encapsulation Yes 
"""Line 19:By creating a class it encapulates or protects and provide security for data,methods and functions."""
#2.2 Polymorphism Yes
"""Line 23-38: Polymorphism allows the user to perform same action in many different ways.
That is calcuting area (same) of diferent shapes"""
#2.3 Inheritance NO