def city_country(city, country):
    city_country_message = city.title() + ', ' + country.title()
    return str(city_country_message)


message = city_country('Qingdao', 'China')
print(message)
message = city_country('Shanghai', 'China')
print(message)
message = city_country('Tokyo', 'Japan')
print(message)
