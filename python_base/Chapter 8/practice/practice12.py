# 8.12
def get_sandwich_components(*components):
	print("\nThis sandwich is composed of:")
	for component in components:
		print(f"- {component}")

get_sandwich_components('bread', 'bacon', 'cheese', 'lettuce')
get_sandwich_components('bread')
get_sandwich_components('bread', 'ham', 'cheese', 'bacon', 'lettuce', 'tomato')