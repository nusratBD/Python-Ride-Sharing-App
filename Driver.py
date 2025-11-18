"""
1.Create Driver
2.Accept Ride Request
"""
from User import User
class Driver(User):
    def __init__(self,name,email,phone):
        super().__init__(name,email,phone)
        self.availability=True