"""
COMP 163 - Project 1: Character Creator & Saving/Loading
name: Cameron Love
Date: October 29th, 2025

AI Usage: AI helped walk me through how I can change my code to only accept valid classes. Helped me parse the data in the load character function. As well as helping me with my git commits
"""
import os
import random

def create_character(name, character_class):
    
    character_stats = calculate_stats(character_class, 1) # Calls the calculate_stats function and assigns the charaters stats based on what class they selected

    if character_stats == None: #If the user entered an invalid class then then create character function returns None
        return None

    character = { #Creates users character
        "name" : name,
        "class" : character_class,
        "level" : 1,
        "strength" : character_stats[0],
        "magic" : character_stats[1],
        "health" : character_stats[2],
        "gold" : 0
    }

    return character #Returns the character dictionary

def calculate_stats(character_class, level):
    valid_class = True #Boolean that will be used later to handle invalid class input
    #Initializing stats
    strength = 0
    magic = 0
    health = 0

    #Assigns character stats based on class selection and level
    if character_class == "Warrior":
        strength = 58 + (level * 2)
        magic = 18 + (level * 2)
        health = 58 + (level * 2)
    elif character_class == "Mage":
        strength = 18 + (level * 2)
        magic = 58 + (level * 2)
        health = 38 + (level * 2)
    elif character_class == "Rogue":
        strength = 38 + (level * 2)
        magic = 38 + (level * 2)
        health = 18 + (level * 2)
    elif character_class == "Cleric":
        strength = 38 + (level * 2)
        magic = 58 + (level * 2)
        health = 58 + (level * 2)
    else:
        valid_class = False # If the user enters something other then the 4 valid classes then valid class turns false

    if  valid_class == True: # Returns character stats if user enters valid class
        character_stats = (strength, magic, health)
        return character_stats
    else: #Returns error message and none if user enters invald class
        print(f"Error: '{character_class}' is not a valid class.")
        return None

def save_character(character, filename):
    valid_file = True #Boolean that will be used later to handle invalid class file

    with open (filename, "w+") as character_file: # Writes character stats in text file by access character dictionary values
        character_file.write(f"Character name: {character["name"]}\n")
        character_file.write(f"class: {character["class"]}\n")
        character_file.write(f"level: {character["level"]}\n")
        character_file.write(f"strength: {character["strength"]}\n")
        character_file.write(f"magic: {character["magic"]}\n")
        character_file.write(f"health: {character["health"]}\n")
        character_file.write(f"gold: {character["gold"]}\n")
    
    if os.path.isfile(filename) == True: #If filename is an existing file then this will return true
        valid_file = True
    else:
        valid_file = False

    return valid_file
        


def load_character(filename):
    
    if os.path.isfile(filename) == True: #File will only open if it already exist
        with open(filename, "r") as character_file:
            character_stats = character_file.readlines() #Reads the file and returns a list of strings where the first element is the first line and so on
            
            #Seperates the left and right of the colon, mainly get the string to the right of the colon. Then accesses the name using index [1] and .strip to get rid of the newline
            character_class = character_stats[1].split(': ')[1].strip()
            name = character_stats[0].split(': ')[1].strip()
            level = int(character_stats[2].split(': ')[1].strip())
            strength = int(character_stats[3].split(': ')[1].strip())
            magic = int(character_stats[4].split(': ')[1].strip())
            health = int(character_stats[5].split(': ')[1].strip())
            gold = int(character_stats[5].split(': ')[1].strip())

            #Reassigns the characters stats
            character = {
                "name" : {name},
                "class" : {character_class},
                "level" : {level},
                "strength" : {strength},
                "magic" : {magic},
                "health" : {health},
                "gold" : {gold}
            }

            return character #Returns the character dictionary
    else: # If the file does not exist then the fuction returns none
        return None
    

def display_character(character): #Simply displays the character stats in the console
    print("=== CHARACTER SHEET ===")
    print(f"name : {character['name']}")
    print(f"class : {character['class']}")
    print(f"level : {character['level']}")
    print(f"strength : {character['strength']}")
    print(f"magic : {character['magic']}")
    print(f"health : {character['health']}")
    print(f"gold : {character['gold']}")


def level_up(character): 
    
    character["level"] += 1 #Adds a level to the character
    
    new_stats = calculate_stats(character["class"], character["level"]) # Calcules the characters new stats with the additional level

    #Assigns the new stats to the original character stats
    character["strength"] = new_stats[0] 
    character["magic"] = new_stats[1]
    character["health"] = new_stats[2]


"""
Function I created for bonus points. Added a dodge and block stat
"""

def extensive_stat_calculate(character_class, level):
    valid_class = True
    strength = 0
    magic = 0
    health = 0
    dodge = 0
    block = 0 

    if character_class == "Warrior":
        strength = 58 + (level * 2)
        magic = 18 + (level * 2)
        health = 58 + (level * 2)
        dodge = 18 + (level * 2)
        block = 58 + (level * 2)
    elif character_class == "Mage":
        strength = 18 + (level * 2)
        magic = 58 + (level * 2)
        health = 38 + (level * 2)
        dodge = 38 + (level * 2)
        block = 18 + (level * 2)
    elif character_class == "Rogue":
        strength = 38 + (level * 2)
        magic = 38 + (level * 2)
        health = 18 + (level * 2)
        dodge = 58 + (level * 2)
        block = 18 + (level * 2)
    elif character_class == "Cleric":
        strength = 38 + (level * 2)
        magic = 58 + (level * 2)
        health = 58 + (level * 2)
        dodge = 38 + (level * 2)
        block = 38 + (level * 2)

    else:
        valid_class = False

    if  valid_class == True:
        character_stats = (strength, magic, health, dodge, block)
        return character_stats
    else:
        print(f"Error: '{character_class}' is not a valid class.")
        return None

"""
Function I created for bonus points. Gives each class 2 specil abilities that temporarily boost their stats
"""

def special_abilities(character_class, level):

    buffed_stats = extensive_stat_calculate(character_class, level) #Grabs stats from extensive_stat_calculate function
    
    if buffed_stats is None: #Returns None if extensive_stat_calculate returns None
        return None

    #Assigns stat names to stat numbers from characters orginal stats
    strength = buffed_stats[0]
    magic = buffed_stats[1]
    health = buffed_stats[2]
    dodge = buffed_stats[3]
    block = buffed_stats[4]

    """
    Each class comes with two unique special abilities that Temporarily one of their stats.
    Special abilities are based off of the archetype of the class
    User enters the string 1 or 2 to choose between special abilities
    """

    if character_class == "Warrior":
        print("Choose your special ability!")
        user_input =  input("1) Last Stance (Temporarily Boost HP *only works if 20 hp*)\n2) Rage (Temporarily Boost Strength)\n")
        if user_input == "1":
            if health <= 20:
                health += (40 + (level * 2))
        elif user_input == "2":
            strength += (20 + (level * 2))
        else:
            print("Wrong Input")
    
    if character_class == "Mage":
        print("Choose your special ability!")
        user_input =  input("1) Magic Musisarus (Temporarily Boost Magic Stat) \n2) Healing of Osiris (Temporarily Boost HP)\n")
        if user_input == "1":
            magic += (20 + (level * 2))
        elif user_input == "2":
            health += (20 + (level * 2))
        else:
            print("Wrong Input")
    
    if character_class == "Rogue":
        print("Choose your special ability!")
        user_input =  input("1) Assasination (50% Chance of Insta-Kill) \n2) Perfect Dodge(100% Of Dodging Incoming Attack)\n")
        if user_input == "1":
            rand_num = random.randrange(1,11) #Uses the random module to generate a random number from 1-10
            if rand_num >= 6:
                strength += 400
        elif user_input == "2":
            dodge += 400
        else:
            print("Wrong Input")
    if character_class == "Cleric":
        print("Choose your special ability!")
        user_input =  input("1) Armor Boost (Temporarily Boost Block) \n2) Health Boost(Temporarily Boost HP)\n")
        if user_input == "1":
            block += (20 + (level * 2))
        elif user_input == "2":
            health += (20 + (level * 2))
        else:
            print("Wrong Input")
    
    return (strength, magic, health, dodge, block) #Returns the temporarily buffed stats

if __name__ == "__main__": #Space to test my function
    print("Welcome Player 1!")
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")