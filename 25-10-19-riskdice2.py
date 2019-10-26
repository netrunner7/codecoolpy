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

def dice_throw():
    diceoutcome = (random.randrange(1,6))
    return diceoutcome

def throw_and_set_attacker_dice():
    a1 = dice_throw()
    a2 = dice_throw()
    a3 = dice_throw() 
    attacker_list = [a1, a2, a3]
    attacker_list.sort(reverse = True)
    print(" Attacker: ", attacker_list[0] , "-" , attacker_list[1] , "-" , attacker_list[2])
    return attacker_list

def throw_and_set_defender_dice():
    d1 = dice_throw()
    d2 = dice_throw()
    defender_list = [d1, d2]
    defender_list.sort(reverse = True)
    print(" Defender: ", defender_list[0] , "-" , defender_list[1])
    return defender_list

def outcome(attackersortedlist, defendersortedlist):
    awin = 0
    dwin = 0
    for x in range(2):
        if attackersortedlist[x] > defendersortedlist[x]:
            awin += 1
        else:
            dwin += 1
    print(" Attacker: Lost", dwin , "units")
    print(" Defender: Lost", awin , "units")


def main():
    print("Dice:")
    attackersortedlist = throw_and_set_attacker_dice()
    defendersortedlist = throw_and_set_defender_dice()
    print("Outcome:")
    outcome(attackersortedlist , defendersortedlist)


main()
