import random as r
import HCF_LCM_Module as hl

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
        print(f"Incorrect answer. The correct type was {type_answer} No points awarded.")
    
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

def AddFrac(d,count):
    if d==1:
        nume1=r.randint(1,10)
        denom1=r.randint(1,10)
        if nume1>denom1:
            nume1, denom1 == denom1, nume1
        nume2=r.randint(1,10)
        denom2=r.randint(1,10)
        if nume2>denom2:
            nume2, denom2 == denom2, nume2
    
    elif d==2:
        nume1=r.randint(1,25)
        denom1=r.randint(1,25)
        nume2=r.randint(1,25)
        denom2=r.randint(1,25)
    
    elif d==3:
        numlist=[x for x in range(-30,30) if x!=0 or x!=1 or x!=-1]
        nume1=numlist[r.randint(0,len(numlist)-1)]
        denom1=numlist[r.randint(0,len(numlist)-1)]
        nume2=numlist[r.randint(0,len(numlist)-1)]
        denom2=numlist[r.randint(0,len(numlist)-1)]

        if nume1<0 and denom1<0:
            nume1, denom1 = -nume1, -denom1
        if nume2<0 and denom2<0:
            nume2, denom2 = -nume2, -denom2

    frac1=f'{nume1}/{denom1}'
    frac2=f'{nume2}/{denom2}'
        
    if denom1==denom2:
        denom_s=denom1
        nume_s = nume1+nume2
        if nume_s>denom_s:
            smaller = denom_s
        else:
            smaller = nume_s
        for i in range(2,smaller+1):
            if nume_s%i==0 and denom_s%i==0:
                while nume_s%i and denom_s%i:
                    nume_s, denom_s = nume_s%i, denom_s%i
        
        if nume_s<0 and denom_s<0:
            nume_s, denom_s = -nume_s, -denom_s
        frac_sum = f"{nume_s}/{denom_s}"
    
    elif denom1!=denom2:
        denom_s=hl.compute_lcm(denom1,denom2)
        nume_s = (nume1*(denom_s//denom1)) + (nume2*(denom_s//denom2))
        if nume_s>denom_s:
            smaller = denom_s
        else:
            smaller = nume_s
        for i in range(2,smaller+1):
            if nume_s%i==0 and denom_s%i==0:
                while nume_s%i and denom_s%i:
                    nume_s, denom_s = nume_s%i, denom_s%i
        
        if nume_s<0 and denom_s<0:
            nume_s, denom_s = -nume_s, -denom_s
        frac_sum = f"{nume_s}/{denom_s}"
        

    print("Find the sum of the fractions in simplified form: ",frac1,"+",frac2)
    frac_user=input("Sum : ")

    if frac_user==frac_sum:
        print("Correct answer. One point awarded")
        count+=1
    else:
        print(f"Wrong answer. The correct answer is {frac_sum} No points awarded")
    
    return count



def SubtractFrac(d,count):
    if d==1:
        nume1=r.randint(1,10)
        denom1=r.randint(1,10)
        if nume1>denom1:
            nume1, denom1 == denom1, nume1
        nume2=r.randint(1,10)
        denom2=r.randint(1,10)
        if nume2>denom2:
            nume2, denom2 == denom2, nume2
    
    elif d==2:
        nume1=r.randint(1,25)
        denom1=r.randint(1,25)
        nume2=r.randint(1,25)
        denom2=r.randint(1,25)
    
    elif d==3:
        numlist=[x for x in range(-30,30) if x!=0 or x!=1 or x!=-1]
        nume1=numlist[r.randint(0,len(numlist)-1)]
        denom1=numlist[r.randint(0,len(numlist)-1)]
        nume2=numlist[r.randint(0,len(numlist)-1)]
        denom2=numlist[r.randint(0,len(numlist)-1)]

        if nume1<0 and denom1<0:
            nume1, denom1 = -nume1, -denom1
        if nume2<0 and denom2<0:
            nume2, denom2 = -nume2, -denom2

    frac1=f'{nume1}/{denom1}'
    frac2=f'{nume2}/{denom2}'
        
    if denom1==denom2:
        denom_s=denom1
        nume_s = nume1-nume2
        if nume_s>denom_s:
            smaller = denom_s
        else:
            smaller = nume_s
        for i in range(2,smaller+1):
            if nume_s%i==0 and denom_s%i==0:
                while nume_s%i and denom_s%i:
                    nume_s, denom_s = nume_s%i, denom_s%i
        
        if nume_s<0 and denom_s<0:
            nume_s, denom_s = -nume_s, -denom_s
        frac_diff = f"{nume_s}/{denom_s}"
    
    elif denom1!=denom2:
        denom_s=hl.compute_lcm(denom1,denom2)
        nume_s = (nume1*(denom_s//denom1)) - (nume2*(denom_s//denom2))
        if nume_s>denom_s:
            smaller = denom_s
        else:
            smaller = nume_s
        for j in range(2,smaller+1):
            if nume_s%j==0 and denom_s%j==0:
                while nume_s%j and denom_s%j:
                    nume_s, denom_s = nume_s%j, denom_s%j
        
        if nume_s<0 and denom_s<0:
            nume_s, denom_s = -nume_s, -denom_s
        frac_diff = f"{nume_s}/{denom_s}"
        

    print("Find the difference of the fractions in simplified form: ",frac1,"-",frac2)
    frac_user=input("Difference : ")

    if frac_user==frac_diff:
        print("Correct answer. One point awarded")
        count+=1
    else:
        print(f"Wrong answer. The correct answer is {frac_diff} No points awarded")
    
    return count