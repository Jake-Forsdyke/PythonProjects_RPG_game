from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#black magic
fire=Spell("fire",10,100,"black")
thunder=Spell("thunder",10,100,"black")
blizzard=Spell("blizzard",10,100,"black")
meteor=Spell("meteor",20,200,"black")
quake=Spell("quake",14,140,"black")
#white magic
cure=Spell("cure",12,120,"white")
cura=Spell("cura",18,200,"white")

#create some items
potion=Item("potion","potion", "Heals 200 HP",200)
hipotion=Item("Hi-potion","potion", "Heals 100 HP",100)
superpotion=Item("super potion","potion", "Heals 500 HP",500)
elixer=Item("Elixer","elixer","fully restores HP/MP of one party member",9999)
hielixer=Item("Mega Elixer","elixer","fully restores party's HP/MP",9999)
grenade=Item("grenade","attack","deals 500 damage",500)
#magic=[{"name":"fire","cost":10,"dmg":60},
     #  {"name":"thunder","cost":10,"dmg":80},
      # {"name":"blizzard","cost":10,"dmg":60}]
player_spells=[fire,thunder,blizzard,meteor,quake,cure,cura]
enemy_spells =[fire,meteor,cure]
player_items=[{"item":potion,"quantity":15},
              {"item":hipotion, "quantity": 5},
              {"item":superpotion,"quantity":5},
              {"item":elixer,"quantity": 5},
              {"item":hielixer,"quantity": 2},
              {"item":grenade,"quantity":5}]

player1=Person("valos",3260,165,60,34,player_spells,player_items)
player2=Person("nick ",4160,235,60,34,player_spells,player_items)
player3=Person("phil ",3089,123,60,34,player_spells,player_items)
players=[player1,player2,player3]
enemy1=Person("Thanos",12000,500,345,25,enemy_spells,[])
enemy2=Person("Imp   ",1250,130,560,325,enemy_spells,[])
enemy3=Person("Imp   ",1250,130,560,325,enemy_spells,[])
enemies=[enemy1,enemy2,enemy3]
#print(player.gethp())
#print(enemy.gethp())

run=True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while run:
       print("===========================")
       print("\n\n")
       for player in players:
           print("name                  HP                                     MP")
           player.get_stats()

       print("\n")
       for enemy in enemies:
           enemy.get_enemy_stats()


       for player in players:
              player.choose_action()
              choice=input("choose action: ")
              index=int(choice)-1

              if index==0:
                     dmg=player.generate_damage()
                     enemy = player.choose_target(enemies)
                     enemies[enemy].take_damage(dmg)
                     print("you attacked "+enemies[enemy].name.replace(" ", "") + " for",dmg,"points of damage.")

                     if enemies[enemy].gethp() == 0:
                         print(enemies[enemy].name.replace(" ", "") + " has died.")
                         del enemies[enemy]
              elif index==1:
                     player.choose_magic()
                     magic_choice=int(input("choose magic: "))-1

                     if magic_choice ==-1:
                            continue
                   #  magic_dmg=player.generate_spelldamage(magic_choice)
                   # spell=player.get_spell_name(magic_choice)
                   #  cost=player.get_spell_mp_cost(magic_choice)

                     spell=player.magic[magic_choice]
                     magic_dmg=spell.generate_damage()

                     current_mp = player.get_mp()

                     if spell.cost > current_mp:
                         print(bcolors.FAIL+"\nnot enough MP\n"+bcolors.ENDC)
                         continue

                     player.reduce_mp(spell.cost)

                     if spell.type=="white":
                         player.heal(magic_dmg)
                         print(bcolors.OKBLUE+"\n"+ spell.name + " heals for",str(magic_dmg),"hp."+ bcolors.ENDC)
                     elif spell.type=="black":

                         enemy = player.choose_target(enemies)
                         enemies[enemy].take_damage(magic_dmg)

                         print(bcolors.OKBLUE+"\n"+spell.name+" deals",str(magic_dmg)," points of damage to "+enemies[enemy].name.replace(" ", "")+bcolors.ENDC,)

                         if enemies[enemy].gethp() == 0:
                             print(enemies[enemy].name.replace(" ", "") + " has died.")
                             del enemies[enemy]

              elif index ==2:
                     player.choose_item()
                     item_choice = int(input("choose item: ")) - 1
                     if item_choice ==-1:
                            continue
                     item = player.item[item_choice]["item"]

                     if player.item[item_choice]["quantity"]==0:
                            print(bcolors.FAIL+"\n"+"none left..."+bcolors.ENDC)
                            continue

                     player.item[item_choice]["quantity"] -= 1

                     if item.type =="potion":
                            player.heal(item.prop)
                            print(bcolors.OKGREEN + "\n" + item.name + " deals", str(item.prop), "points of healing" + bcolors.ENDC)

                     elif item.type=="elixer":
                            if item.name=="Mega Elixer":
                                for i in players:
                                     i.hp = player.maxhp
                                     i.mp = player.maxmp
                            else:
                                 player.hp= player.maxhp
                                 player.mp= player.maxmp
                            print(bcolors.OKGREEN+"\n" + item.name +" fully restores HP/MP"+ bcolors.ENDC)
                     elif item.type=="attack":

                            enemy = player.choose_target(enemies)
                            enemies[enemy].take_damage(item.prop)

                            print(bcolors.OKGREEN + "\n" + item.name + " deals",str(item.prop),"points of damage to" + enemies[enemy].name.replace(" ", "")+ bcolors.ENDC)

                            if enemies[enemy].gethp() == 0:
                                print(enemies[enemy.name.replace(" ", "") + " has died."])
                                del enemies[enemy]

       print("===========================")

       # check if battle is over
       defeated_heros = 0
       for player in players:
           if player.gethp() == 0:
               defeated_heros += 1

       defeated_enemies = 0
       for enemy in enemies:
           if enemy.gethp() == 0:
               defeated_enemies += 1
#check if enemy won
       if defeated_heros == 2:
           print(bcolors.FAIL + "your enemies have defeated you!" + bcolors.ENDC)
           run = False
#check if player won
       elif defeated_enemies == 2:
           print(bcolors.OKGREEN + "you win!" + bcolors.ENDC)
           run = False
       print("\n")

       # Enemy attack phase
       for enemy in enemies:
            enemy_choice = random.randrange(0, 2)

            if enemy_choice == 0:
                # Chose attack
               target = random.randrange(0, 3)
               enemy_dmg = enemies[0].generate_damage()

               players[target].take_damage(enemy_dmg)
               print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace("    :", "") + "for", enemy_dmg)

            elif enemy_choice == 1:
                    spell, magic_dmg = enemy.choose_enemy_spell()
                    enemy.reduce_mp(spell.cost)

                    if spell.type == "white":
                        enemy.heal(magic_dmg)
                        print(bcolors.OKBLUE + spell.name + " heals" + enemy.name + "for " + str(magic_dmg), "HP" + bcolors.ENDC)

                    elif spell.type == "black":
                        target = random.randrange(0, 3)
                        players[target].take_damage(magic_dmg)

                        print(bcolors.OKBLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals",
                              str(magic_dmg), "points of damage to " + players[target].name.replace("    :", "") + bcolors.ENDC)

                        if players[target].gethp() == 0:
                            print(players[target].name.replace(" ", "") + " has died.")
                            del players[target]










