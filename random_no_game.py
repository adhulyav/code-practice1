import random
def game():
 count=0
 number=random.randint(1,100)
 while True:
  guess=int(input("Enter a number between 1 to 100: "))
  if guess== number:
    print("you guessed the number!")
    count+=1
    break
  elif guess < number:
    print("you guessed number is low")
    count+=1
  elif guess > number:
    print("you guessed number is high")
    count+=1
 print("you guessed the number in",count,"tries")
game()