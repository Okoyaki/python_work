# 8.13
def build_profile(first, last, **user_info):
	"""Строит словарь с информацией о пользователе."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('max', 'shushakov', city = 'ufa',
							 faculty = 'firt', course = '4')
print(user_profile)