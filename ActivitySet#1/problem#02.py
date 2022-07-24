# Why Program
class Airline:
    def __init__(self,Name,PAN_No,Mobile_no,Email_id,Source,Destination,Seat_No,Air_Fare,Travel_date):
        self.Name=Name
        self.PAN_No=PAN_No
        self.Mobile_no=Mobile_no
        self.Email_id=Email_id
        self.Source=Source
        self.Destination=Destination
        self.Seat_No=Seat_No
        self.Air_Fare=Air_Fare
        self.Travel_date=Travel_date
    def airline_details(self):
        print(self.Name,"\t",self.PAN_No,"\t",self.Mobile_no,"\t",self.Email_id,"\t",self.Source,"\t",self.Destination,"\t",self.Seat_No,"\t",self.Air_Fare,"\t",self.Travel_date)
airlineobject=[]
n=(int(input('Enter the number of passengers:')))
for i in range(n):
    Name=input('Enter the passengers Name:')
    PAN_No=input('Enter PAN_No:')
    Mobile_no=int(input('Enter Moblie no:'))
    Email_id=input('Enter Email id:')
    Source=input('Enter source:')
    Destination=input('Enter the destination:')
    Seat_No=input('Enter the seat no:')
    Air_Fare=input('Enter the air fare:')
    Travel_date=int(input('Enter the travel date:'))
    airlineobject.append(Airline(Name,PAN_No,Mobile_no,Email_id,Source,Destination,Seat_No,Air_Fare,Travel_date))
for obj in airlineobject:
    obj.airline_details()
    