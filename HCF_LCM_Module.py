def compute_gcd(x, y):
    while(y):
       x, y = y, x % y
    hcf=x
    return hcf

def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x,y)
    return lcm