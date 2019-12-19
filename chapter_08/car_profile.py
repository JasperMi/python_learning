def make_car(manufacturer, type, **car_info):
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['type'] = type
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
