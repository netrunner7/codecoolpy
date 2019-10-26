# When the attacker's die value is larger: Attacker wins (1 defender unit dies)
# When the 2 dice value is tie: Defender wins (1 attacker unit dies)
# When the defender's die value is larger: Defender wins (1 attacker unit dies)
# Attacker: Lost x units
# Defender: Lost x units

import random
# print(random.randrange(1,6))

a1 = 0           # kosc atakujacego1
a2 = 0
a3 = 0
d1 = 0           # kosc bronionacego1
d2 = 0

def readNumber3(text):
    isCorrect = False
    num = 0

    while isCorrect == False:
        userInput = input(text)
        userInputint = int(userInput)

        if userInputint <=3 and userInputint >0:
            num = int(userInput)
            isCorrect = True
        else:
            print("Type 1 , 2 or 3")
    
    return num

def readNumber2(text):
    isCorrect = False
    num = 0

    while isCorrect == False:
        userInput = input(text)
        userInputint = int(userInput)

        if (userInput.isdigit()) and userInputint <=2 and userInputint >0:
            num = int(userInput)
            isCorrect = True
        else:
            print("Type 1 , 2 or 3")
    
    return num

def dice_throw():
    diceoutcome = (random.randrange(1,6))
    return diceoutcome

def throw_and_set_attacker_dice(number_of_attackers):
    if number_of_attackers > 0:
        a1 = dice_throw()
        attacker_list = [a1]
    if number_of_attackers > 1:
        a2 = dice_throw()
        attacker_list = [a1, a2]
    if number_of_attackers > 2:
        a3 = dice_throw()
        attacker_list = [a1, a2, a3]
    
    attacker_list.sort(reverse = True)
    if number_of_attackers > 2:
        print(" Attacker: ", attacker_list[0] , "-" , attacker_list[1] , "-" , attacker_list[2])
    elif number_of_attackers > 1:
        print(" Attacker: ", attacker_list[0] , "-" , attacker_list[1])
    elif number_of_attackers >0:
        print(" Attacker: ", attacker_list[0])
    
    
    
    return attacker_list

def throw_and_set_defender_dice(number_of_defenders):
    if number_of_defenders > 0:
        d1 = dice_throw()
        defender_list = [d1]
    if number_of_defenders > 1:
        d2 = dice_throw()
        defender_list = [d1, d2]
    defender_list.sort(reverse = True)
    if number_of_defenders > 1:
        print(" Defender: ", defender_list[0] , "-" , defender_list[1])
    elif number_of_defenders > 0:
        print(" Defender: ", defender_list[0])
    return defender_list

# fix it!

def outcome(attackersortedlist, defendersortedlist):

    awin = 0
    dwin = 0
    if len(attackersortedlist) > len(defendersortedlist):
        longerlist = len(attackersortedlist)
    else:
        longerlist = len(defendersortedlist)
    if len(attackersortedlist) == len(defendersortedlist):
        for x in range(1 , longerlist):
            if attackersortedlist[x] > defendersortedlist[x]:
                awin += 1
            else:
                dwin += 1
    print(" Attacker: Lost", dwin , "units")
    print(" Defender: Lost", awin , "units")


def main():
    attackernum = readNumber3("How many attackers are there? ")
    defendernum = readNumber2("How many defenders are there? ")
    print("Dice:")
    attackersortedlist = throw_and_set_attacker_dice(attackernum)
    defendersortedlist = throw_and_set_defender_dice(defendernum)
    print("Outcome:")
    outcome(attackersortedlist , defendersortedlist)


main()
