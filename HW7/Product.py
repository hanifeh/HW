class Product:

    def __init__(self, product_type, name, price, unit, commission_groups):
        self.product_type = product_type
        self.name = name
        self.price = price
        self.unit = unit
        self.commission_groups = commission_groups
        self.commissions = []

    def get_type(self):
        return self.product_type

    def get_name(self):
        return self.name

    def add_markup_data(self, lower_cost, upper_cost, lower_count, product_type, unit):
        self.lower_cost = lower_cost
        self.upper_cost = upper_cost
        self.lower_count = lower_count

    def get_markup(self, count):
        if count > self.lower_count:
            markup = self.lower_cost
        else:
            markup = round(self.upper_cost + ((count - 1) *
                                              ((self.upper_cost - self.lower_cost) / (1 - self.lower_count))), 3)
        return markup

    def get_price(self, count):
        markup = self.get_markup(count)
        total_price = round((self.price + (self.price * markup / 100)) * count, 2)
        return total_price

    def add_commissions(self, commissions):
        for commission in commissions:
            if commission.get_group_name() in self.commission_groups:
                self.commissions.append(commission)

    def get_discount(self, count, user_id):
        total_price = self.get_price(count)
        discounts = [0]
        for commission in self.commissions:
            for user in commission.get_users():
                if user.get_id() == user_id:
                    if commission.unit == 'percent':
                        discounts.append(total_price * commission.cost / 100)
                    elif commission.unit == 'Dollar':
                        discounts.append(commission.cost)
        discount = round(sorted(discounts, reverse=True)[0], 2)
        return discount
