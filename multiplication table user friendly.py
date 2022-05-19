""" I wrote a code to print a mul table like in books
if the x value is increased then the table is extened upto the value of x
y value is to mark the index
"""

value = int(input("how many tables:"))
y=1
for x in range(1, value+1):   # 1 x 2 = result x is 1 and y is 2

    while y <= 10:

        print("{:>4}.".format(y),x,"x",y, end= " ")
        print("=",x*y)
        y+=1
    print() 
    y=1

