import random
class BRTA:
    def driving_test(self,email):
        score=random.randint(0,100)
        if score>=33:
            license_number=random.randint(5000,9999)
            with open("license.txt","a") as f:
                f.write(f"{email}:{license_number}\n")
            print(f"Congrats, you have passed. Your score is {score}. And your license number is {license_number}")
            return license_number
        else:
            print(f"Sorry you have failed the test. Your score is {score}")
            return False
    def validate_license(self,email,license_number):
        with open("license.txt","r") as f:
            lines=f.read().split("\n")
            for line in lines:
                line_value=line.split(":")
                if line_value[0]==email and line_value[1]==license_number:
                    return True
            return False

b=BRTA()
# b.driving_test("nusrat@gmail.com")
# b.driving_test("mehedi@gmail.com")
nu=b.validate_license("akash@gmail.com","9872")
print(nu)

