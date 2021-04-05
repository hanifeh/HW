class Commission:
    def __init__(self, group_name, cost, unit, users):
        self.group_name = group_name
        self.cost = cost
        self.unit = unit
        self.users_list = users
        self.users = []

    def add_users(self, users):
        for user in users:
            if user.get_id() in self.users_list:
                self.users.append(user)

    def get_group_name(self):
        return self.group_name

    def get_users(self):
        return self.users
