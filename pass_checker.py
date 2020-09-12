username = input("Username: ")
password = input("Password: ")
password_len = len(password)
hidden_password = "*" * password_len


print(f"{username}, your password, {hidden_password}, is {password_len} characters long.")