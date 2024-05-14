#creating function
#1.use the keyword def
#2.include the function name
#3.Specify the parameters 
#4.main code
#5.return value
#crete a new function
#Call it gross function
#def grossnetCalculator(gross):
    #net=(gross-(0.1*(gross)))
   # print('Net salary is:',net)
    

    
#gross=float(input("Enter annual gross salary\n"))

#using or calling the function
#grossnetCalculator(gross)
#function2 calculating the perimetre of a rectangle

#def periRectangle():
    #l=int (input('enter length:\n'))
   # w=int (input('enter width:\n'))
    #p=l + l + w + w
   # print("Perimeter of rectangle",p,"cm")
#CALL THE FUNCTION
#periRectangle()

#homework QUESTION
#CREATE A FUNCTION,without Parametre
#CALL THIS Area Rectangle
#In the function ask user to enter Length and width
#Calculate the area and print out the result

def AreaRectangle():
    l=int(input("enter length:\n"))
    w=int (input("enter width:\n"))
    A= l*w
    print("Area of a rectangle",A,"cm")
#calling function
AreaRectangle()