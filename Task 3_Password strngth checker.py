def password_strength(a):
    if len(a) < 8:
        print("Password should be minimum 8 characters")
    else:
        Strength = 0

        # Checking for uppercase, lowercase, digits, and special characters
        if any(char.isupper() for char in a):
            Strength += 1
        if any(char.islower() for char in a):
            Strength += 1
        if any(char.isdigit() for char in a):
            Strength += 1
        if any(not char.isalnum() for char in a):
            Strength += 1

        if Strength >= 3:
            print("Strong Password")
        elif Strength == 2:
            print("Moderate Password")
        elif Strength == 1:
            print("Weak Password")
        else:
            print("Very Weak Password")
a=input("Enter Your Password :")
password_strength(a)


