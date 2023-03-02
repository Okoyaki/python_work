# 8.11 (code from 8.10)
def send_messages(unsent_messages, sent_messages):
	while unsent_messages:
		msg = unsent_messages.pop()
		print(f"Sending message: {msg}")
		sent_messages.append(msg)

def show_messages(messages):
	for message in messages:
		print(message.title())

unsent_messages = ['hello', 'yo', 'bye', 'who']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)
show_messages(sent_messages)

print(unsent_messages)
print(sent_messages)