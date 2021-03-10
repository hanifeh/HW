from product_data import p_name, p_price, p_commission
from markup_data import mup_lower_cost, mup_upper_cost, mup_lower_count
from discount_data import d_cost, d_unit, d_users
from user_data import u_names


def calculate_total_price(product_id, count):
    start_price = p_price(product_id)
    markup = calculate_markup_percent(product_id, count)
    total_price = round((start_price + (start_price * markup / 100)) * count, 2)
    return total_price


def calculate_discount(product_id, count, user_id):
    total_price = calculate_total_price(product_id, count)
    commissions = []
    commission_groups = p_commission(product_id)
    commissions_data = [(d_cost(group), d_unit(group)) for group in commission_groups
                        for userid in d_users(group) if userid == user_id]
    if len(commissions_data) == 0:
        discount = 0
    else:
        for commission in commissions_data:
            if commission[1] == 'percent':
                commissions.append(total_price * commission[0] / 100)
            elif commission[1] == 'Dollar':
                commissions.append(commission[0])
        discount = round(sorted(commissions, reverse=True)[0], 2)
    return discount


def calculate_markup_percent(product_id, count):
    lower_cost = mup_lower_cost(product_id)
    upper_cost = mup_upper_cost(product_id)
    lower_count = mup_lower_count(product_id)
    if count > lower_count:
        markup = lower_cost
    else:
        markup = round(upper_cost - ((count - 1) * ((upper_cost - lower_cost) / (lower_count - 1))), 3)
    return markup


def calculate_product_price(product_id, count, user_id=0):
    product_name = p_name(product_id)
    total_price = calculate_total_price(product_id, count)
    discount = calculate_discount(product_id, count, user_id)
    total_with_commission = round(total_price - discount, 2)
    user_name = u_names(user_id)
    result = {
        'product_name': product_name,
        'total_price': total_price,
        'total_with_commission': total_with_commission,
        'discount': discount,
        'username': user_name,
    }
    return result


print(calculate_markup_percent("1", 5))
print(calculate_markup_percent("2", 3))
print(calculate_markup_percent("3", 20))
print(calculate_product_price("1", 5, 1002))
print(calculate_product_price("2", 5, 1003))
print(calculate_product_price("3", 2, 1004))
print(calculate_product_price("2", 1))
print(calculate_product_price("1", 10, 1002))
print(calculate_product_price("1", 15, 1003))
print(calculate_product_price("4", 20, 1005))
