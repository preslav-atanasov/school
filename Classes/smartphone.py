class Smartphone:
    def __init__(self):
        memory = float(input("how much memory do you have?: "))
        self.memory = memory
        self.apps = []
        self.size = None
        self.name = None
        self.is_on = False

    def power(self):
        userinput = input("Is the phone on? (yes/no): ")
        if userinput.lower() == "yes":
            print("Phone is on.")
            self.is_on = True
            return self.is_on
        else:
            print("Phone is off.")
            return self.is_on

    def install(self):
        name = input("Name of the app?: ")
        self.name = name
        size = float(input("Size of the app to be installed? (in GB): "))
        self.size = size
        if size <= self.memory and self.is_on is True:
            print(self.is_on)
            self.apps.append(name)
            print(f"App '{name}' successfully installed.")
            self.memory -= self.size
            print(f"{self.memory}GB of memory left.")
        else:
            print(self.is_on)
            print(f"Not enough memory! You need {size - self.memory}GB more.")

    def check_space(self):
        print(f"You have {self.memory}GB of memory left.")

    def apps_installed(self):
        print("The following apps are installed on this device:")
        print(self.apps)


# Example usage
smartphone = Smartphone()
smartphone.power()
smartphone.install()
smartphone.check_space()
smartphone.apps_installed()
