"""
COMP 163 - Project 1: Character Creator & Saving/Loading
name: Cameron Love
Date: October 29th, 2025

AI Usage: AI helped walk me through how I can change my code to only accept valid classes. As well as helped me parse the data in the load character function
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