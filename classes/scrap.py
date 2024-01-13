print("\n\n")
print("name                  HP                                     MP")
print("                      _________________________              ________________")
print(bcolors.BOLD + "Valos:     "+" 460/460  |" + bcolors.OKGREEN + "█████                    " +
      bcolors.ENDC +
      bcolors.BOLD + "|    "+"65/65   |"+bcolors.OKBLUE + "█               "+bcolors.ENDC+"|")
print("                      _________________________              ________________")
print("Valos:      460/460  |                         |    65/65   |               |")
print("                      _________________________              ________________")
print("Valos:      460/460  |                         |    65/65   |               |")
print("\n\n")



print("                      _________________________               ____________")
        print(bcolors.BOLD + str(self.name) +"    "+str(self.hp)+"/"+str(self.maxhp)+"   |" + bcolors.OKGREEN + hp_bar +
              bcolors.ENDC +
              bcolors.BOLD + "|    " + str(self.mp)+"/"+str(self.maxmp)+"   |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")


def get_stats(self):
    hp_bar = ""
    bar_ticks = (self.hp / self.maxhp) * 100 / 4

    mp_bar = ""
    mp_ticks = (self.mp / self.maxmp) * 100 / 10

    while bar_ticks > 0:
        hp_bar += "█"
        bar_ticks -= 1

    while len(hp_bar) < 25:
        hp_bar += " "

    while mp_ticks > 0:
        mp_bar += "█"
        mp_ticks -= 1

    while len(mp_bar) < 10:
        mp_bar += " "

    # Ensuring that blank spaces are added when hp/mp decreased by a digit
    hp_string = str(self.hp) + "/" + str(self.maxhp)
    current_hp = ""
    if len(hp_string) < 9:
        decreased = 9 - len(hp_string)

        while decreased > 0:
            current_hp += " "
            decreased -= 1

        current_hp += hp_string
    else:
        current_hp = hp_string

    mp_string = str(self.mp) + "/" + str(self.maxmp)
    current_mp = ""
    if len(mp_string) < 7:
        decreased = 7 - len(mp_string)

        while decreased > 0:
            current_mp += " "
            decreased -= 1

        current_mp += mp_string
    else:
        current_mp = mp_string

    print("                     _________________________              __________ ")
    print(bcolors.BOLD + self.name + "     " +
          current_hp + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD +
          "|     " +
          current_mp + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    # enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # chose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemies[0].generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for ",
                  enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + " for ", str(magic_dmg),
                      " hp." + bcolors.ENDC)

            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals",
                      str(magic_dmg),
                      " points of damage to " + players[target].name.replace(" ", "") + bcolors.ENDC, )

                if players[target].gethp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[player]
        #  print("enemy chose ", spell," damage is ", magic_dmg)