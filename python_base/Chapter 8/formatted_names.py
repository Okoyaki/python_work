def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		fullname = f"{first_name} {middle_name} {last_name}"
	else:
		fullname = f"{first_name} {last_name}"
	return fullname.title()


musician = get_formatted_name('jimi', 'hendrix', middle_name='lee')
print(musician)
