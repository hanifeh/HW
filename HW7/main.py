from Company_data import *
from Company import Company

if __name__ == '__main__':
    company = Company('x')
    company.create_products(product_list)
    company.add_markup(markup_list)
    company.create_discounts(discount_list)
    company.create_users(user_list)
    company.set_data()
    print(company.calculate_markup_percent("1", 5))
    print(company.calculate_markup_percent("2", 1))
    print(company.calculate_markup_percent("3", 20))
    print(company.calculate_product_price("1", 5, 1002))
    print(company.calculate_product_price("2", 5, 1003))
    print(company.calculate_product_price("3", 2, 1004))
    print(company.calculate_product_price("2", 1))
    print(company.calculate_product_price("1", 10, 1002))
    print(company.calculate_product_price("1", 15, 1003))
    print(company.calculate_product_price("4", 20, 1005))
