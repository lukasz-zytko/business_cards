from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone} {self.email}"
    
    def contact(self):
        return f".. Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"

class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def __str__(self):
        return super().__str__() + f" {self.position} {self.company} {self.business_phone}"
    
    def contact(self):
        return f".. Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}"

card1 = BaseContact(
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    phone = fake.phone_number(),
    email = fake.email()
)

card2 = BusinessContact(
    first_name = fake.first_name(),
    last_name = fake.last_name(),
    phone = fake.phone_number(),
    email = fake.email(),
    position = fake.job(),
    company = fake.company(),
    business_phone = fake.phone_number()
)

print(card2)
print(card2.contact())