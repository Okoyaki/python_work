# 5.8/5.9
users = ['Alex', 'Marie', 'Max', 'admin', 'Kate']

if users:
	for user in users:
		if user.lower() == 'admin':
			print(f"Hello {user}, would you like to see a status report?")
		else:
			print(f"Hello {user}, thank you for logging in again")
else:
	print("We need to find some users!")