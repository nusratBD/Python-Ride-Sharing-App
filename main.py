from User import User
from Driver import Driver
from Ride import Ride
"""
#User class
1)User Create করব
২)User Ride Request করবে
৩)User এর ride history update করব
৪)User ride_history করব 
"""
u1=User("Nusrat","nusrat@gmail.com","07543q768")
# print(u1.__dict__)
ride1=u1.request_ride("Mirpur","Banani")
# print(ride1.__dict__)
# u1.user_ride_history(ride1)
# print(u1.ride_history[0].driver)
"""
1.Driver create করব। 
"""
d1=Driver("Akash","akash@gmail.com","087565436899")
# print(d1.__dict__)
r1=Ride(u1)
print(r1.__dict__)
r1.assign_driver(d1)
print(r1.__dict__)
r1.complete_ride(700)
print(r1.driver.__dict__)


