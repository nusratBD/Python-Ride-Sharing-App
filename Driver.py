"""
1.Create Driver
2.Accept Ride Request
"""
from User import User
from Brta import BRTA
authority=BRTA()
class Driver(User):
    def __init__(self,name,email,phone,license_number):
        super().__init__(name,email,phone)
        self.availability=True
        self.license_number=license_number
        self.valid_driver=authority.validate_license(email,license_number)
# d1=Driver("Akash","nusrat@gmail.com","01708778173","5360")
# print(d1.__dict__)

