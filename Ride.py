class Ride:
    def __init__(self,user,driver=None,status="Pending",fare=0):
        self.user=user
        self.driver=driver
        self.status=status
        self.fare=fare
    def assign_driver(self,driver):
        self.driver=driver
        driver.availability=False
        self.status="Accepted"
    def complete_ride(self,fare):
        self.driver.availability=True
        self.fare=fare
        self.status="Completed"