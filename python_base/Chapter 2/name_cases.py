# 2.3
user_name = "Alex"
message = f"Hello {user_name}, could you help me with my studies today?"
print(message)

# 2.4
print(f"Username: {user_name.lower()}, {user_name.upper()}, {user_name.title()}")

# 2.5
message = 'Kurt Vonnegut once said, "True terror is to wake up one morning and discover that your high school class is running the country."'
print(message)

# 2.6
famous_person = "Kurt Vonnegut"
quote_text = "True terror is to wake up one morning and discover that your high school class is running the country."
message = f'{famous_person} once said, "{quote_text}"'
print(message)

# 2.7
user_name = "\tAlex \n"
print(user_name)
print(user_name.lstrip())
print(user_name.rstrip())
print(user_name.strip())