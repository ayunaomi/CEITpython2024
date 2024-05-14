#CONSTRUCTORS
#OBJECTS
#ENCAPSULATION
#POLYMORPHISM
#INHERITANCE

#RULE 1 CREATE CONSTRUCTOR AKA INIT METHOD (FUNCTION) BEFORE CREATING OBJECTS 
#WHY? PACKAGE EVERYTHING SO WE CAN USE IT ANYWHERE
#creating a new class

#CREATING FIRST CLASS THAT CONTAINS FUNCTIONS USED TO CALCULATE PERIMETER
import math
class PerimeterBox:
    #CREATE CONSTRUCTOR
    def __init__(self) -> None:
        pass 

    #second function
    def PeriRectangle(self):
        l=int(input("Enter length:\n"))
        w=int(input("Enter width:\n"))
        p=l+w+l+w
        print("Perimetre is:",p,"cm")
    #third function


    def Perisquare(self):
        s=int(input("Enter sides:\n"))
        p=s+s+s+s
        print("Perimeter of sqaure is:",p,"cm")
        
        #fourth Function
    def PeriTriangle(self):
        s=int(input('ENTER SIDES:\n'))
        p=s+s+s
        print("Permeter of triangle is:",p,"cm")

        #FIFTH FUNCTION

    def CCircumference(self):
        r=int(input("enter radius:\n"))
        c=2*math.pi*r
        print("Circumference of a circle is:",c,"cm")

#initialize objects 
periObj=PerimeterBox()
#user choice
print("welcomt to perimeterbox\n")
print("Choose with object to calculate its perimeter")
choice=int(input("1.Rectangle\n2.Square\n3.Triangle\n4.Circle\n"))

#CALLING OR USING OBJECT
#periObj.PeriRectangle()


#IF STATEMENT
if choice==1:
    periObj.PeriRectangle()
elif choice==2:
    periObj.Perisquare()
elif choice==3:
    periObj.PeriTriangle()
elif choice==4:
    periObj.CCircumference()
else: 
    print("Invalid option")


