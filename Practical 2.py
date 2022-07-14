def cal_si(p,r,t):
    return p*r*t/100

p = int(input("Enter principal value: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))
i = cal_si(p,r,t)
print("Total amount incl. interest",p + i)