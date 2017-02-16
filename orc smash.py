#Orc's have attacked and you must fight them

import random

print("You, Saege Endrison, Ulfan warrior, must face your first real challenge"
      "\nsince your defeat so long ago.")
print("\nAn Orc stands before you, This barbaric humanoid bears ragged equipment"
      "\nand armor in sullen colors. It has coarse body hair and a stooped"
      "\nposture like some primitive man but with a grayish-green skin and"
      "\nbestial features beneath a black hood. Burning red eyes peer"
      "\nbelow a low, sloping brow, just above a flattened nose, and"
      "\nprominent tusk-like teeth.")

hp=int(13)
pac=int(18)
pab=int(3)
orchp=int(11)
oac=int(13)
oab=int(5)


while hp>0:
    fight=input("\ndo you attack or defend?\n")
    if fight=="attack":
        attackroll=(random.randint(1,20)+pab)
        if attackroll > oac:
            pdam=(random.randint(1,8)+4)
            orchp-=pdam
            print("you strike the orc with your battleaxe, dealing", pdam,"damage."
                  "(the orc has", orchp,"health left)")
            if orchp<=0:
                break
        if attackroll<=oac:
            print("you swing your axe at the orc and miss.")
        orcattack=(random.randint(1,20)+oab)
        if orcattack>pac:
            odam=(random.randint(1,4)+random.randint(1,4)+4)
            hp-=odam
            print("The Orc swings his falcion fiercly, dealing", odam,"damage."
                  "(you have", hp,"health left)")
        if orcattack<=pac:
            print("The orc strikes at you and is deflected by your shield.")
    elif fight=="defend":
        print("You raise your sheild")
    

if hp<=0:
    print("You have been slain.")
if orchp<=0:
    print("You have slain your foe.")

input("Do you wish to play again?")
