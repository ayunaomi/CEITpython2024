#my_list =['p','r','o','g','a','m','i','z']
#print(my_list[2:5])
#print(my_list[5:])
#print(my_list[:])
#list in square brackets
#ceit =['CCIT','CCDBM','CCNS','CCAIT']
#ceit.append ('CCLSA')#ADD
#print (ceit)
#CHANGING AN ITEM IN LIST
#ceit[2]='CCDCA'
#print(ceit)
#deleting
#del ceit[3]
#print (ceit)
#ceit.remove('CCAIT')
#print(ceit)

#using length function
#print(len(ceit))

#tuple

#my_info=("naomi",23,71686549,ceit)
#print(my_info)
#print(type(my_info))
#my_info[1]=21
#print(my_info)#cannot change
#exercise
#q1
#a=(1,2,3,4,5)
#del a
#print(a) # a not defined
#q2
a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
print(a.count(1))
print(a.index(5))

#Question 3
#i) Create an empty tuple and print output
empty_tuple=()
print (empty_tuple)
#ii) Create a tuple with integers: 4, 6, 8, 10, 12, 14 and print outcome
integer=(4,6,8,10,12,14)
print(integer)
#iii) Create a tuple with having objects with different data types: => integer 4, string "Python",and float
#9.3 and print output on screen
tuple=(4,"Python",9.3)
print(tuple)
#iv) Create a nested tuple having => "Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6) and print output on screen
nested_tuple=("Python",{4:5, 6:2, 8:2},(5,3,5,6))
print(nested_tuple)
#What object is "Python"? Ans: _ _ _String
#What object is (5, 3, 5, 6)? Ans: _ _ _tuple
#What object is {4: 5, 6: 2, 8:2}? Ans: _ _ _dictionary
