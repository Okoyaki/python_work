# 5.2
cars = ['audi', 'toyota', 'bmw', 'tesla']
pizza = 'Pepperoni'
age_0 = 22
age_1 = 18

print(pizza == 'Pepperoni')
print(pizza != 'pepperoni')

print(pizza.lower() != 'pepperoni')

print(age_0 > age_1)
print(age_0 < age_1)
print(age_0 >= age_1)
print(age_0 <= age_1)

print(age_0 > 18 and pizza.lower() == 'pepperoni')
print(age_1 >= 18 or pizza.lower() != 'pepperoni')

print('audi' in cars)
print('toyota' not in cars)