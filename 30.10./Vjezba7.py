def password_checking(password):
    passwordLength = len(password)

    hasUpperCase = False
    hasNumber = False
    hasPassword = False

    for x in password:
        if x.isdigit() == True and hasNumber == False:
            hasNumber = True
        
        if x.isupper() == True and hasUpperCase == False:
            hasUpperCase = True

    passwordInLower = password.lower()
    if "password" in passwordInLower or "lozinka" in passwordInLower:
        hasPassword = True

    if  passwordLength < 8 or passwordLength > 15:
        print("Lozinka mora sadrzavati izmedu 8 i 15 znakova")

    elif not (hasUpperCase and hasNumber):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")

    elif hasPassword == True:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")

    else:
        print("Lozinka je jaka!")

password = input("Unesi lozinku: ")
password_checking(password)
