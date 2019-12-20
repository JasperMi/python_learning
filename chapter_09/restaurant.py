class Restaurant():
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant_name:" + self.restaurant_name)
        print("Cuisine_type:" + self.cuisine_type)

    def open_restaurant(self):
        print("Open_restaurant")


restaurant = Restaurant("Jasper's restaurant", 'Lu')
restaurant2 = Restaurant("Alice's restaurant", 'Lu')
restaurant3 = Restaurant("Jack's restaurant", 'Lu')
print("Restaurant_name:" + restaurant.restaurant_name)
print("Cuisine_type:" + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
