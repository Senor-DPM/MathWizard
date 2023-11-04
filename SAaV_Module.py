import random as r

def SAaV_Cube(d,c):
    if d==1:
        s=r.randint(2,10)
    elif d==2:
        s=r.randint(11,30)
    TSA=6*s**2
    CSA=4*s**2
    Vol=s**3

    print("Enter the total surface area(TSA), curved surface area(CSA) and Volume of a cube of side",s,":")
    while True:
        try:
            user_tsa = int(input("TSA = "))
            user_csa = int(input("CSA = "))
            user_v = int(input("Volume = "))
            break
        except ValueError:
            print("Invalid input, please try again.")
    if(user_tsa==TSA) and (user_csa==CSA) and (user_v==Vol):
        print("All are correct. 3 points awarded.")
        c+=3
    elif(user_tsa==TSA) and (user_csa==CSA) and (user_v!=Vol):
        print("Only TSA & CSA are correct. 2 points awarded")
        c+=2
    elif(user_tsa==TSA) and (user_csa!=CSA) and (user_v==Vol):
        print("Only TSA & volume are correct. 2 points awarded")
        c+=2
    elif(user_tsa!=TSA) and (user_csa==CSA) and (user_v==Vol):
        print("Only CSA & volume are correct. 2 points awarded")
        c+=2
    elif(user_tsa==TSA) and (user_csa!=CSA) and (user_v!=Vol):
        print("Only TSA is correct. 1 point awarded")
        c+=1
    elif(user_tsa!=TSA) and (user_csa==CSA) and (user_v!=Vol):
        print("Only CSA is correct. 1 point awarded")
        c+=1
    elif(user_tsa!=TSA) and (user_csa!=CSA) and (user_v==Vol):
        print("Only volume is correct. 1 point awarded")
        c+=1
    else:
        print("No correct answer. No points awarded.")
    return c

def SAaV_Cuboid(d,c):
    if d == 1:
        l = r.randint(2, 10)
        w = r.randint(2, 10)
        h = r.randint(2, 10)
    elif d == 2:
        l = r.randint(11, 30)
        w = r.randint(11, 30)
        h = r.randint(11, 30)

    TSA = 2 * (l * w + w* h + h * l)
    CSA = 2 * h * (l + w)
    Volume = l * w * h

    print("Enter the total surface area(TSA), curved surface area(CSA), and Volume of a cuboid with dimensions :")
    print("Length :",l)
    print("Width :",w)
    print("Height :",h)

    while True:
        try:
            user_tsa = int(input("TSA = "))
            user_csa = int(input("CSA = "))
            user_v = int(input("Volume = "))
            break
        except ValueError:
            print("Invalid input, please try again.")

    if (user_tsa == TSA) and (user_csa == CSA) and (user_v == Volume):
        print("All answers are correct. 3 points awarded.")
        c += 3
    elif (user_tsa == TSA) and (user_csa == CSA) and (user_v != Volume):
        print("Only TSA and CSA are correct. 2 points awarded.")
        c += 2
    elif (user_tsa == TSA) and (user_csa != CSA) and (user_v == Volume):
        print("Only TSA and Volume are correct. 2 points awarded.")
        c += 2
    elif (user_tsa != TSA) and (user_csa == CSA) and (user_v == Volume):
        print("Only CSA and Volume are correct. 2 points awarded.")
        c += 2
    elif (user_tsa == TSA) and (user_csa != CSA) and (user_v != Volume):
        print("Only TSA is correct. 1 point awarded.")
        c += 1
    elif (user_tsa != TSA) and (user_csa == CSA) and (user_v != Volume):
        print("Only CSA is correct. 1 point awarded.")
        c += 1
    elif (user_tsa != TSA) and (user_csa != CSA) and (user_v == Volume):
        print("Only Volume is correct. 1 point awarded.")
        c += 1
    else:
        print("No correct answers. 0 points awarded.")
    return c

def SAaV_Sphere(d,c):
    allCorrect=False
    if d == 1:
        rad = r.randint(2, 10)
    elif d == 2:
        rad = r.randint(11, 30)

    TSA = 4 * 3.14 * (rad ** 2)  # Total Surface Area formula
    Volume = (4/3) * 3.14 * (rad ** 3)  # Volume formula
    TSA=round(TSA,2)
    Volume=round(Volume,2)

    print("Enter the Total Surface Area (TSA) and Volume of a sphere with radius (Take pi = 3.14):")
    print("Radius:", rad)

    while True:
        try:
            user_tsa = float(input("TSA(To 2 decimal places) = "))
            user_v = float(input("Volume(To 2 decimal places) = "))
            break
        except ValueError:
            print("Invalid input, please try again.")

    if (user_tsa == TSA) and (user_v == Volume):
        print("Both answers are correct. 2 points awarded.")
        c += 2
        allCorrect=True
    elif (user_tsa == TSA) or (user_v == Volume):
        print("One answer is correct. 1 point awarded.")
        c += 1
    else:
        print("Neither answer is correct. No points awarded.")
    if not allCorrect:
        print("Correct Answers : ")
        print("TSA =",TSA)
        print("Volume :",Volume)
        print()
    return c

def SAaV_Cone(d, c):
    if d == 1:
        rad = r.randint(2, 10)  # Radius of the cone
        h = r.randint(2, 10)  # Height of the cone
    elif d == 2:
        rad = r.randint(11, 30)
        h = r.randint(11, 30)

    TSA = 3.14 * rad * (rad + (rad**2 + h**2)**0.5)  # Total Surface Area formula
    CSA = 3.14 * rad * (rad**2 + h**2)**0.5  # Curved Surface Area formula
    Volume = (1/3) * 3.14 * rad**2 * h  # Volume formula
    TSA=round(TSA,2)
    CSA=round(CSA,2)
    Volume=round(Volume,2)
    print("Enter the Total Surface Area (TSA), Curved Surface Area (CSA), and Volume of a cone with dimensions(Use pi = 3.14): ")
    print("Radius:", rad)
    print("Height:", h)

    while True:
        try:
            user_tsa = float(input("TSA(To 2 decimal places) = "))
            user_csa = float(input("CSA(To 2 decimal places) = "))
            user_v = float(input("Volume(To 2 decimal places) = "))
            break
        except ValueError:
            print("Invalid input, please try again.")

    if (user_tsa == TSA) and (user_csa == CSA) and (user_v == Volume):
        print("All answers are correct. 3 points awarded.")
        c += 3
    elif (user_tsa == TSA) and (user_csa == CSA) and (user_v != Volume):
        print("Only TSA and CSA are correct. 2 points awarded.")
        c += 2
    elif (user_tsa == TSA) and (user_csa != CSA) and (user_v == Volume):
        print("Only TSA and Volume are correct. 2 points awarded.")
        c += 2
    elif (user_tsa != TSA) and (user_csa == CSA) and (user_v == Volume):
        print("Only CSA and Volume are correct. 2 points awarded.")
        c += 2
    elif (user_tsa == TSA) and (user_csa != CSA) and (user_v != Volume):
        print("Only TSA is correct. 1 point awarded.")
        c += 1
    elif (user_tsa != TSA) and (user_csa == CSA) and (user_v != Volume):
        print("Only CSA is correct. 1 point awarded.")
        c += 1
    elif (user_tsa != TSA) and (user_csa != CSA) and (user_v == Volume):
        print("Only Volume is correct. 1 point awarded.")
        c += 1
    else:
        print("No answer is correct. No points awarded.")
    
    return c

def SAaV_Cylinder(d, c):
    if d == 1:
        radius = r.randint(2, 10)  # Radius of the cylinder
        height = r.randint(2, 10)  # Height of the cylinder
    elif d == 2:
        radius = r.randint(11, 30)
        height = r.randint(11, 30)
    
    TSA = 2 * 3.14 * radius * (radius + height)  # Total Surface Area formula
    CSA = 2 * 3.14 * radius * height  # Curved Surface Area formula
    Volume = 3.14 * radius ** 2 * height  # Volume formula
    TSA = round(TSA, 2)
    CSA = round(CSA, 2)
    Volume = round(Volume, 2)

    print("Enter the Total Surface Area (TSA), Curved Surface Area (CSA), and Volume of a cylinder with dimensions (Use pi = 3.14): ")
    print("Radius:", radius)
    print("Height:", height)

    while True:
        try:
            user_tsa = float(input("TSA(To 2 decimal places) = "))
            user_csa = float(input("CSA(To 2 decimal places) = "))
            user_v = float(input("Volume(To 2 decimal places) = "))
            break
        except ValueError:
            print("Invalid input, please try again.")

    if (user_tsa == TSA) and (user_csa == CSA) and (user_v == Volume):
        print("All answers are correct. 3 points awarded.")
        c += 3
    elif (user_tsa == TSA) and (user_csa == CSA) and (user_v != Volume):
        print("Only TSA and CSA are correct. 2 points awarded.")
        c += 2
    elif (user_tsa == TSA) and (user_csa != CSA) and (user_v == Volume):
        print("Only TSA and Volume are correct. 2 points awarded.")
        c += 2
    elif (user_tsa != TSA) and (user_csa == CSA) and (user_v == Volume):
        print("Only CSA and Volume are correct. 2 points awarded.")
        c += 2
    elif (user_tsa == TSA) and (user_csa != CSA) and (user_v != Volume):
        print("Only TSA is correct. 1 point awarded.")
        c += 1
    elif (user_tsa != TSA) and (user_csa == CSA) and (user_v != Volume):
        print("Only CSA is correct. 1 point awarded.")
        c += 1
    elif (user_tsa != TSA) and (user_csa != CSA) and (user_v == Volume):
        print("Only Volume is correct. 1 point awarded.")
        c += 1
    else:
        print("No answer is correct. No points awarded.")

    return c