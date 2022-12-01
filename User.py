import csv

class User:
    def __init__(self, ID, username, password, name, payment_info, address, email, new=False):
        self.ID = ID
        self.username = username
        self.password = password
        self.name = name
        self.payment_info = payment_info
        self.address = address
        self.email = email
        if new:
            self._update()

    def login(self, username, password):
        if username == self.username and password == self.password:
            return True
        return False

    def change_name(self, name):
        self.name = name
        self._update()

    def change_pass(self, password):
        self.password = password
        self._update()

    def change_payment_info(self, payment_info):
        self.payment_info = payment_info
        self._update()

    def change_address(self, address):
        self.address = address
        self._update()

    def change_email(self, email):
        self.email = email
        self._update()

    def delete_account(self):
        lines = []  # store csv in memory
        #current_user = [self.ID, self.username, self.password, self.name, self.payment_info, self.address, self.email]

        with open('users.csv', 'r') as users_file:
            users_read = csv.reader(users_file, delimiter=',')
            for row in users_read:
                if self.ID != row[0]:  # read all users into list except for current user
                    lines.append(row)
        with open('users.csv', 'w') as users_file:  # overwrite users.csv file with updated data
            users_write = csv.writer(users_file, delimiter=',', lineterminator='\n')
            users_write.writerows(lines)  # old unchanged users

    def _update(self):  # write class to csv file
        lines = []  # store csv in memory
        current_user = [self.ID, self.username, self.password, self.name, self.payment_info, self.address, self.email]

        with open('users.csv', 'r') as users_file:
            users_read = csv.reader(users_file, delimiter=',')
            for row in users_read:
                if self.ID != row[0]:  # read all users into list except for current user
                    lines.append(row)
        with open('users.csv', 'w') as users_file:  # overwrite users.csv file with updated data
            users_write = csv.writer(users_file, delimiter=',', lineterminator='\n')
            users_write.writerows(lines)  # old unchanged users
            users_write.writerow(current_user)  # new user
