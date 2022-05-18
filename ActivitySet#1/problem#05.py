# Functions


def computepay(hrs,rate):
    if hrs<=40:
        pay=hrs*rate
    else:
        pay=(40*rate)+((hrs-40)*rate*1.5)
	return pay

hrs=float(input("Enter hours: "))
rate=float(input("Enter the rate per hour:"))
pay= computepay(hrs,rate)
print("Pay",pay) 