"""
1.Create a user
2.Request a ride
3.Save Ride History
"""
from Ride import Ride
class User:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        self.ride_history=[]
    def request_ride(self,start_location,end_location):
        self.start_location=start_location
        self.end_location=end_location
        self.ride=Ride(self)
        return self.ride
    def user_ride_history(self):
        self.ride_history.append(self.ride)
u1=User("Nusrat","nusrat@gmail.com","018476554")
u1.request_ride("Banani","Mirpur")
print(u1.__dict__)
