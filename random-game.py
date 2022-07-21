import random
r = random.randint(1,100)
i = 0 # count of guess
while True:
	print("This is", i , "times to guess")
	input_r = input("Please enter a number \n")
	i = i + 1
	input_r = int(input_r)
	if r == input_r:
		print("You guess right!")
		break
	elif r > input_r:
		print("This number is small than right answer!")
	else:
		print("This number is large than right answer!")
