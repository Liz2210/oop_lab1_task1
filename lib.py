from abc import ABC, abstractmethod


class Ingredient(ABC):
    def __init__(self, name, weight):
        self.measurement = "grams"
        self.name = name
        self.weight = weight

    @abstractmethod
    def get_calories(self):
        pass

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight

    def get_calories_per_gram(self):
        return self.get_calories() / self.weight if self.weight > 0 else 0

    def get_calories_per_100g(self):
        return self.get_calories_per_gram() * 100

    def __str__(self):
        return f"{self.name} ({self.weight} {self.measurement}): {self.get_calories()} calories total.\n" \
               f"{self.get_calories_per_100g()} calories per 100g.\n{self.get_calories_per_gram()} calories per gram\n\n"


class ChickenEgg(Ingredient):
    def __init__(self, weight):
        super().__init__("Chicken Egg", weight)

    def get_calories(self):
        return self.weight * 78


class GooseEgg(Ingredient):
    def __init__(self, weight):
        super().__init__("Goose Egg", weight)

    def get_calories(self):
        return self.weight * 147


class Cheese(Ingredient):
    def __init__(self, weight):
        super().__init__("Cheese", weight)

    def get_calories(self):
        return self.weight * 400


class CottageCheese(Ingredient):
    def __init__(self, weight):
        super().__init__("Cottage Cheese", weight)

    def get_calories(self):
        return self.weight * 98


class Milk(Ingredient):
    def __init__(self, weight):
        super().__init__("Milk", weight)
        self.measurement = "milliliters"

    def get_calories(self):
        return self.weight * 42


class Beef(Ingredient):
    def __init__(self, weight):
        super().__init__("Beef", weight)

    def get_calories(self):
        return self.weight * 250


class MineralWater(Ingredient):
    def __init__(self, weight):
        super().__init__("Mineral Water", weight)
        self.measurement = "milliliters"

    def get_calories(self):
        return 0


class Bread(Ingredient):
    def __init__(self, weight):
        super().__init__("Bread", weight)

    def get_calories(self):
        return self.weight * 265


class Kaiser(Ingredient):
    def __init__(self, weight):
        super().__init__("Kaiser", weight)

    def get_calories(self):
        return self.weight * 277


class Radish(Ingredient):
    def __init__(self, weight):
        super().__init__("Radish", weight)

    def get_calories(self):
        return self.weight * 16


class Cucumber(Ingredient):
    def __init__(self, weight):
        super().__init__("Cucumber", weight)

    def get_calories(self):
        return self.weight * 15


class Apple(Ingredient):
    def __init__(self, weight):
        super().__init__("Apple", weight)

    def get_calories(self):
        return self.weight * 52


class Onion(Ingredient):
    def __init__(self, weight):
        super().__init__("Onion", weight)

    def get_calories(self):
        return self.weight * 40
