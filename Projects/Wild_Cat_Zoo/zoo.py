from lion import Lion
from tiger import Tiger
from cheetah import Cheetah

lion = Lion("Simba", "Male", 5)
tiger = Tiger("Josh", "Female", 7)
cheetah = Cheetah("Cheetahh", "Male", 10)


class Zoo(Lion, Tiger, Cheetah):
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int, animals: list,
                 workers: list, gender: str, age: int):
        super().__init__(name, gender, age)
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = animals
        self.workers = workers

    def add_animal(self, animal, price):
        if self.__budget > price:
            if self.__animal_capacity > 0:
                print(f"{self.name} the {animal}")
