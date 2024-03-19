from mammal import *

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
