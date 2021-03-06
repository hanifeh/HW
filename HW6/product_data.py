from company_data import product_list


def p_name(product_id):
    # this function return product name /// need product id
    for product in product_list:
        if product['type'] == product_id:
            return product['name']


def p_price(product_id):
    # this function return product price /// need product id
    for product in product_list:
        if product['type'] == product_id:
            return product['price']


def p_commission(product_id):
    # this function return product commission groups /// need product id
    for product in product_list:
        if product['type'] == product_id:
            return product['commission_groups']
