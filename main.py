# Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        pass

    def eat(self):
        pass

    def __str__(self):
        return f"Животное: {self.name}, Возраст: {self.age}, Цвет: {self.color}"


class Bird(Animal):
    def __init__(self, name,age,color,species):
        super().__init__(name,age,color)
        self.species = species

    def make_sound(self):
        print(f'{self.name} - курлык-курлык')

    def __str__(self):
        return f"Птица {self.species}, Имя: {self.name}, Возраст: {self.age}, Цвет: {self.color}"


class Mammal(Animal):
    def __init__(self,name,age,color, species):
        super().__init__(name,age,color)
        self.species = species

    def make_sound(self):
        print(f'{self.name} - ррррррр')

    def __str__(self):
        return f"Млекопитающее {self.species}, Имя: {self.name}, Возраст: {self.age}, Цвет: {self.color}"



class Reptile(Animal):
    def __init__(self,name,age,color, species):
        super().__init__(name,age,color)
        self.species = species

    def make_sound(self):
        print(f'{self.name} - ррр-ррр')

    def __str__(self):
        return f"Рептилия {self.species}, Имя: {self.name}, Возраст: {self.age}, Цвет: {self.color}"


class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position


    def __str__(self):
        return f'Сотрудник {self.name}, Должность {self.position}'


class ZooKeeper(Employee):
    def feed_animal(self):
        print(f'{self.name} - кормит животных')

    def __str__(self):
        return f'Сотрудник {self.name}, Должность {self.position}'

class Veterinarian(Employee):
    def heal_animal(self):
        print(f'{self.name} - лечит животных ')


    def __str__(self):
        return f' Сотрудник {self.name}, Должность {self.position}'



class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def info(self):
        print(f'Информация о зоопарке "{self.name}":')
        print("Животные:")
        if self.animals:
            for animal in self.animals:
                print(f"  - {animal}")
        else:
            print("  В зоопарке пока нет животных.")
        print("Сотрудники:")
        if self.employees:
            for employee in self.employees:
                print(f"  - {employee}")
        else:
            print("  В зоопарке пока нет сотрудников.")


    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'{animal.name}  -  добавлен в зоопарк')

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f'{animal.name} - удален из зоопарка')

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'{employee.name} - добавлен в зоопарк')

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee.name)
            print(f'{employee.name}  - удален из зоопарка')



bird1 = Bird('Дима',2,'белый','голубь')
mammal1 = Mammal('Вася',3, 'Оранжевый','Тигр')
reptile1 = Reptile('Лев',5,'Черный','Крокодил')

zoo = Zoo('Тестовый зоопарк')
zoo.add_animal(bird1)
print('-----')
zoo.add_animal(mammal1)
print('-----')
zoo.add_animal(reptile1)
print('-----')
bird1.make_sound()
print('-----')
mammal1.make_sound()
print('-----')
reptile1.make_sound()
print('-----')

kepper1 = ZooKeeper('Ирина','Смотритель')
veterinarian1 = Veterinarian('Олег','Ветеринар')

zoo.add_employee(kepper1)
print('-----')
zoo.add_employee(veterinarian1)
print('-----')
zoo.info()

kepper1.feed_animal()
print('-----')
veterinarian1.heal_animal()






