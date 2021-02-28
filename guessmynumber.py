import random
# this imports the random module
def numcheck(message):
  while True:
    try:
      message = int(input(message))
      if message <= 0:
        message = "Sorry i need a valid positive number: "
        continue
      if message > 5:
        message = "Sorry i need a number between 1 and 5: "
        continue
      else:
        return message
    except:
        message = "Sorry i need a valid number: "

print("My Guessing Game \nto save the world guess the right number")
name=input("what is your name? ").lower()
print("hello ",name, ". ready to save the world?")
guesscount = 0
secret = random.randint(1, 5)

while True:
    
  print(secret)
  guesscount += 1
  print("\nI am guessing a number between 1 and 5\n")
  myGuess = numcheck("what is your guess? ")
  if guesscount <= 10:
      if secret == myGuess:
        print("\nYou guessed right! well done the world is safe\n\t HORRAY!!")
        print("\n\t you guessed in",guesscount,"tries")
      elif myGuess < secret:
        print("\nyou guess is too low")
        print(" you have",guesscount-10,"guess left")
        continue
      elif myGuess > secret:
        print("\nyou guess is too high")
        print(" you have", guesscount - 10, "guess left")
        continue
      else:
        print("\nOh dear! You guessed wrong! the Answer was ",secret ," your guess was ", myGuess,"\n\t KABOOM!!")

  retry=input("try again? Y/N: ").lower()
  if retry == "y":
      guesscount = 0
      secret = random.randint(1, 5)
      continue
  else:
      break
print("Thank you for playing",name)
