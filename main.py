from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)




print("========= MINI-PROJECT=========")
print("[1] Create donor account")
print("[2] View donor")
print("[3] Search donor")
print("[4] Eligibilty Criteria")
print("[5] Request Blood")
print("[6] Blood Stock")
print("[7] Exit")
print("===============================")





donor={}


while(True):
    option = int(input("Enter your option: "))


    if option == 1:
        phone_num = int(input("Enter your phone number: "))
        if phone_num in donor:
            print("Phone number already exists. Try again!")
        else:
            username = input("Enter your username: ")
            blood_group = input("Enter blood group: ")
            otp = int(input("Enter the given OTP number: "))

            donor[phone_num] = {
                "username": username,
                "blood_group": blood_group,
                "otp": otp
            }

            print("Donor Account Created")



    elif option == 2:
        for phone_num in donor:
            print("Phone:", phone_num)
            print("Username:", donor[phone_num]["username"])
            print("Blood Group:", donor[phone_num]["blood_group"])
            print()



    elif option == 3:
        phone_num = int(input("Enter phone number to search: "))

        if phone_num in donor:
            print("Username:", donor[phone_num]["username"])
            print("Blood Group:", donor[phone_num]["blood_group"])
        else:
            print("Donor not found!")



    elif option == 4:
        age = int(input("Enter age: "))
        weight = float(input("Enter weight in kilograms: "))

        if age >= 18 and age <= 65 and weight >= 50:
            print("Eligible to donate blood")
        else:
            print("Not eligible to donate blood")



    elif option == 5:
        blood_group = input("Enter required blood group: ")

        for phone_num in donor:
            if donor[phone_num]["blood_group"] == blood_group:
                print("Username:", donor[phone_num]["username"])



    elif option == 6:
        for phone_num in donor:
            print("Blood Group:", donor[phone_num]["blood_group"])

    else:
        print("Thank you for helping save lives through blood donation!")

     