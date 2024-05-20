email = input("Enter your email account: ")
Valid_character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,_-"
check, check1 = 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if ("." in email[-4:] or "." in email[-3:]) and email.count(".") == 1:
                for character in email:
                    if character not in Valid_character:
                        print("invalid Email.")
                        break
                else:
                    print("Valid Email..")
            else:
                print("Wrong Email 4")
        else:
            print("Invalid Email: Using @ symbol only once.l̥")
    else:
        print("Invalid Email : First character must be alphabet.")
else:
    print("Invalid Email: Email address should be at least 6 character allowed.")
