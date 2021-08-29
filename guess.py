import random
value = random.randint(1,100)
while True :
    guess  = int(input("Guess the number : "))
    if guess<value :
        print("Try a bit higher")
    elif guess>value :
        print("try a little lower")
    else :
        print("congratulations you won!!!")
        break


