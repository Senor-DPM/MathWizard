import random as r
deci=[0.1,0.1,0.1,0.1,0.1,0.01,0.01,0.01,0.001]
def Add_Rat(d,c):
    if(d==1):
        n1 = r.randint(-25,25) * deci[r.randint(0,len(deci-1))]
        n2 = r.randint(-25,25) * deci[r.randint(0,len(deci-1))]
    elif(d==2):
        n1 = r.randint(-99,99) * deci[r.randint(0,len(deci-1))]
        n2 = r.randint(-99,99) * deci[r.randint(0,len(deci-1))]
    elif(d==3):
        while n1>100 and n1<-100 and n2>100 and n2<-100:
            n1 = r.randint(-999,999) * deci[r.randint(0,len(deci-1))]
            n2 = r.randint(-999,999) * deci[r.randint(0,len(deci-1))]
    elif(d==4):
        while n1>1000 and n1<-1000 and n2>1000 and n2<-1000:
            n1 = r.randint(-9999,9999) * deci[r.randint(0,len(deci-1))]
            n2 = r.randint(-9999,9999) * deci[r.randint(0,len(deci-1))]
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
        print(f"Incorrect answer. The correct answer was {answer}. No points given.")
        print()
        return c


def Subtract_Rat(d,c):
    if(d==1):
        n1 = r.randint(-25,25)
        n2 = r.randint(-25,25)
    elif(d==2):
        n1 = r.randint(-99,99)
        n2 = r.randint(-99,99)
    elif(d==3):
        while n1>100 and n1<-100 and n2>100 and n2<-100:
            n1 = r.randint(-999,999)
            n2 = r.randint(-999,999)
    elif(d==4):
        while n1>1000 and n1<-1000 and n2>1000 and n2<-1000:
            n1 = r.randint(-9999,9999)
            n2 = r.randint(-9999,9999)
    answer=n1-n2
    print("Q.",n1,"-",n2,"= ")
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
        print(f"Incorrect answer. The correct answer was {answer}. No points given.")
        print()
        return c



def Multiply_Rat(d,c):
    if(d==1):
        n1 = r.randint(-10,10)
        n2 = r.randint(-10,10)
    elif(d==2):
        n1 = r.randint(-25,25)
        n2 = r.randint(-25,25)
    elif(d==3):
        n1 = r.randint(-100,100)
        n2 = r.randint(-100,100)
    elif(d==4):
        n1 = r.randint(-999,999)
        n2 = r.randint(-999,999)
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
        print(f"Incorrect answer. The correct answer was {answer}. No points given.")
        print()
        return c



def Divide_Rat(d,c):
    if(d==1):
        n1 = r.randint(-50,50)
        n2 = r.randint(-10,10)
    elif(d==2):
        n1 = r.randint(-500,500)
        n2 = r.randint(-10,10)
    elif(d==3):
        n1 = r.randint(-9999,9999)
        n2 = r.randint(-50,50)
    elif(d==4):
        n1 = r.randint(-99999,99999)
        n2 = r.randint(-99,99)
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
        print(f"Both correct! One point given. \nCorrect quotient : {quotient} \t\t Correct remainder : {remainder}")
        print()
        return c+1
    elif user_q!=quotient and user_r==remainder:
        print(f"Only remainder correct. Half point given. \nCorrect quotient : {quotient} \t\t Correct remainder : {remainder}")
        print()
        return c+0.5
    elif user_q==quotient and user_r!=remainder:
        print(f"Only quotient correct. Half point given. \nCorrect quotient : {quotient} \t\t Correct remainder : {remainder}")
        print()
        return c+0.5
    else:
        print(f"Incorrect answer. No points given. \nCorrect quotient : {quotient} \t\t Correct remainder : {remainder}")
        print()
        return c