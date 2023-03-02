# 5.10
current_users = ['Alex', 'Marie', 'Max', 'Jordan', 'Kate', 'Egor']
current_users_low = []
new_users = ['Marie', 'Igor', 'Jonathan', 'Max', 'Karen']

for user in current_users:
	current_users_low.append(user.lower())

for user in new_users:
	if user.lower() in current_users_low:
		print("Choose another name.")
	else:
		print("This name is free to choose.")