import random

class RegistrationData:

    def random_email():
        random_email = f"dariachernukha14{random.randint(100, 999)}@{random.choice(['ya.ru', 'yandex.ru', 'google.com', 'mail.ru'])}"
        return random_email

    def random_password():
        symbols = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        random_password = ""
        for i in range(6):
            random_password += random.choice(symbols)
        return random_password

print(RegistrationData.random_email())
print(RegistrationData.random_password()[:5])