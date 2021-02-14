import random

ex: bool = False

while(ex != True):

    rand = random.randint(1, 6)
    print(f"you'r dice rolling is {rand}")

    answerForExit = input("Do you want play again? (y/n): ")
    if answerForExit == 'n':
        ex = True
