# -*- coding: utf-8 -*-
"""
Anannya Saha
id#100669554
Assignment 4

"""
#question 1
class StudentEntry:
    #this is the constructor.
    def __init__(self,name,sid):
        self.name=name
        self.sid=sid
        
    #this is the function to calculate average
    def average(self):
        return self.labs+self.assignments+self.midterm*.3+self.final*.4
    
    #this is the function to determine lettergrade
    def letterGrade(self):
        marks=self.average()
        if 80<=marks<=100:
            return "A"
        if 70<=marks<=79:
            return "B"
        if 60<=marks<=69:
            return "C"
        if 50<=marks<=59:
            return "D"
        if 40<=marks<=49:
            return "E"
#bsmith is anobject
bsmith=StudentEntry("Bob Smith","1000001")
#these are the variables needed to calculate the average
bsmith.labs=9.0
bsmith.assignments=17.0
bsmith.midterm=57.5
bsmith.final=60.0
#we call the function lettergrade to determine the lettergrade
print("Bob smith: ",bsmith.letterGrade())
#this is another object
sjones = StudentEntry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5
print("Sally Jones: ", sjones.letterGrade())

#Question2
#this is declaration of the class
class Product:
    #constructor
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight
    #this method determines the shipping cost
    def getshippingcost(self):
        shippingcost=self.weight*10
        return shippingcost
    #this method determines the tax
    def gettax(self):
        tax=self.price*0.13
        return tax
    #this method determines total price
    def getTotalPrice(self):
        totalcost=self.price+self.gettax()+self.getshippingcost()
        return totalcost
#objects are created
razor=Product("razor",49.99,0.25)
homeGym = Product("Home Gym", 879.99, 115.0)
print("total cost of", razor.name, ":", razor.getTotalPrice())
print("total cost of", homeGym.name, ":", homeGym.getTotalPrice())

#question 3
def subset(list1,list2):
    ctr=0
    for i in list1:
        for j in list2:
            if i==j:
                #counting how many elements match
                ctr=ctr+1
    ctr2=0
    for i in list1:
#counting how many elements are there in list1
        ctr2=ctr2+1
    if ctr2==ctr:
        print("True")
    else:
        print("False")
subset([1,9,13,15,23], [1,3,5,7,9,11,13,15,17,19,21,23,25])

#question 4
def sublistinRange(list1,a,b):
    list2=[]
    for i in list1:
#checking if element in list1 is in the range
        if a<=i<=b:
            list2.append(i)
    return(list2)

print(sublistinRange([5,8,3,21,7,4,14], 4, 14))


#question 5
def ispalindrome(word):
#base case
    if len(word) < 2: return True
#checking if the last letter and the first letter is same or not
    if word[0] != word[-1]: return False
#calling the function for the inner words
    return ispalindrome(word[1:-1])
print(ispalindrome("level"))
print(ispalindrome("lever"))


#question 6
def jumpMaximum(list1):
    ctr=0
    maxi=0
    maxilocation=0
    for i in list1:
        if maxi<i:
#finding the maximum
            maxi=i
#finding the location of the maximum number
            maxilocation=ctr
#the counter for index should go on.
        ctr=ctr+1
#temporary variable is needed to store the first element of list
    temp=list1[0]
#maximum number should be assigned to the first element
    list1[0]=maxi
#first element should be on the position o fmaximum number
    list1[maxilocation]=temp
    return list1
print(jumpMaximum([5,8,3,21,7,4,14]))

#question 7
def isReordering(list1):
    #storing the list first
   # list3=list1
    #this is an example of insertion sort
    for j in range (1,len(list1)):
        #we start comparing with the element which is before the element from where we started
        i=j-1
        #keeping the backup of the element from where we started
        key=list1[j]
        #reordering will go on untill an element comes which is smaller than the key
        while(i>=0 and list1[i]>key):
            #changing position for the greater elements
            list1[i+1]=list1[i]
            #going back to the direction from where we started 
            i=i-1
        #keeping the key right before the smaller number
        list1[i+1]=key
        #checking if the list2 is sorted as list1
    
    return list1
     
print(isReordering([5,8,3,21]))



