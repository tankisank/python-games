import random
#rock beats scissors
#scissors beats paper
#paper beats rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
flag=False
def rpc(cc,pc):
    print(cc)
    print(pc)
    global flag
    if cc==rock and pc==paper:
        print("u lose")
        flag=True
    elif cc==rock and pc==scissors:
        print("u win")
        flag = True
    elif cc == paper and pc == scissors:
        print("u lose")
        flag = True
    elif cc == paper and pc == rock:
        print("u win")
        flag = True
    elif cc == scissors and pc == paper:
        print("u lose")
        flag = True
    elif cc == scissors and pc == rock:
        print("u win")
        flag = True
    else:
        flag=False




while flag==False:
    x = input("what do u choose rock,paper or scissors")
    if x == 'rock':
        playerchoice = rock
    elif x == 'paper':
        playerchoice = paper
    elif x == 'scissors':
        playerchoice = scissors
    else:
        playerchoice = rock
    computerchoice = random.choice([rock, paper, scissors])
    rpc(computerchoice, playerchoice)
