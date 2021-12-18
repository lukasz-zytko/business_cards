from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

card1 = BaseContact(
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    phone = fake.phone_number(),
    email = fake.email()
)

print(card1.phone)