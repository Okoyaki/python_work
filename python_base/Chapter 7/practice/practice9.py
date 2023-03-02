# 7.9
sandwich_orders = ['chese sandwich', 'bacon sandwich', 'fried sandwich',
				   'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("There are no pastrami left.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I made your {sandwich}!")
	finished_sandwiches.append(sandwich)

print("\nAll the finished sandwiches are: ")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())