password = input('password khod ra vared konid : ')
if all([len(password) >= 6, any(i.isdigit() for i in password), any(i.islower() for i in password), any(i.isupper() for i in password), any(i in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"] for i in password)]):
    print("password is safe .")
else:
    print("password is not safe .")
