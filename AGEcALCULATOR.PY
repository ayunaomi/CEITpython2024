"""THIS PROGRAMME SHOULD ACCEPPT INPUT INPUT FROM USER AND CALCULATE THE PERSONS AGE"""
#step 1-->create class
class AgeCalculator:
    def __init__(self) -> None:
        pass

    def calculatemyage(self):
        YOB= int(input("Enter year of birth\n"))
        if (YOB > 2024):
            print("invalid year")
        else:
            Ans=2024-YOB
            print("I am",Ans,"years wiser")


#Object initialization
#OBJECTNAME CAN BE ANY
Ageobj=AgeCalculator()
#use the object
print("Welcome ")
Ageobj.calculatemyage()
#this is optional
