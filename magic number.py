import random
magic_number=random.randint(1,20)
attempts=0
while attempts<5:
    print("guess a number between 1 and 20")
    guess=int(input())
    attempts=attempts+1
    if guess==magic_number:
        break
print("you have guess the magic number")
