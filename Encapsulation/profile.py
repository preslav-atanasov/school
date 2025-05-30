class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: int):
        if not (5 <= len(str(value)) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_case_presented = len([c for c in value if c.isupper()]) > 0
        is_digit_present = len([c for c in value if c.isdigit()]) > 0

        if not is_length_valid or not is_digit_present or not is_upper_case_presented:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f"You have a profile with username: {self.username} and password: {'*' * len(self.password)}"


# invalid_pass = Profile("My username", "My-password")
# print(invalid_pass)
# invalid_name = Profile("Too_long_username", "183erSDJF8")
# print(invalid_name)
correct_profile = Profile("Username", "P4ssword")
print(correct_profile)
