# 3.4
invited_people = ['Andrew', 'Egor', 'Ilya', 'Ainur', 'Roma']
print(f"Hello, {invited_people[0]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[1]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[2]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[3]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[4]}! I am inviting you to a dinner tonight!")

# 3.5
print(f"{invited_people[4]} said that he wouldn't be coming tonight\n")
invited_people[4] = 'Ilshat'
print(f"Hello, {invited_people[0]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[1]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[2]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[3]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[4]}! I am inviting you to a dinner tonight!")

# 3.6
print("There would be more guests coming tonight\n")
invited_people.insert(0, 'Katya')
invited_people.insert(3, 'Danil')
invited_people.append('Nikita')
print(f"Hello, {invited_people[0]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[1]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[2]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[3]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[4]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[5]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[6]}! I am inviting you to a dinner tonight!")
print(f"Hello, {invited_people[7]}! I am inviting you to a dinner tonight!")

# 3.7
print("Only two guests are coming\n")
canceled_guest = invited_people.pop()
print(f"I deeply apologise for cancelling the invitation, {canceled_guest}")
canceled_guest = invited_people.pop()
print(f"I deeply apologise for cancelling the invitation, {canceled_guest}")
canceled_guest = invited_people.pop()
print(f"I deeply apologise for cancelling the invitation, {canceled_guest}")
canceled_guest = invited_people.pop()
print(f"I deeply apologise for cancelling the invitation, {canceled_guest}")
canceled_guest = invited_people.pop()
print(f"I deeply apologise for cancelling the invitation, {canceled_guest}")
canceled_guest = invited_people.pop()
print(f"I deeply apologise for cancelling the invitation, {canceled_guest}")
print(f"{invited_people[0]}, the invitation isn't cancelled, I'll be waiting for you!")
print(f"{invited_people[1]}, the invitation isn't cancelled, I'll be waiting for you!")
del invited_people[1]
del invited_people[0]
print(invited_people)
