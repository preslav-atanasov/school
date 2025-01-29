class EmailValidator:
    def __init__(self, min_length, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        else:
            return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        else:
            return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        else:
            return False

    def validate(self, email):
        username = email.split("@")[0]
        mail = email.split("@")[1].split(".")[0]
        domain = email.split("@")[1].split(".")[1]
        if self.__is_domain_valid(domain) and self.__is_name_valid(username) and self.__is_mail_valid(mail):
            return f"Valid"
        else:
            return f"Invalid"


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(5, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
