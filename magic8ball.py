import random
#just messing about nothing really to see
print ("magic eight ball\n")

magic = ("As I see it, yes",
          "Ask again later",
          "Better not tell you now",
          "Cannot predict now",
          "Concentrate and ask again",
          "Don’t count on it",
          "It is certain",
          "It is decidedly so",
          "Most likely",
          "My reply is no",
          "My sources say no",
          "Outlook not so good",
          "Outlook good",
          "Reply hazy, try again",
          "Signs point to yes",
          "Very doubtful",
          "Without a doubt",
          "Yes",
          "Yes – definitely",
          "You may rely on it",
          )
while True:
  ballroll = int(random.randint(0,19))
  print("The ball speaks! \'",magic[ballroll],"\'")
  retry = input ("\nCall upon the ball again? Y/N: ").lower()
  if retry== "y":
    continue
print ("The ball falls quiet")
