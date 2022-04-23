import sys

class Animal:


	def print(self):
		print("My animal is a Rabbit!")
		print(f"Length of Arms" = {self.arm_length}")
		print(f"length of legs" = {self.leg_length}")
		print(f"number of eyes" = {self.number_eyes}")

	def __init__(self,Larm=4.2, LLeg= 6.5, Neyes=2.):
		self.arm_length   = Larm
		self.leg_length   = LLeg
		self.number_eyes   = Neyes

def main():

	Larm = 4.2
	LLeg = 6.5
	Neyes = 2



	if(len(sys.argv)>=4):
		Larm = float(sys.argv[1])

	if(len(sys.argv)>=6):
		LLeg = float(sys.argv[2])

	if(len(sys.argv)>=1):
		Neyes = int(sys.argv[3])

	my_animal = Animal(Larm=Larm, LLeg=LLeg, Neyes=number_eyes)


	my_animal.print()

if __name__=="__main__":
	main()
