from random import randrange
print("Integer Divisions!!")
a = randrange(5)
b = randrange(5)
print(a)
print(b)
answer=input("Enter the answer:")
try:
	c=a/b
	if(int(answer)==c):
		print("CORRECT!!")
	else:
		print("INCORRECT!!")
except:
	print("Please enter an integers Only!!")

