# Character creation module

# Stat Progression blocks by level

character_level = 1

Good_save = {1:2,2:3,3:3,4:4,5:4}
Poor_save = {1:0,2:0,3:1,4:1,5:1}

Good_BAB = character_level
Med_BAB = character_level * 3//4
Poor_BAB = character_level * 1//2

import pickle, pointbuy
character_name = input("What is your characters name?")
pointbuy.point_buy()


f = open("character1.dat", "wb")
pickle.dump(character_name, f)
f.close()

f = open("character1.dat", "rb")
character_name = pickle.load(f)

print(character_name)
f.close
