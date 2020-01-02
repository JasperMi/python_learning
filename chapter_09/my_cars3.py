from chapter_09.car2 import Car2
from chapter_09.electric_car3 import ElectricCar

my_beetle = Car2('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
