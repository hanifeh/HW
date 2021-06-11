from company_data import markup_list


def mup_lower_cost(product_id):
    # this function return markup lower cost /// need product id
    for product in markup_list:
        if product['product_type'] == product_id:
            return product['lower_cost']


def mup_upper_cost(product_id):
    # this function return markup upper cost /// need product id
    for product in markup_list:
        if product['product_type'] == product_id:
            return product['upper_cost']


def mup_lower_count(product_id):
    # this function return markup lower count /// need product id
    for product in markup_list:
        if product['product_type'] == product_id:
            return product['lower_count']
