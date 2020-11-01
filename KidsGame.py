from random import randrange
class Animal:
	print("Welcome to the guessing Game!!")
	
	def __init__(self, name):
		self.name = name

	def guess_who_am_i(self):
		print("I will give you 3 hints, guess what animal I am")
		guess_option=randrange(0,3)
		if guess_option>0:
			guess_tries=1
			while guess_tries<3:
				if guess_tries>1:
					print("I have exceptional memory")
					answer=input("Who am I?:")
				else:
					print("I am the largest land-living mammal in the world")
					answer=input("Who am I?:")

				if(answer=='elephant'):
					print("You got it! I am",e.name)
					exit()
				else:
					print("Nope,try again")
					guess_tries+=1
			print("I am out of hints! the answer is:",e.name)
			exit()
		elif guess_option==1:
			guess_tries=1
			while guess_tries<3:
				if guess_tries>1:
					print("I am the biggest cat")
					answer=input("Who am I?:")
				else:
					print("I come in black and white or orange and black")
					answer=input("Who am I?:")

				if(answer=='tiger'):
					print("You got it! I am",t.name)
					exit()
				else:
					print("Nope,try again")
					guess_tries+=1
			print("I am out of hints! the answer is:",t.name)
			exit()
		else:
			guess_tries=1
			while guess_tries<4:
				if guess_tries>2:
					print("I use echo-location")
					answer=input("Who am I?:")
				elif guess_tries>1:
					print("I can fly")
					answer=input("Who am I?:")
				else:
					print("I see well in dark")
					answer=input("Who am I?")

				if(answer=='bat'):
					print("You got it! I am",b.name)
					exit()
				else:
					print("Nope,try again")
					guess_tries+=1
			print("I am out of hints! the answer is:",b.name)
			exit()

e= Animal("elephant")
t = Animal("tiger")
b=Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()


