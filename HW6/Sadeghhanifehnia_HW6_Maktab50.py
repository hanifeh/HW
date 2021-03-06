from product_data import p_name, p_price, p_commission
from markup_data import mup_lower_cost, mup_upper_cost, mup_lower_count
from discount_data import d_cost, d_unit, d_users
from user_data import u_names


def calculate_total_price(product_id, count):
    product_start_price = p_price(product_id)
    markup = calculate_markup_percent(product_id, count)
    return (product_start_price + (product_start_price * markup / 100)) * count


def calculate_commission(product_id, count, user_id):
    total = calculate_total_price(product_id, count)
    commissions = [0]
    commission_groups = p_commission(product_id)
    commissions_user = [(userid, d_cost(group), d_unit(group)) for group in commission_groups for userid in
                        d_users(group) if userid == user_id]
    for commission in commissions_user:
        if commission[2] == 'percent':
            commissions.append(total - (total * commission[1] / 100))
        if commission[2] == 'Dollar':
            commissions.append(total - (count * commission[1]))
    commissions_sorted = sorted(commissions, reverse=True)
    return commissions_sorted[0]


def calculate_markup_percent(product_id, count):
    lower_cost = mup_lower_cost(product_id)
    upper_cost = mup_upper_cost(product_id)
    lower_count = mup_lower_count(product_id)
    if count > lower_count:
        return lower_cost
    else:
        return round(upper_cost - ((count - 1) * ((upper_cost - lower_cost) / (lower_count - 1))), 3)


def calculate_product_price(product_id, count, user_id=0):
    product_name = p_name(product_id)
    total_price = calculate_total_price(product_id, count)
    total_with_commission = total_price
    if user_id > 1000:
        total_with_commission = calculate_commission(product_id, count, user_id)
        if total_with_commission == 0:
            total_with_commission = total_price
    discount = total_price - total_with_commission
    user_name = u_names(user_id)

    result = {'product_name': product_name, 'total_price': total_price, 'total_with_commission': total_with_commission,
              'discount': discount, 'username': user_name}
    return result


print(calculate_markup_percent("1", 5))
print(calculate_markup_percent("2", 1))
print(calculate_markup_percent("3", 20))
print(calculate_product_price("1", 10, 1002))
print(calculate_product_price("1", 15, 1003))
print(calculate_product_price("4", 20, 1005))
print(calculate_product_price("2", 1))
