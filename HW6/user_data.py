from company_data import user_list


def u_names(user_id):
    # this function return users name /// need discount group
    user_name = {'first_name': '', 'last_name': ''}
    for user in user_list:
        if user['userid'] == user_id:
            user_name['first_name'] = user['first_name']
            user_name['last_name'] = user['last_name']
    return user_name
