"""
1.Create User
2.Request Ride
3.Save Ride History
"""
class User:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        self.ride_history=[]
    def request_ride(self,start_location,end_location):
        self.start_location=start_location
        self.end_location=end_location
        from Ride import Ride
        ride=Ride(self)
        return ride
    def user_ride_history(self,ride):
        self.ride_history.append(ride)