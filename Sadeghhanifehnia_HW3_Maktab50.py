password = input('password khod ra vared konid : ')
pass_check = "nemibashad ."


def digit_check(check_password):
    for i in check_password:
        if i.isdigit():
            return True
    else:
        return False


def lower_check(check_password):
    for i in check_password:
        if i.islower():
            return True
    else:
        return False


def upper_check(check_password):
    for i in check_password:
        if i.isupper():
            return True
    else:
        return False


def special_check(check_password):
    for i in check_password:
        if i in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]:
            return True
    else:
        return False


if all([len(password) >= 6, digit_check(password), lower_check(password), upper_check(password),
        special_check(password)]):
    pass_check = "mibashad ."

print("password shoma motmaen", pass_check)
