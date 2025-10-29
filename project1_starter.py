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
