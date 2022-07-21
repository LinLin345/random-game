import random
r = random.randint(1,100)
while True:
	input_r = input("Please enter a number \n")
	input_r = int(input_r)
	if r == input_r:
		print("You guess right!")
		break
	elif r > input_r:
		print("This number is small than right answer!")
	else:
		print("This number is large than right answer!")
