from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_ice_cream(self):
        print("Here are all the ice cream:")
        for flavor in self.flavors:
            print(flavor)


frank_ice_cream_stand = IceCreamStand("frank's ice cream stand", 'Lu', ['apple ice cream', 'orange ice cream'])
frank_ice_cream_stand.show_ice_cream()
