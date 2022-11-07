PLACEHOLDER = "[name]"
names = []

with open("Input/Names/invited_names.txt", mode="r") as file:
	names = file.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as letter:
	letter_contents = letter.read()

print(letter_contents)

for name in names:
	new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
	with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
		completed_letter.write(new_letter)