from company_data import discount_list


def d_cost(discount_group):
    # this function return discount cost /// need discount group
    for group in discount_list:
        if group['group_name'] == discount_group:
            return group['cost']


def d_unit(discount_group):
    # this function return discount unit /// need discount group
    for group in discount_list:
        if group['group_name'] == discount_group:
            return group['unit']


def d_users(discount_group):
    # this function return discount users /// need discount group
    for group in discount_list:
        if group['group_name'] == discount_group:
            return group['users']
