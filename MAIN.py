from Module_Mains import *

while True:
    print("1 : Start/Continue")
    print("0 : Exit")
    startMenu=int(input("Enter your option : "))
    print()
    if startMenu==1:
        while True:
            print("1 : Basic Operations - Whole Numbers")
            print("2 : Basic Operations - Integers")
            print("3 : Basic Operations - Rational")
            print("4 : Area and Perimeter")
            print("5 : Surface Area and Volume")
            print("6 : Linear and Quadratic Equations")
            print("7 : Fractions")
            print("0 : Go Back")
            try:
                topics=int(input("Enter your desired topic : "))
                print()
            except:
                print("Please choose a valid topic.")



            if topics==1:
                while True:
                    print("1 : Addition")
                    print("2 : Subtraction")
                    print("3 : Multiplication")
                    print("4 : Division")
                    print("0 : Go Back")
                    while True:
                        try:
                            operation=int(input("Which operation : "))
                            print()
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                        
                    if operation==1:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Add_Main(ques)
                        goback=True
                        break

                    elif operation==2:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Subtract_Main(ques)
                        goback=True
                        break

                    elif operation==3:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Multiply_Main(ques)
                        goback=True
                        break

                    elif operation==4:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Divide_Main(ques)
                        goback=True
                        break

                    elif operation==0:
                        goback=False
                        break

                    else:
                        print("Invalid input, try again.")
                if goback:
                    break

            

            elif topics==2:
                while True:
                    print("1 : Addition")
                    print("2 : Subtraction")
                    print("3 : Multiplication")
                    print("4 : Division")
                    print("0 : Go Back")
                    while True:
                        try:
                            operation=int(input("Which operation : "))
                            print()
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                        
                    if operation==1:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Add_Int_Main(ques)
                        goback=True
                        break

                    elif operation==2:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Subtract_Int_Main(ques)
                        goback=True
                        break

                    elif operation==3:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Multiply_Int_Main(ques)
                        goback=True
                        break

                    elif operation==4:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Divide_Int_Main(ques)
                        goback=True
                        break

                    elif operation==0:
                        goback=False
                        break

                    else:
                        print("Invalid input, try again.")
                if goback:
                    break

        

            elif topics==3:
                while True:
                    print("1 : Addition")
                    print("2 : Subtraction")
                    print("3 : Multiplication")
                    print("4 : Division")
                    print("0 : Go Back")
                    while True:
                        try:
                            operation=int(input("Which operation : "))
                            print()
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                        
                    if operation==1:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Add_Main(ques)
                        goback=True
                        break

                    elif operation==2:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Subtract_Main(ques)
                        goback=True
                        break

                    elif operation==3:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Multiply_Main(ques)
                        goback=True
                        break

                    elif operation==4:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        Divide_Main(ques)
                        goback=True
                        break

                    elif operation==0:
                        goback=False
                        break

                    else:
                        print("Invalid input, try again.")
                if goback:
                    break



            elif topics==4:
                while True:
                    print("1 : Square")
                    print("2 : Rectangle")
                    print("3 : Trapezium")
                    print("4 : Circle")
                    print("0 : Go Back")
                    while True:
                        try:
                            shape=int(input("Which shape : "))
                            print()
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                    print()
                    
                    if shape==1:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        AP_Square_Main(ques)
                        goback=True
                        break

                    elif shape==2:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        AP_Rectangle_Main(ques)
                        goback=True
                        break

                    elif shape==3:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        AP_Trapezium_Main(ques)
                        goback=True
                        break

                    elif shape==4:
                        ques=input("How many questions : ")
                        if not str(ques).isdigit():
                            print("Invalid Input. Please try again.")
                            continue
                        ques=int(ques)
                        AP_Circle_Main(ques)
                        goback=True
                        break

                    elif shape==0:
                        goback=False
                        break

                    else:
                        print("Invalid input, try again.")
                if goback:
                    break
            


            elif topics==5:
                while True:
                    print("1 : Cube")
                    print("2 : Cuboid")
                    print("3 : Sphere")
                    print("4 : Cone")
                    print("5 : Cylinder")
                    print("0 : Go Back")
                    while True:
                        try:
                            shape=int(input("Which shape : "))
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                    print()
                
                    if shape==1:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            SAaV_Cube_Main(ques)
                            goback=True
                            break
                    elif shape==2:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            SAaV_Cuboid_Main(ques)
                            goback=True
                            break
                    elif shape==3:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            SAaV_Sphere_Main(ques)
                            goback=True
                            break
                    elif shape==4:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            SAaV_Cone_Main(ques)
                            goback=True
                            break
                    elif shape==5:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            SAaV_Cylinder_Main(ques)
                            goback=True
                            break
                    elif shape==0:
                        goback=False
                        break
                if goback:
                    break
            


            elif topics==6:
                while True:
                    print("1 : Solution of Linear Equations of Single Variable")
                    print("0 : Go Back")
                    while True:
                        try:
                            choice=int(input("Which shape : "))
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                    print()
                
                    if choice==1:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            LE_Single_Main(ques)
                            goback=True
                            break
                    
                    elif choice==0:
                        goback=False
                        break
                if goback:
                    break
        
            elif topics==7:
                while True:
                    print("1 : Types of Fraction")
                    print("2 : Convert Fractions to Decimal")
                    print("3 : Sum of Fractions")
                    print("4 : Difference of Fractions")
                    print("0 : Go Back")
                    while True:
                        try:
                            choice=int(input("Which subtopic : "))
                            break
                        except:
                            print("Invalid input. Please enter a valid option.")
                    print()
                
                    if choice==1:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            Fraction_Type_Main(ques)
                            goback=True
                            break
                    
                    if choice==2:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            FracToDec_Main(ques)
                            goback=True
                            break
                    
                    if choice==3:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            AddFrac_Main(ques)
                            goback=True
                            break
                    
                    if choice==4:
                            ques=input("How many questions : ")
                            if not str(ques).isdigit():
                                print("Invalid Input. Please try again.")
                                continue
                            ques=int(ques)
                            SubtractFrac_Main(ques)
                            goback=True
                            break
                    
                    elif choice==0:
                        goback=False
                        break
                if goback:
                    break


            elif topics==0:
                break
            
    elif startMenu==0:
        break

    else:
        print("Invalid input, try again.")