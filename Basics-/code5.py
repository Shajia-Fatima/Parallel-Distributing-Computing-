# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())     # Output: Buddy barks.