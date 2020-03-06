def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 位置实参
describe_pet('hamster', 'harry')
# 参数实参
describe_pet(animal_type='hamster', pet_name='harry')
