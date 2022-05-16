# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate per hour")
r=float(rate)
if h<=40:
    pay=h*r
if h>40:
    x=h-40
    pay=(40*r)+(x*r*1.5)
print(pay)


#conditional execution problem 2
score = float(input("Enter Score: "))
if 0.0<score<1.0:
    if score>=0.9:
        print("A")
    elif 0.8<=score<0.9:
        print("B")
    elif 0.7<=score<0.8:
        print("C")
    elif 0.6<=score<0.7:
        print("D")
    elif score<0.6:
        print("F")
else:
    print("The given value is out of range")