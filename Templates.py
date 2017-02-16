class Creature(object):
    def target(self):
        target = self

    def death(self):
        if HP <= -1 * con:
            self = dead
            

class Aberration(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Poor_save
        base_will = Good_save

    def traits(self):
        traits = [darkvision(60)]


class Animal(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Good_save
        base_ref = Good_save
        base_will = Poor_save

    def traits(self):
        traits = [low_light_vision]

class Construct(Creature):
    def HD(self):
        HD = 10

    def BAB(self):
        BAB = Good_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Poor_save
        base_will = Poor_save

    def traits(self):
        super(Construct, self).HP()
        HP = HD * character_level

        super(Contruct, self).death()
        if HP <= 0:
            self = dead

        traits = [low_light_vision, darkvision(60)]

        immunities = [mind_effecting, bleed, disease, death_effect, necromancy,
                      paralysis, poison, sleep, stun, healing, ability_damage,
                      ability_drain, fatigue, exhaustion, energy_drain,
                      nonlethal_damage, resurrection]
        
        fort_save = None
     

class Dragon(Creature):
    def HD(self):
        HD = 12

    def BAB(self):
        BAB = Good_BAB

    def Saves(self):
        base_fort = Good_save
        base_ref = Good_save
        base_will = Good_save
        
    def traits(self):
        traits = [darkvision(60), low_light_vision]
        immunities = [sleep, paralysis]

class Fey(Creature):
    def HD(self):
        HD = 6

    def BAB(self):
        BAB = Poor_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Good_save
        base_will = Good_save

    def traits(self):
        traits = [low_light_vision]

class Humanoid(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Poor_save
        base_will = Poor_save

class Magical_beast(Creature):
    def HD(self):
        HD = 10

    def BAB(self):
        BAB = Good_BAB

    def Saves(self):
        base_fort = Good_save
        base_ref = Good_save
        base_will = Poor_save

    def traits(self):
        traits = [darkvision(60), low_light_vision]

class Monstrous_humanoid(Creature):
    def HD(self):
        HD = 10

    def BAB(self):
        BAB = Good_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Good_save
        base_will = Good_save
        
    def traits(self):
        traits = [darkvision]

class Ooze(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Poor_save
        base_will = Poor_save
        
    def traits(self):
        immunities = [gaze, illusion, mind_effecting, poison, sleep, paralysis,
                      polymorph, stun, crit, flanking, precision]
        

class Outsider(Creature):
    def HD(self):
        HD = 10

    def BAB(self):
        BAB = Good_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Poor_save
        base_will = Poor_save
        
    def traits(self):
        immunity = [resurrection]

class Plant(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Good_save
        base_ref = Poor_save
        base_will = Poor_save
        
    def traits(self):
        traits = [low_light_vision]
        immunities = [mind_effecting, paralysis, poison, polymorph, sleep, stun]

class Undead(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Poor_save
        base_ref = Poor_save
        base_will = Good_save

    def traits(self):
        super(Undead, self).HP()
        HP_per_level = HD + cha_mod
        HP = HP_per_level * character_level

        super(Undead, self).death()
        if HP <= 0:
            self = dead

        traits = [darkvision(60)]

        immunities = [mind_effecting, bleed, disease, death_effect, paralysis,
                      poison, sleep, stun, ability_damage,fatigue, exhaustion,
                      energy_drain,nonlethal_damage, strength_damage,
                      dexterity_damage, constitution_damage, resurrection]
        
        super(Undead, self).fort_save()
        fort_save = base_fort + cha_mod

class Vermin(Creature):
    def HD(self):
        HD = 8

    def BAB(self):
        BAB = Med_BAB

    def Saves(self):
        base_fort = Good_save
        base_ref = Poor_save
        base_will = Poor_save

    def traits(self):
        trait = [darkvision(60)]
        immunities = [mind_effecting]
