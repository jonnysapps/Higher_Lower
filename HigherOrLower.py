
def main():
	roll1 = (random.randint(1, 10))
	print(roll1)
	while True:
		roll2 = (random.randint(1, 10))
		time.sleep(1)
		choice1 = input("Higher or Lower?: ")
		time.sleep(1)
		print(roll2)
		if((choice1 == "Higher" or choice1 == "higher") and roll1 < roll2):
			print("correct")
			roll1 = roll2
		elif((choice1 == "Lower" or choice1 ==  "lower") and roll1 > roll2):
			print("correct")
			roll1 = roll2
		elif(roll1 == roll2):
			print("Call that one a tie?")
			continue
		else:	
			print("Incorrect")
			break
		 
import random
import time

print("Welcome to Jonny's Higher or Lower game")
time.sleep(1)
while True:
    main()
    replay = input("play again? (y/n): ")
    if(replay != "y"):
        break
time.sleep(1)
print("Thanks for playing!")

