class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, a):
        print(f'Через {a} лет {self.name} исполнится {a+self.age}')

p = Person('John', 23, 'male')
p.calculate_age(10)