from mammal import *
from vehicle import *
import sqlite3

print("Starting simulation...")

connection = sqlite3.connect("simulation.db")
print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS car (type TEXT PRIMARY KEY, currentSpeed, doors)")
cursor.execute("SELECT COUNT(*) FROM car")
car_id = 0
rows = cursor.fetchall()
car1 = Car("Hyundai i30", 5)
cursor.execute(f"INSERT OR IGNORE INTO car (type, currentSpeed, doors) VALUES ('{car1.get_type_name()}','{car1.get_current_speed()}', '{car1.get_door_count()}')")
connection.commit()


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

# Check the count of vehicle
print("Number of vehicle:", Vehicle.vehicle_count())


car2 = Car("Opel Adam", 3)
bicycle1 = Bicycle("KTM 1290")
bicycle2 = Bicycle("Honda CB125R")

# Check the count got vehicle
print("Number of vehicle:", Vehicle.vehicle_count())

# Check car methods
car1.start()
car1.accelerate(199)
car1.decelerate(200)
print(car1.get_current_speed())
car1.accelerate(2)
car1.decelerate(50)
car1.stop()
print(car1.get_current_speed())

# Check bicycle methods
bicycle1.ring(5)

# Remove vehicle
del car1
del car2
del bicycle1
del bicycle2

# Check the count got vehicle
print("Number of vehicle:", Vehicle.vehicle_count())

connection.close()
print("End simulation...")
