# look what I did:
def new_section():
	print()
	print("----------")
	print()


# 8-9 Messages

def show_messages(message):
	for message in text_messages:
		print(message)

text_messages = ['lol', 'wtf', 'omw']

show_messages(text_messages)


new_section()


# 8-10 Sending messages

def show_messages(message):
	for message in text_messages:
		print(message)

def send_messages(messages):
	while text_messages:
		current_message = text_messages.pop()
		print(f"Moving {current_message}")
		sent_messages.append(current_message)
		print(f"Sent messages: {sent_messages}\n")

text_messages = ['lol', 'wtf', 'omw']
sent_messages = []

show_messages(text_messages)
print()
send_messages(sent_messages)


new_section()


# 8-11 Archived messages

print(f"Non-copied argument list: {text_messages}")

new_text_messages = ['rofl', 'k', 'omg']
send_messages(new_text_messages[:])
print(f"Copied argument list: {new_text_messages}")


