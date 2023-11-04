import random as r
import math

def LE_Single(d,count):
    if d == 1:
        a = r.randint(1, 5)
        b = r.randint(1, 5)
        c = a * r.randint(1, 10) + b
    elif d == 2:
        a = r.randint(6, 15)
        b = r.randint(6, 15)
        c = a * r.randint(11, 20) + b
    elif d == 3:
        a = r.randint(16, 30)
        b = r.randint(16, 30)
        c = a * r.randint(21, 40) + b
    elif d == 4:
        a = round(r.uniform(0.5, 5.0), 1)
        b = round(r.uniform(0.5, 5.0), 1)
        c = round(r.uniform(1.0, 10.0), 1)
    else:
        print("Invalid difficulty level. Please choose 1, 2, 3, or 4.")
        return

    print(f"Solve the linear equation: {a}x + {b} = {c}")

    while True:
        try:
            user_solution = float(input("Enter your solution for x(Till two decimal points): "))
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")

    expected_solution = (c - b) / a

    if user_solution == expected_solution:
        print("Correct! Your solution is accurate. One point awarded.")
        count+=1
    else:
        print(f"Sorry, that's not correct. The correct solution is x = {expected_solution:.2f}. No point awarded.")
    
    return count

