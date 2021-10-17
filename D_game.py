player = input("What is your name? ")
print("Hi" + " " + str(player))

def player_age():
	global age
	age = "This sentence will always be False in the loop"
	while age.isdigit() == False:
		age = input("What is your age? ")
		if age.isdigit() == False:
			print("Enter by number please!")
		else:
			return int(age)
player_age()
if int(age) > 18:
	print("\nWelcome to the Game!\n")    
else:
	print("Unqualified!")
	exit()

#First
First_question = input("You are watching your TV when you hear a sound. Do you check it?\n Yes\n No\n").lower()
if First_question == "yes":
	print("\nYou are dead!")
	exit()
if First_question == "no":
	pass
else:
	print("\nInvalid input!\nYou died")
	exit()

#Second
Second_question = input("\nYou keep watching, but the sound is getting louder. Will you check it?\n Yes\n No\n").lower()
if Second_question == "yes":
	print("\nYou died")
	exit()
if Second_question == "no":
	pass
else:
		print("\nInvalid input!\nYou died")
		exit()

#Third
print("\nThe TV shows some questions:")
class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

question_prompts = [
"Are you going to die tonight?\n yes\n no\n\n",
"\nAre you sure about that?\n yes\n no\n\n",
"\nOK?\n yes\n no\n\n",
]

question = [
	Question(question_prompts[0], "no"),
	Question(question_prompts[1], "yes"),
	Question(question_prompts[2], "yes"),
]

def Third_question(questions):
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			pass
		else:
			print("DIED!")
			exit()

Third_question(question)

#Fourth
Fourth_question = input("\nNoticing that the noise has stopped, you feel hungry\nWhen you walk into the kitchen, the electricity runs out\nYou saw something hiding in the dark. Check it?\n Yes\n No\n")
if Fourth_question == "yes":
	print("Oh, it was just a lamp placed in the corner")
if Fourth_question == "no":
	print("You start to feel nervous")
if Fourth_question != "yes" and Fourth_question != "no":
	print("...")
	exit()

