import random
class BRTA:
    def driving_test(self,email):
        score=random.randint(0,100)
        filtered=[]
        if score >= 33:
            license_number = random.randint(5000, 9999)

            # Step-1: Read file
            with open("license.txt", "r") as f:
                lines = f.readlines()

            # Step-2: Filter old entry
            filtered = [line for line in lines if email not in line]

            # Step-3: Rewrite file with updated list
            with open("license.txt", "w") as f:
                f.writelines(filtered)

            # Step-4: Append new license info
            with open("license.txt", "a") as f:
                f.write(f"{email}:{license_number}\n")

            print(f"Congrats, you passed! Score: {score}, License: {license_number}")
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
b.driving_test("mahadi@gmail.com")
# b.driving_test("mehedi@gmail.com")
# nu=b.validate_license("akash@gmail.com","9872")
# print(nu)

