d = {}
l = []
n = int(input("Enter no. of students: "))
for i in range(n):
    name = input("Enter the name of student: ")
    eng = int(input("Marks in English: "))
    maths = int(input("Marks in Maths: "))
    cs = int(input("Marks in CS: "))
    l = [eng, maths, cs]
    d[name] = l

print(d)

for k in d:
    l1 = []
    l1 = d[k]
    s = 0
    for j in l1:
        s = s + j    # Total marks
        p = s/3      # % age marks
    print(k, ":", p, "%")