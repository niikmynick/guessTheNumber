from random import randint
from math import log2, ceil


def enterLimit():
    global limit
    if input('you can choose difficulty of game\ndo you want to play with numbers from 1 to 100?\n') == 'no':
        limit = int(input('enter limit number here:    '))
        print('ok, we starting now')
    else:
        print('ok, we starting now')


def isValid(s):
    global limit
    return s.isdigit() and 1 <= int(s) <= limit or s == 'stop'


def playAgain():
    if input('want play again? (yes / no)\n') == 'yes':
        return True
    else:
        return False


def checkInput(i):
    global n
    global count
    if int(i) < n:
        print('your num is lower, try again')
        return True
    elif int(i) > n:
        print('your num is higher, try again')
        return True
    else:
        print('you are right!')
        print('attempts:', count)
        print(f'i got a score in {ceil(log2(limit))} attempts')
        if playAgain():
            enterLimit()
            print('number is selected')
            n = randint(1, limit)
            count = 0
            return True
        else:
            return False


def game():
    global count
    print("Hi, welcome to 'guess the number' game")
    enterLimit()
    print('number is selected')
    while True:
        count += 1
        inp = input()
        if isValid(inp):
            if inp == 'stop' or not checkInput(inp):
                print('Bye!')
                break
        else:
            print(f'you need to enter a number from 1 to {limit}')


count = 0
limit = 100
n = randint(1, limit)
game()
