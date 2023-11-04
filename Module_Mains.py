from DMAS_Whole_Module import *
from AreaPerimeter_Module import *
from SAaV_Module import *
from Lin_Quad_Equa_Module import *
from DMAS_INT_Module import *
from DMAS_RAT_Module import *
from Fractions_Module import *

def Add_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Add_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Add(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Subtract_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Subtract_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Subtract(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Multiply_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Multiply_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Multiply(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Divide_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Divide_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Divide(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

#-----------------------------------------------------------------------------------------------------------------------------------------------

def Add_Int_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-4) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Add_Int_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Add_Int(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Subtract_Int_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Subtract_Int_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Subtract_Int(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Multiply_Int_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Multiply_Int_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Multiply_Int(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Divide_Int_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Divide_Int_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Divide_Int(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

#-----------------------------------------------------------------------------------------------------------------------------------------------

def Add_Rat_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Add_Rat_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Add_Rat(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Subtract_Rat_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Subtract_Rat_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Subtract_Rat(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Multiply_Rat_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Multiply_Rat_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Multiply_Rat(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

def Divide_Rat_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3,4]:
        print("Error. Try again please.")
        Divide_Rat_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=Divide_Rat(diff,count)

        print("You have earned ",count," out of ",ques," points.")
        print()

#-----------------------------------------------------------------------------------------------------------------------------------------------

def AP_Square_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3]:
        print("Invalid input. Try again please.")
        AP_Square_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=AP_Square(diff,count)
        
        print("You have earned ",count," out of ",ques," points.")
    print()

def AP_Rectangle_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3]:
        print("Invalid input. Try again please.")
        AP_Rectangle_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=AP_Rectangle(diff,count)
        
        print("You have earned ",count," out of ",ques," points.")
    print()

def AP_Trapezium_Main(ques):
    print()
    count=0
    for i in range(0,ques):
        count=AP_Trapezium(count)
        
    print("You have earned",count,"out of",ques,"points.")
    print()

def AP_Circle_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invlaid Input. Please try again.")
        AP_Circle_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=AP_Circle(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

#----------------------------------------------------------------------------------------------------------------------------------------------

def SAaV_Cube_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invalid Input. Please try again.")
        SAaV_Cube_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=SAaV_Cube(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def SAaV_Cuboid_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invalid Input. Please try again.")
        SAaV_Cuboid_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=SAaV_Cuboid(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def SAaV_Sphere_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invalid Input. Please try again.")
        SAaV_Sphere_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=SAaV_Sphere(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def SAaV_Cone_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invalid Input. Please try again.")
        SAaV_Cone_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=SAaV_Cone(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def SAaV_Cylinder_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invalid Input. Please try again.")
        SAaV_Cylinder_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=SAaV_Cylinder(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

#----------------------------------------------------------------------------------------------------------------------------------------------

def LE_Single_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-2) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2]:
        print("Invalid Input. Please try again.")
        LE_Single_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=LE_Single(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

#----------------------------------------------------------------------------------------------------------------------------------------------

def Fraction_Type_Main(ques):
    count=0
    for i in range(0,ques):
        count=Fraction_Type(count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def FracToDec_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-3) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3]:
        print("Invalid Input. Please try again.")
        FracToDec_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=FracToDec(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def AddFrac_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-3) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3]:
        print("Invalid Input. Please try again.")
        AddFrac_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=AddFrac(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()

def SubtractFrac_Main(ques):
    while True:
        try:
            diff = int(input("Enter the difficulty(1-3) : "))
            print()
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if diff not in [1,2,3]:
        print("Invalid Input. Please try again.")
        SubtractFrac_Main(ques)
    else:
        count=0
        for i in range(0,ques):
            count=SubtractFrac(diff,count)
    
    print("You have earned",count,"out of",ques,"points.")
    print()