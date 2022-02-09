#The following program is a text adventure game. You are a knowledgeable traveler scouting an unknown valley.
#You come across a village that has been stuck in a drought. With help of your knowledge of ancient myths, you go
#on an adventure to retrive the items necessary to activate the ancient legend and save the village.


#The following 3 variables determine whether or not you've collected a specific orb
green_orb = False
red_orb = False
blue_orb = False
#The following variable keeps track of the total amount of orbs you've collected
total_orbs = 0

#The following function is the universal battle system used for the game.
def Battle_System(area):
    #Sets enemies hp
    enemy_hp = 50
    #Sets player's hp
    hero_hp = 40
    #Loop keeps the battle going until the enemy is defeated unless you are defeated
    while enemy_hp > 0:
        print("\nEnemy hp: " + str(enemy_hp) + "\nYour hp: " + str(hero_hp))
        option = input("What will you do?\nFight     Heal\n\n")
        #Player can decide to fight or heal
        #Also displays enemies and player's health
        if option.lower() == "fight":
            print("\n\nYou attacked with your sword\nEnemy attacked back")
            enemy_hp -= 5
            hero_hp -= 6
            #If your health reaches zero, you die
            #Gives player option to retry or quit
            if hero_hp <= 0:
                game_option = input("\nYOU WERE DEFEATED\nGAME OVER\n\nRetry    End Game\n\n")
                if game_option.lower() == "retry":
                    if area == 1:
                        enemy_hp = 0
                        Howling_Forest()
                    elif area == 2:
                        enemy_hp = 0
                        Flaming_Peak()
                    elif area == 3:
                        enemy_hp = 0
                        Eerie_Swamp()
                elif game_option.lower() == "end game":
                    quit()
        #Player can heal. Will increase their health by a set amount
        #Player can't go over their max health
        elif option.lower() == "heal":
            if hero_hp < 40:
                hero_hp += 4
                if hero_hp >= 40:
                    hero_hp = 40
                    print("\n\nYour hp is maxed out")
                print("\n\nYou healed")
            elif hero_hp == 40:
                 print("\n\nYour hp is maxed out")
        else: print("\n\nInvalid input, try again")
    print("\nENEMY DEFEATED\nBATTLE OVER")

#Function plays dialogue and battle of Eerie Swamp location
def Eerie_Swamp():
    print("\n*As you tread through the marshlands of the Eerie Swamp, you see a little house suspended over the swamp.\
    \nSuddenly you see an arrow skim right pass you, narrowly missing your throat.*\n\n???: 'Who are you? Why are you here?'\
    \nYou: 'Uhh hi. I'm looking for an orb? Who are you?'\n???: I'm a mage, protectorate of the blue orb. Now, why do you need the orb!?\
    \nYou: 'A village needs it. To solve their drought.'\nMage: Hmmmm. I would give it, but you need to show me you are strong enough to handle the orb.\
    \nI challenge you to a battle! If you win, I'll give you the orb. Lose and you must leave!\n\nBATTLE START")

    Battle_System(3)

    print("\nMage: 'Hmmm you are indeed a strong warrior! Here, take this orb!'\n\n*The mage handed you the blue orb and healed you up*\
    \n\nMage: 'I wish luck upon you and your village! Good luck!'\n\n*You return to the crossroads*\n")
    return True

#Function plays dialogue and battle of Flaming Peak location
def Flaming_Peak():
    print("\n*As you climb the rocky slope of the Flaming Mountains, you reach Flaming Peak.\nYou notice a cave with a torch at the entrance. You take it and enter.\
    \nYou see a light beam shining down on an old pedestal holding a red orb.\nYou walk up to the pedestal and then suddenly hear a roar!*\
    \n\n???: *Roarrrrr* 'Don't touch the orb!!!'\n\n*You see something flying towards you and realize...it's a dragon!*\
    \n\nYou: 'Sorry sorry! I just need that orb!'\nDragon: 'Fool! I'm the gaurdian of this orb! I can't just give it to anyone!\
    \nBut...if you were able to defeat me in battle, I'll give it to you!\n\nBATTLE START")

    Battle_System(2)

    print("\nDragon: 'Wow wasn't expecting to lose that! You really want this orb!'\nWell a promise is a promise, here ya go!'\
    \n\n*The dragon gives you the red orb and heals you up*\n\nDragon: 'I wish you luck on your journey!'\n\n*You return to the crossroads*\n")
    return True

#Function plays dialogue and battle of Howling Forest location
def Howling_Forest():
    print("\n*As you travel further into the deep woods, you spot a clearing.\nThere, you see an old pedestal with a green orb on it.\
    \nAs you approch to collect it you hear a loud growl*\n\n???: 'Grrrrrr! Who goes there!'\n\n*You see a large werewolf jump out from the bushes*\
    \n\nWerewolf: 'What business do you have here human!?'\nYou: 'Oh uh sorry I'm just here to get this orb.'\
    \nWerewolf: 'I'm the protector of this orb! If you want it, you'll have to fight me in battle for it!\nAwwwoooooo'\n\nBATTLE START")
    
    Battle_System(1)

    print("\nWerewolf: 'Hmm you are strong human. Here, take this.'\n\n*You got the green orb and the werewolf heals you up*\n\nWerewolf: 'Good luck on your journey human'\
    \n\n*You return to the crossroads*\n")
    return True

#Function gives a nice visual to the player of the different paths to take.
#Function also prompts player for decision of where to go.
def crossroads():
    print("\ 1\      |2|      /3/")
    print(" \  \     | |     / / ")
    print("  \  \    | |    / /  ")
    print("   \  \   | |   / /   ")
    print("    \  \  | |  / /    ")
    print("     \  \ | | / /     ")
    print("      \  \| |/ /      ")
    print("       \      /       ")
    print("        \    /        ")
    print("         |  |         ")
    print("         |  |         ")
    print("         |  |         ")
    return int(input("Enter the number of the path you would like take: "))

#Following gives an intro to the game and sets up the player for what the game is about
print("*On your trek through an unknown valley, you encounter a small village. The village is bare.\
\nYou notice the lack of vegetation and the carvings of what might have used to be a river.\nFrom the distance you see a man approach you.*\
\n\nYou: 'Hi hello, who are you?' \n???: 'Hello, I am the mayor of this village'\nYou: 'Uhhh...nice village you got there?'\
\nMayor: 'Yeah? Well it used to be better. A large river used to flow through, lots of fertile soil to grow crops.\nBut for 2 weeks now\
 we've gotten nothing but hot sun! The river has dried up and the crops have died off. Our village is at a crisis.\
\n\n*You look around at the desolate land, but then notice a strange structure in the middle of the village.*\
\n\nMayor: 'Oh that? I wish I could tell you more about it, but I know nothing about it. All I know is that it's been here for centuries.'\
\nYou: 'No no, I recognize this! This is an ancient statue of the goddess of nature!'\
\n\n*You dusted off the plaque on the statue and read it* \n'Green, red and blue. When combined shall bring natural prosperity'\
\n*You also notice 3 holes in front of the statue that seem to fit orbs*\
\n\nYou: 'Yes! I think there are 3 orbs that must be collected, and with that, should solve this drought!'\
\nMayor: 'Oh! Thank you so much traveller! Here's a sword, a shield and some food! Please retrive those orbs!'\
\nYou: 'Uhhh what??? I didn't sign up for this!\nMayor: 'Please! I'm desperate! Only you know how to fix this!'\nYou: 'Ok fine, I'll do it'\
\nMayor: 'Excellent! Good luck!'")
print("\n*As you left the village, you reach a crossroad*\n  Path 1 on the left leads to Howling Forest.\n  Path 2 straight ahead leads to Flaming Peak.\
\n  Path 3 on the right leads to Eerie Swamp.\n")

#This loop handles the core layout of the adventure
#This loop will iterate until the player retrives all 3 orbs
while total_orbs < 3:
    option_num = crossroads()
    if option_num == 1:
        if green_orb == False:
            green_orb = Howling_Forest()
            total_orbs += 1
        else: print("\n*You've already been there*\n")
    elif option_num == 2:
        if red_orb == False:
            red_orb = Flaming_Peak()
            total_orbs += 1
        else: print("\n*You've already been there*\n")
    elif option_num == 3:
        if blue_orb == False:
            blue_orb = Eerie_Swamp()
            total_orbs += 1
        else: print("\n*You've already been there*\n")
    else: print("Invalid entry. Please select 1, 2 or 3")

#Dialogue and conclusion of the game. Only displays once player finds all three orbs.
print("*With all 3 orbs in your possession, you hurry back to the village*\n\nYou: 'Mr. Mayor! I've done it! I have all 3 orbs!'\
\nMayor: 'Amazing work! I knew you could do it!'\n\n*You place the orbs one by one into the designated holes.\
\nYou notice that the sky has quickly darkened, with a singular hole in the clouds\nallowing sunlight to shine upon the statue.\
\nSuddenly, you feel rumbling. You look to the distance and see a wave of water\nflowing down what used to be the river.*\
\n\nMayor: 'Hurray! You've done it! You've brought hope back to our village!\nYou are a hero to us all!\
 Thank you again traveller! May your journey be a fulfilling one!'\n\n*As you go off into the distance, you look back and smile at your\
 accomplishment.*\n\nTHE END\n\n")

#Player presses enter to exit game
input("*Press enter to exit*")