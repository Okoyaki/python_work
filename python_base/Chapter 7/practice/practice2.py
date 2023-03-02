# 7.2
table_number = input("How many tables would you like to place reservation on? ")
table_number = int(table_number)

if table_number > 8:
	print("\nDeepest apologies, you will have to wait a little bit.")
else:
	print("\nTables are ready.")