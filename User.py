class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.name = ''
        self.surname = ''
        self.phone = ''
        self.email = ''
        self.birthday = ''
        self.sex = ''
        self.WHERE_I_WAS = ''

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\n' \
               f'Phone: {self.phone}\ne-mail: {self.email}\n' \
               f'Birthday: {self.birthday}\nSex: {self.sex}\n'

    def set(self, user: dict):
        self.name = user['name']
        self.surname = user['surname']
        self.phone = user['phone']
        self.email = user['email']
        self.birthday = user['birthday']
        self.sex = user['sex']

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_sex(self, sex):
        self.sex = sex
