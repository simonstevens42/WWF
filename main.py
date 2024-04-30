from mammal import *
from vehicle import *
import datetime

print("Starting simulation...")

cat1 = Cat("Whiskers", datetime.date(2019, 5, 15), 5.5, "Persian", "Likes to sleep a lot")
dog1 = Dog("Buddy", datetime.date(2018, 7, 20), 10.2, "Golden Retriever", "Loves playing fetch")

# Display the data of the cat and the dog
print("Cat data:")
print(cat1.show_data())
print("Dog data:")
print(dog1.show_data())

# Display the population of dogs and cats
print("Dogs in the population:", Dog.get_dog_population())
print("Cats in the population:", Cat.get_cat_population())

# Remove the cat and the dog (imagine that they have died)
del cat1
del dog1

# Check the population of dogs and cats after removal
print("Dogs in the population:", Dog.get_dog_population())
print("Cats in the population:", Cat.get_cat_population())

# Check the count of vehicles
print("Count of the vehicles:", Vehicle.vehicle_count())

car1 = CombustionCar("Porsche 911 GT3", 120000, 3, "gasoline", 510, 12.9, 64)
car2 = ElectricCar("Tesla Model S", 80000, 5, "electric", 1020, 18.7, 250)

print(car1.get_fuel_level())
car1.refuel(33)
car1.refuel(32)
print(car1.get_fuel_level())

print(car2.get_battery_level())
car2.recharge("Type-3", 1, 126)
car2.recharge("Type-1", 5, 126)
car2.recharge("Type-1", 2, 126)
car2.recharge("Type-1", 2, 125)
print(car2.get_battery_level())

print("Count of the vehicles:", Vehicle.vehicle_count())

del car1
del car2
print("End simulation...")
