from Product import Product
from Commission import Commission
from User import User


class Company:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.discounts = []
        self.users = []

    def create_products(self, product_list):
        for product in product_list:
            self.products.append(Product(**product))

    def add_markup(self, markup_list):
        for markup in markup_list:
            for product in self.products:
                if markup["product_type"] == product.get_type():
                    product.add_markup_data(**markup)

    def create_discounts(self, discount_list):
        for discount in discount_list:
            self.discounts.append(Commission(**discount))

    def create_users(self, user_list):
        for user in user_list:
            self.users.append(User(**user))

    def set_data(self):
        for product in self.products:
            product.add_commissions(self.discounts)
        for discount in self.discounts:
            discount.add_users(self.users)

    def calculate_markup_percent(self, product_type, count):
        for product in self.products:
            if product.get_type() == product_type:
                markup = product.get_markup(count)
                return markup

    def calculate_total_price(self, product_type, count):
        for product in self.products:
            if product.get_type() == product_type:
                total_price = product.get_price(count)
                return total_price

    def calculate_discount(self, product_id, count, user_id):
        for product in self.products:
            if product.get_type() == product_id:
                discount = product.get_discount(count, user_id)
                return discount

    def get_product_name(self, product_id):
        for product in self.products:
            if product.get_type() == product_id:
                name = product.get_name()
                return name

    def get_user_name(self, user_id):
        user_name = {'first_name': '', 'last_name': ''}
        for user in self.users:
            if user.get_id() == user_id:
                first_name, last_name = user.get_username()
                user_name['first_name'] = first_name
                user_name['last_name'] = last_name
        return user_name

    def calculate_product_price(self, product_id, count, user_id=0):
        product_name = self.get_product_name(product_id)
        total_price = self.calculate_total_price(product_id, count)
        discount = self.calculate_discount(product_id, count, user_id)
        total_with_commission = round(total_price - discount, 2)
        user_name = self.get_user_name(user_id)
        result = {
            'product_name': product_name,
            'total_price': total_price,
            'total_with_commission': total_with_commission,
            'discount': discount,
            'username': user_name,
        }
        return result
