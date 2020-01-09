def get_formatted_city_name(city, country, popluation=''):
    """生成格式化的城市和国家名称"""
    if popluation:
        full_city_name = city + ", " + country + "-population " + str(popluation)
    else:
        full_city_name = city + ", " + country
    return full_city_name.title()
