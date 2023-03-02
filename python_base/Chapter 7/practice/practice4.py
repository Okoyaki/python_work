# 7.4
active = True

while active:
	topping = input("\nEnter a topping of your choice: ")
	
	if topping != 'quit':
		print(f"{topping.title()} has been added to your pizza.")
	else:
		active = False