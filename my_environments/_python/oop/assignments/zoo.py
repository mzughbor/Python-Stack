class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age
        self.health = 50
        self.happiness = 50

    def feed(self):
        self.health += 10
        self.happiness += 10
        print(f"{self.name} has been fed.")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")


class Lion(Animal):
    def __init__(self, name, age=1, mane_size="Medium"):
        super().__init__(name, age)
        self.mane_size = mane_size

    def feed(self):
        self.health += 5
        self.happiness += 7
        print(f"{self.name} the Lion roars happily after eating.")

    def display_info(self):
        super().display_info()
        print(f"  Type: Lion | Mane Size: {self.mane_size}")


class Monkey(Animal):
    def __init__(self, name, age=1, favorite_food="Banana"):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def feed(self):
        self.health += 5
        self.happiness += 15
        print(f"{self.name} the Monkey swings with joy after eating {self.favorite_food}.")

    def display_info(self):
        super().display_info()
        print(f"  Type: Monkey | Favorite Food: {self.favorite_food}")


class Bear(Animal):
    def __init__(self, name, age=1, fur_color="Brown"):
        super().__init__(name, age)
        self.fur_color = fur_color

    def feed(self):
        self.health += 13
        self.happiness += 13
        print(f"{self.name} the Bear grunts with satisfaction after eating.")

    def display_info(self):
        super().display_info()
        print(f"  Type: Bear | Fur Color: {self.fur_color}")


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, animal_type, name, **kwargs):
        animal_type = animal_type.lower()
        if animal_type == "lion":
            self.animals.append(Lion(name, **kwargs))
        elif animal_type == "monkey":
            self.animals.append(Monkey(name, **kwargs))
        elif animal_type == "bear":
            self.animals.append(Bear(name, **kwargs))
        else:
            print(f"Unknown animal type: {animal_type}")

    def feed_all(self):
        print(f"\nFeeding all animals in {self.name}...")
        for animal in self.animals:
            animal.feed()

    def print_all_info(self):
        print(f"\n{'-'*15} {self.name} {'-'*15}")
        for animal in self.animals:
            animal.display_info()

# Example usage
if __name__ == "__main__":
    my_zoo = Zoo("Mahmoud Amazing Zoo")
    my_zoo.add_animal("lion", "Simba", mane_size="Large")
    my_zoo.add_animal("lion", "Nala", mane_size="Small")
    my_zoo.add_animal("monkey", "George", favorite_food="Mango")
    my_zoo.add_animal("bear", "Baloo", fur_color="Gray")

    my_zoo.print_all_info()
    my_zoo.feed_all()
    my_zoo.print_all_info()
