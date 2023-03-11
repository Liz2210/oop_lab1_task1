from lib import *


def test_call():
    # Create some ingredients
    egg1 = ChickenEgg(50)
    egg2 = GooseEgg(80)
    cheese = Cheese(200)
    cottage_cheese = CottageCheese(150)
    milk = Milk(300)
    beef = Beef(500)
    mineral_water = MineralWater(1000)
    bread = Bread(150)
    kaiser = Kaiser(100)
    radish = Radish(50)
    cucumber = Cucumber(80)
    apple = Apple(120)
    onion = Onion(70)

    print(egg1)
    print(egg2)
    print(cheese)
    print(cottage_cheese)
    print(milk)
    print(beef)
    print(mineral_water)
    print(bread)
    print(kaiser)
    print(radish)
    print(cucumber)
    print(apple)
    print(onion)

    onion.set_weight(90)
    print(onion)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_call()