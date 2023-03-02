# 6.6
favorite_language = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

survey_people = ['jen', 'edward', 'alex', 'max', 'kate']

for person in survey_people:
	if person in favorite_language.keys():
		print(f"{person.title()}, thank you for doing the survey!")
	else:
		print(f"{person.title()}, please complete the survey!")