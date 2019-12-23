class Restaurant():
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, count_served):
        self.number_served = count_served

    def increment_number_served(self, increment_served):
        self.number_served += increment_served

    def describe_restaurant(self):
        print("Restaurant_name:" + self.restaurant_name)
        print("Cuisine_type:" + self.cuisine_type)

    def open_restaurant(self):
        print("Open_restaurant")

# restaurant = Restaurant("Jasper's restaurant", 'Lu')
# restaurant2 = Restaurant("Alice's restaurant", 'Lu')
# restaurant3 = Restaurant("Jack's restaurant", 'Lu')
# print("Restaurant_name:" + restaurant.restaurant_name)
# print("Cuisine_type:" + restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
# print("Number_served:" + str(restaurant.number_served))
# restaurant.number_served = 10000000
# print("Number_served:" + str(restaurant.number_served))
# restaurant.set_number_served(20000000)
# print("Number_served:" + str(restaurant.number_served))
# restaurant.increment_number_served(10000)
# print("Number_served:" + str(restaurant.number_served))
