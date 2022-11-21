from faker import Faker
fake = Faker()


def getRegisteredUser():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year(),
        "month": fake.month()
    }


# if __name__ == '__main__':
#     print(getRegisteredUser())
