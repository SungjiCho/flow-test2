from random import randint



chance = 3
answer = randint(1,100+1)
print(answer)

#def guess():
#    guess = int(input("Hi, guess the num(1 ~ 100)> "))
#    print(["Correct" if answer == guess else "Wrong"][0])
#for i in range(chance):
#    guess()


def jam_recursion(n):
    num = int(input("Hi, guess the num(1 ~ 100)> "))
    if n == 1:
        print("game over!")
        return False
    elif num == answer:
        print("==Correct!!==")
        return True
    else:
        n -= 1
        print("==Wrong!==")
        jam_recursion(n)


def guess():
    guess = int(input("Hi, guess the num(1 ~ 100)> "))
    print(["Correct" if answer == guess else "Wrong"][0])
for i in range(chance):
    guess()

def guess_sunny(n):
    chance = 0
    while chance < 4:
        guess = int(input('Guess the num(1~100)> '))
        chance = chance + 1
        if guess == answer:
            print('Correct!')
            break
        else:
            print('Wrong!')
