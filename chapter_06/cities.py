cities = {
    'Qingdao': {
        'country': 'China',
        'population': 10000000,
        'fact': 'beautiful',
    },

    'Tokyo': {
        'country': 'Tokyo',
        'population': 15000000,
        'fact': 'amazing',
    },

    'Shanghai': {
        'country': 'China',
        'people': 20000000,
        'population': 'fantastic'
    },
}

for city, city_info in cities.items():
    print("\ncity: " + city)
    for single_info, content in city_info.items():
        if type(content) == 'str':
            print("\t" + single_info + " : " + content)
        else:
            print("\t" + single_info + " : " + str(content))
