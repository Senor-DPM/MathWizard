import random as r
def Add(d,c):
    if(d==1):
        n1 = r.randint(1,25)
        n2 = r.randint(1,25)
    elif(d==2):
        n1 = r.randint(10,99)
        n2 = r.randint(10,99)
    elif(d==3):
        n1 = r.randint(100,999)
        n2 = r.randint(100,999)
    elif(d==4):
        n1 = r.randint(1000,9999)
        n2 = r.randint(1000,9999)
    answer = n1+n2
    print("Q.",n1,"+",n2,"= ")
    while True:
        try:
            user=int(input("Enter the sum : "))
            break
        except:
            print("Invalid input. Please enter a number.")
            print()

    if user==answer:
        print("Correct answer! Point given.")
        print()
        return c+1
    else:
        print("Incorrect answer. No points given.")
        print()
        return c


def Subtract(d,c):
    if(d==1):
        n1 = r.randint(0,25)
        n2 = r.randint(0,25)
    elif(d==2):
        n1 = r.randint(10,99)
        n2 = r.randint(10,99)
    elif(d==3):
        while n1>100 and n1<-100 and n2>100 and n2<-100:
            n1 = r.randint(100,999)
            n2 = r.randint(100,999)
    elif(d==4):
        while n1>1000 and n1<-1000 and n2>1000 and n2<-1000:
            n1 = r.randint(1000,9999)
            n2 = r.randint(1000,9999)
    if n1>=n2:
        answer=n1-n2
        print("Q.",n1,"-",n2,'=')
    elif n1<n2:
        answer=n2-n1
        print("Q.",n2,"-",n1,'=')
    while True:
        try:
            user=int(input("Enter the difference : "))
            break
        except:
            print("Invalid input. Please enter a number.")
            print()
    if user==answer:
        print("Correct answer! Point given.")
        print()
        return c+1
    else:
        print("Incorrect answer. No points given.")
        print()
        return c



def Multiply(d,c):
    if(d==1):
        n1 = r.randint(1,10)
        n2 = r.randint(1,10)
    elif(d==2):
        n1 = r.randint(10,25)
        n2 = r.randint(10,25)
    elif(d==3):
        n1 = r.randint(11,100)
        n2 = r.randint(11,100)
    elif(d==4):
        n1 = r.randint(100,999)
        n2 = r.randint(100,999)
    answer = n1*n2
    print("Q.",n1,"*",n2,"= ")
    while True:
        try:
            user=int(input("Enter the solution : "))
            break
        except:
            print("Invalid input. Please enter a number.")
            print()

    if user==answer:
        print("Correct answer! Point given.")
        print()
        return c+1
    else:
        print("Incorrect answer. No points given.")
        print()
        return c



def Divide(d,c):
    if(d==1):
        n1 = r.randint(11,50)
        n2 = r.randint(2,10)
    elif(d==2):
        n1 = r.randint(101,500)
        n2 = r.randint(2,10)
    elif(d==3):
        n1 = r.randint(1000,9999)
        n2 = r.randint(11,50)
    elif(d==4):
        n1 = r.randint(-99999,99999)
        n2 = r.randint(11,99)
    if n1<n2:
        n1, n2==n2, n1
    quotient = n1//n2
    remainder = n1%n2
    print("Q.",n1,"/",n2,"= ")
    while True:
        try:
            user_q=int(input("Enter the quotient : "))
            user_r=int(input("Enter the remainder : "))
            break
        except:
            print("Invalid input. Please enter a number.")
            print()
    if user_q==quotient and user_r==remainder:
        print("Both correct! Point given.")
        print()
        return c+1
    elif user_q!=quotient and user_r==remainder:
        print("Only remainder correct. Half point given.")
        print()
        return c+0.5
    elif user_q==quotient and user_r!=remainder:
        print("Only quotient correct. Half point given.")
        print()
        return c+0.5
    else:
        print("Incorrect answer. No points given.")
        print()
        return c