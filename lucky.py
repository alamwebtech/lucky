for num in range(1,21):
	if num == 4 or num == 13:
		state = "UNLUCKY"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} This is a {state} number")

for emoji in range(1,10):
	print("\U0001f600" * emoji)

for x in range(3):
	for emoji in range(1,10):
		print("\U0001f600" * emoji)