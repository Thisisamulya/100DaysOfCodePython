#Hangman Game {guessing words}

import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def arom():
    m=6
    for j in range(n+4):
        v=input("Enter a letter ").lower()
        for i in range(n):
            if v==x[i]:
                l.pop(i)
                l.insert(i,x[i])
        for j in l:
            print(j,end='')
        else:
            if v not in x:
                if m==0:
                    print(stages[0])
                    return False
                print(stages[m])
                m=m-1
        print()
    if '-' not in l:
        return True
        
my_wordl=["books","might","hidden","attack","golden","brazil","clothes","belong","paste","gallery","goosebumps","computer","imagine"]
x=random.choice(my_wordl)
n=len(x)
for i in range(n):
    print("_ ",end='')
print()
l=[]
for i in range(n):
    l.append("_")

s=arom()
        
if s==True:
    print("YOU WON !!, GAMEOVER")
else:
    print("GAMEOVER, you lost~")