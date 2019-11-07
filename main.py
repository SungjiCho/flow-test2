chance = 3
answer = randint(1,100+1)
print(answer)
  
def guess():
   guess = int(input("Hi, guess the num(1 ~ 100)> "))
   print(["Correct" if answer == guess else "Wrong"][0])
for i in range(chance):
    guess()
