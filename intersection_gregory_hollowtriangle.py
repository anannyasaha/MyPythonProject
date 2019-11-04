"""Anannya Saha"""
"""100669554"""
"""Finding intersection"""

list1=[1,3,5,7,9,11,13,15,17,19,21,23,25]
list2=[1,4,9,16,25]

commonlist=[]

for i in list1:     
    """ loop over the first list"""
    for c in list2: 
        """loop over the second list"""
        if i==c:
            """if the elements match then insert it into the common list"""
            commonlist+=[c]
            
print("intersect","(",list1,",",list2,")")
print(commonlist)  
"""printing the new commonlist"""
"""Finding the value of pie"""

def gregoryLiebniz(num):
    n=0
    s=0
    while n<=num :
        s=s+((4*(-1)**n)/((2*n)+1))
        """adding each element with the sum"""
        n=n+1
        """increasing the power """
    return s
num=10000000

print(gregoryLiebniz(num))

"""printing the hollow triangle"""

n=int(input("enter the number of rows:"))
"""total row number"""
for i in range(0,n+1):
    """i is the row number"""
    for j in range(0,n-i):
        """j is the number of columns.Number of colums and rows are same"""
        print(' ',end='')
        """being in the same line"""
    for k in range(0,i+1):
        """k is for printing the stars"""
        if i==n or k==i or k==0 :
            """star should print in the last row,on the first column and in the last column"""
            print('*',end='')
        else:
            print(' ',end='')
            """printing space otherwise"""
    print()   
    """going to a new line"""     
            
            