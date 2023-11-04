import random as r
def AP_Square(d,c):
    if d==1:
        s=r.randint(1,20)
    elif d==2:
        s=r.randint(21,50)
    elif d==3:
        s=r.randint(51,99)
    area=s**2
    perimeter=4*s
    print("Q. Find the area and perimeter of a square of side",s,": ")
    while True:
        try:
            user_a=int(input("Area : "))
            user_p=int(input("Perimeter : "))
            break
        except:
            print("Invalid input. Please enter an integer.")
    if user_a==area and user_p==perimeter:
        print("Both are correct! One point awarded.")
        print()
        return c+1
    elif user_a==area and user_p!=perimeter:
        print(f"Only area is correct. Half point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+0.5
    elif user_a!=area and user_p==perimeter:
        print(f"Only perimeter is correct. Half point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+0.5
    else:
        print(f"Incorrect answer. No points given. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c

def AP_Rectangle(d,c):
    if d==1:
        l=r.randint(1,20)
        b=r.randint(1,20)
    elif d==2:
        l=r.randint(21,50)
        b=r.randint(21,50)
    elif d==3:
        l=r.randint(51,99)
        b=r.randint(51,99)
    area=l*b
    perimeter=2*(l+b)
    print("Q. Find the area and perimeter of a rectangle of length",l,"and breadth",b,": ")
    while True:
        try:
            user_a=int(input("Area : "))
            user_p=int(input("Perimeter : "))
            break
        except:
            print("Invalid input. Please enter an integer.")
    if user_a==area and user_p==perimeter:
        print("Both are correct! One point awarded")
        print()
        return c+1
    elif user_a==area and user_p!=perimeter:
        print(f"Only area is correct. Half point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+0.5
    elif user_a!=area and user_p==perimeter:
        print(f"Only perimeter is correct. Half point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+0.5
    else:
        print(f"Incorrect answer. No points given. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c
    

def AP_Trapezium(c):
    pside1=r.randint(2,25)
    pside2=r.randint(2,25)
    side1=r.randint(2,25)
    side2=r.randint(2,25)
    h=r.randint(10,30)
    area=0.5*h*(pside1+pside2)
    perimeter=pside1+pside2+side1+side2
    print("Q. Find the area and perimeter of the parallelogram with the following values : \nParallel Sides =",pside1,"and",pside2,"\nNon-Parallel Sides =",side1,"and",side2,"\nDistance between Parallel Sides =",h)
    while True:
        try:
            user_a=float(input("Area : "))
            user_p=float(input("Perimeter : "))
            break
        except:
            print("Invalid input. Please enter a real number.")
    if user_a==area and user_p==perimeter:
        print(f"Both are correct! One point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+1
    elif user_a==area and user_p!=perimeter:
        print(f"Only area is correct. Half point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+0.5
    elif user_a!=area and user_p==perimeter:
        print(f"Only perimeter is correct. Half point awarded. \nCorrect area : {area} \t\t Correct perimeter : {perimeter}")
        print()
        return c+0.5
    else:
        print("Incorrect answer. No points given.")
        print()
        return c


def AP_Circle(d,c):
    if d==1:
        rad=r.randint(1,11)
    elif d==2:
        rad=r.randint(1,77)
    circum=2*3.14*rad
    area=3.14*rad**2
    print("Enter the circumference and area of the circle whose radius is",rad,"(pi=3.14) : ")
    while True:
        try:
            user_a=float(input("Area = "))
            user_c=float(input("Circumference = "))
            break
        except:
            print("Invalid input, please try again.")
    if user_a==area and user_c==circum:
        print("Both are correct. One point awarded.")
        print()
        return c+1
    elif user_a!=area and user_c==circum:
        print(f"Only circumference is correct. Half point awarded. \nCorrect area : {area} \t\t Correct circumference : {circum}")
        print()
        return c+0.5
    elif user_a==area and user_c!=circum:
        print(f"Only area is correct. Half point awarded. \nCorrect area : {area} \t\t Correct circumference : {circum}")
        print()
        return c+0.5
    else:
        print(f"None are correct. No points awarded. \nCorrect area : {area} \t\t Correct circumference : {circum}")
        print()
        return c