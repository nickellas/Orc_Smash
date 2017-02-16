point_buy = {7:-4, 8:-2, 9:-1, 10:0, 11:1, 12:2, 13:3, 14:5, 15:7, 16:10, 17:13,
             18:17}

ability_score = {"strength": 10, "dex": 10, "con": 10, "wis": 10,
                  "intelligence": 10, "cha": 10}

stat_point = point_buy[ability_score["strength"]] + point_buy[ability_score["dex"]] + point_buy[ability_score["con"]] + point_buy[ability_score["wis"]] + point_buy[ability_score["intelligence"]] + point_buy[ability_score["cha"]]


print("Ability score demo.")


done = "not done"
while done != 0 or stat_point <= 20:
    for i in ability_score:
        print(i, ": ", ability_score[i])
    print("point buy remaining: ", 20-stat_point)
    stat = input("select a stat to change (strength, dex, con, wis, intelligence, cha): ")
    if stat in ability_score:
        ability_score[stat] = int(input("what would you like this stat to be?"))
        stat_point = point_buy[ability_score["strength"]] + point_buy[ability_score["dex"]] + point_buy[ability_score["con"]] + point_buy[ability_score["wis"]] + point_buy[ability_score["intelligence"]] + point_buy[ability_score["cha"]]
        

