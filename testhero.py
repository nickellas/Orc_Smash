class Humanfighter(object):
    def __init__(self, name):
        self.name = name
        self.ability_score = {"Str":18,"Dex":14,"Con":15,"Int":10,"Wis":12,
                              "Cha":7}
        self.ability_mod = {"Str": (self.ability_score["Str"]-10)//2,
                            "Dex": (self.ability_score["Dex"]-10)//2,
                            "Con": (self.ability_score["Con"]-10)//2,
                            "Int": (self.ability_score["Int"]-10)//2,
                            "Wis": (self.ability_score["Wis"]-10)//2,
                            "Cha": (self.ability_score["Cha"]-10)//2}
        self.maxHP = 11 + self.ability_mod["Con"]
        self.HP = self.mxHP
        self.armor = 3
        self.shield = 1
        self.AC = 10 + self.ability_mod["Dex"] + self.armor + self.shield
        self.flatfooted_AC = 10 + self.armor + self.shield
        self.touch_AC = 10 + self.ability_mod["Dex"]
        self.Fort_save = 4
        self.Ref_save = 2
        self.Will_save = 1
        self.CMD = 17
        self.CMB = 5
        self.weapon = {"weapon_name": "battleaxe", "attack_bonus": 3,
                       "damage_die":[8], "damage":4, "crit":[20],
                       "crit_mult": 3, "type": "slashing"}
        self.weapon2 = {"weapon_name": "light steel shield", "attack_bonus":3,
                        "damage_die":[4], "damage":4, "crit":[20],
                        "crit_mult":2, "type": "bludgeoning"}
        self.equipped = [self.weapon, self.weapon2]
        self.inventory = {"gold": 91, "weapon": {"weapon_name": "battleaxe", "attack_bonus": 3, "damage_die":[8], "damage":4, "crit":[20], "crit_mult": 3, "type": "slashing"}
                          "shield": {"weapon_name": "light steel shield", "attack_bonus":3, "damage_die":[4], "damage":4, "crit":[20], "crit_mult": 2, "type": "bludgeoning"}

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



