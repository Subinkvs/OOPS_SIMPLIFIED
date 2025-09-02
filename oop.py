# function importing class from another file


from car import Car

car1 = Car('Hyudai', 2015, 8)
car2 = Car('Maruti', 2009, 3)
car1.model = 'Porsche'
print(car1.model)
print(car1.year)
print(car1.price)

print(car2.model)
print(car2.year)
print(car2.price)

car1.drive()
car2.drive()