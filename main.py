from User import User
from Brta import BRTA
from Driver import Driver
from Ride import Ride

"""
#User class
1)User Create করব
২)User Ride Request করবে
৩)User এর ride history update করব
৪)User ride_history করব 
"""
# u1=User("Nusrat","nusrat@gmail.com","07543q768")
# print(u1.__dict__)
#ride1=u1.request_ride("Mirpur","Banani")
# print(ride1.__dict__)
# u1.user_ride_history(ride1)
# print(u1.ride_history[0].driver)
"""
1.Driver create করব। 
"""
b=BRTA()
b.driving_test("nusrat@gmail.com")
b.driving_test("nusrat1@gmail.com")
b_result=b.get_license()
print(b_result)
for value in b_result:
    print(value)

# b1=b.driving_test("nusrat@gmail.com")


