class User:
    def __init__(self, userid, first_name, last_name):
        self.userid = userid
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def get_id(self):
        return self.userid

    def get_username(self):
        return self.first_name, self.last_name
