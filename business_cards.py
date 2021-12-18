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
    
    @property
    def label_lenght(self):
        label_lenghter = len(self.first_name + " " + self.last_name)
        return f"Długość imienia i nazwiska: {label_lenghter}"

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

#card1 = BaseContact(
#    first_name = fake.first_name(),
#    last_name = fake.last_name(),
#    phone = fake.phone_number(),
#    email = fake.email()
#)

#card2 = BusinessContact(
#    first_name = fake.first_name(),
#    last_name = fake.last_name(),
#    phone = fake.phone_number(),
#    email = fake.email(),
#    position = fake.job(),
#    company = fake.company(),
#    business_phone = fake.phone_number()
#)

#print(card1)
#print(card1.contact())
#print(card1.label_lenght)

def create_contacts(pattern,number):
    if pattern.lower() == 'p':
        print("********* Wizytówki prywatne *********")
        for i in range(number):
            card = BaseContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                phone = fake.phone_number(),
                email = fake.email()
            )      
            print(f"Osoba:\t\t{card.first_name} {card.last_name}\nTelefon:\t{card.phone}\nemail:\t\t{card.email}\n"+str(40*"-"))
    elif pattern.lower() == 'b':
        print("************** Wizytówki biznesowe ***************")
        for i in range(number):
            card = BusinessContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                phone = fake.phone_number(),
                email = fake.email(),
                position = fake.job(),
                company = fake.company(),
                business_phone = fake.phone_number()
                )
            print(f"Osoba:\t\t{card.first_name} {card.last_name}\nTelefon:\t{card.phone}\nemail:\t\t{card.email}\n\tFIRMA:\t\t{card.company}\n\tSTANOWISKO:\t{card.position}\n\tNUMER SŁUŻBOWY:\t{card.business_phone}\n"+str(45*"-"))

if __name__ == "__main__":
    pattern = str(input("Jaki typ wizytówki Cię interesuje? [P] - prywatne, [B] - biznesowe : "))
    number = int(input("Podaj liczbę wizytówek do wygenerowania: "))
    create_contacts(pattern,number)