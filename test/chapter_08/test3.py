def describe_pet(pet_name, animal_type='dog'):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 默认值
# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参
describe_pet('willie')
describe_pet('harry', 'hamster')
