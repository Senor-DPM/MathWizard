import random as r

def Fraction_Type(count):
    Type_List=["U","P","I"]
    nume = r.randint(1,100)
    denom = r.randint(2,100)
    frac = f'{nume}/{denom}'
    
    if nume<denom and nume==1:
        type_answer="U"
    elif nume<denom:
        type_answer="P"
    elif nume>denom:
        type_answer="I"
    
    print("Determine the type of fraction : "+frac,)
    print("Possible Types : Proper(P), Improper(I), Unit(U)")
    while True:
        try:
            user_type = input("Type (Using a single letter): ")
            user_type=user_type.upper()
            if len(user_type) == 1 and user_type.isalpha() and (user_type in Type_List):
                break
            else:
                print("Invalid Input. Please enter a single letter.")
        except:
            print("Enter a single letter only. Please try again.")
    if type_answer==user_type:
        print("Correct answer. One point awarded.")
        count+=1
    elif type_answer!=user_type:
        print("Incorrect answer. No points awarded.")
    
    return count

def FracToDec(d,count):
    if d==1:
        nume = r.randint(1,10)
        denom = r.randint(2,15)
    elif d==2:
        nume = r.randint(1,20)
        denom=r.randint(11,40)
    elif d==3:
        nume = r.randint(21,50)
        denom=r.randint(31,101)
    
    frac=f'{nume}/{denom}'
    deci=round(nume/denom,2)

    print("Convert the following fraction to decimal : "+frac)
    while True:
        try:
            user_dec = float(input("Decimal form : "))
            break
        except ValueError:
            print("Invalid Input. Please try again.")
    if user_dec==deci:
        print("Correct answer! One point awarded.")
        count+=1
    elif user_dec!=deci:
        print(f"Wrong answer. The correct answer was {deci}.No points given.")
    
    return count