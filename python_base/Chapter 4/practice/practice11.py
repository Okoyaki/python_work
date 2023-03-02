# 4.11 (code from 4.1)
pizzas = ['pepperoni', 'margarita', 'pineapple pizza']
for pizza in pizzas:
	print(f"I like {pizza}")
print("I looove pizza!!\n")

friend_pizzas = pizzas[:]
pizzas.append('cheese pizza')
friend_pizzas.append('bacon and cheese pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)