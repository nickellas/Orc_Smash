import random

heroes = []
foes = []

def attack(target):
    print(turn, "attacks", target)
    attack_roll = random.randint(1,20)
    damage = turn.equipped["damage"]
    count = 0
    if attack_roll in turn.equipped["crit"]:
        crit_roll = random.randint(1,20) + turn.equipped["attack_bonus"]
        if crit_roll > target.AC:
            print(turn, "lands a critical hit on", target)
            for i in turn.equipped["damage_die"]:
                damage += random.randint(1,turn.equipped["damage_die"][count])
                count += 1
            damage *= turn.equipped["crit_mult"]
            print(damage)
        else:
            print(turn, "hits", target)
            for i in turn.equipped["damage_die"]:
                damage += random.randint(1,turn.equipped["damage_die"][count])
                count += 1
            print(damage)
    else:
        attack_roll += turn.equipped["attack_bonus"]
        if attack_roll > target.AC:
            print("Hit!")
            for i in turn.equipped["damage_die"]:
                damage += random.randint(1,turn.equipped["damage_die"][count])
                count += 1
            print(damage)
        else:
            print("miss")
            damage = 0
    target.HP -= damage
        
def death(target):
    print(target, "has been slain!")
    foes.remove(target)
    
    



class Orc(object):
    """ The titular foe of Orc Smash """ 
    def __init__(self,name):
        self.name = name
        self.ability_score = {"Str":17,"Dex":11,"Con":12,"Int":7,"Wis":8,
                              "Cha":6}
        self.ability_mod = {"Str": (self.ability_score["Str"]-10)//2,
                            "Dex": (self.ability_score["Dex"]-10)//2,
                            "Con": (self.ability_score["Con"]-10)//2,
                            "Int": (self.ability_score["Int"]-10)//2,
                            "Wis": (self.ability_score["Wis"]-10)//2,
                            "Cha": (self.ability_score["Cha"]-10)//2}
        self.HP = 5 + self.ability_mod["Con"]
        self.armor = 3
        self.AC = 10 + self.ability_mod["Dex"] + self.armor
        self.flatfooted_AC = 10 + self.armor
        self.touch_AC = 10 + self.ability_mod["Dex"]
        self.Fort_save = 3
        self.Ref_save = 0
        self.Will_save = -1
        self.CMD = 14
        self.CMB = 4
        self.weapon = {"weapon_name": "falchion", "attack_bonus":5,
                       "damage_die":[4,4], "damage":4, "crit":[18, 19, 20],
                       "crit_mult":2}
        self.weapon2 = {"weapon_name": "javalin", "attack_bonus":1,
                        "damage_die":[6], "damage":3, "crit":[20],
                        "crit_mult":2}
        self.equipped = self.weapon
        self.inventory = {"gold": 20, "weapon": {"weapon_name": "falchion",
                                             "attack_bonus":5,"damage_die":[4,4],
                                             "damage":4, "crit":[18, 19, 20],
                                             "crit_mult":2},
                          "weapon": {"weapon_name": "javalin", "attack_bonus":1,
                                   "damage_die":[6], "damage":3, "crit":[20],
                                   "crit_mult":2}}

    def switch_weapon(self):
        if self.equipped == self.weapon:
            self.equipped = self.weapon2
            print("Equipped", self.equipped["weapon_name"])
        else:
            self.equipped = self.weapon
            print("Equipped", self.equipped["weapon_name"])
        
    def __str__(self):
        rep = self.name
        return rep

Billy = Orc("Billy")
heroes.append(Billy)
turn = Billy

Karok = Orc("Karok")
foes.append(Karok)

print("An enemy appears. Prepare for battle!")
while foes != []:
    response = input("would you like to fight?")
    attack(Karok)
    for foe in foes:
        if foe.HP <= 0:
            death(foe)
        
print("Battle over!")
    

