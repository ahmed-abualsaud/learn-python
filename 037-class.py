class Car:
    width = 10
    length = 15
    height = 20
    color = 'white'
    volume = width * length * height

print('Car:', Car.volume, Car.color)

# create class-scope variable
volvo = Car
nissan = Car

print('Volvo:', volvo.volume, volvo.color)
print('Nissan:', nissan.volume, nissan.color)


# =====================================================================================================
print('\n')


# it will update all instances (nissan and volvo) because all class variables are class-scoped so they are shared across all instances
nissan.color = 'blue'

print('Volvo:', volvo.volume, volvo.color) # blue
print('Nissan:', nissan.volume, nissan.color) # blue

print('\n')

# create object-scope instance
honda = Car()
# it will update only the honda instance keeping volva and nissan with blue colors
honda.color = 'green'

print('Volvo:', volvo.volume, volvo.color) # blue
print('Nissan:', nissan.volume, nissan.color) # blue
print('Honda:', honda.volume, honda.color) # green


# =====================================================================================================
print('\n')


# an example on class with a constructor
class Vehicle:
    def __init__(self, color):
        self.color = color

# create vehicle instance with red color
toyota = Vehicle('red')

print('Toyota:', toyota.color) # red


# =====================================================================================================
print('\n')


class Person:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    

    def user_details(self):
        print('User Details:\n   name:  {} \n   email: {} \n   age:   {}'.format(self.name, self.email, self.age))


ahmed = Person('Ahmed', 'ahmed@gmail.com', 30)

ahmed.user_details()


# =====================================================================================================
print('\n')


class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show(self):
        s = '%s, %s, balance: %s' % (self.name, self.no, self.balance)
        print (s)

a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson', '19371564761', 50000)

print("a1 balance :  " , a1.balance )
print("a2 no      :  " ,   a2.no)

a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)

print ("a1's balance:", a1.balance)
print ("a2's balance:", a2.balance)

a1.show()
a2.show()
