import json
import random

with open(r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\gods.json", "r") as f:
    data = json.load(f)
with open(r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\image_file_2.json") as json_file:
    god_images = json.load(json_file)
all_gods = data["format"]

def god_class(god_class):
    """
    Creates a list of gods with the matching class called in the function.

    Takes the class name as an argument 'god_class' and parses through a json file
    of the gods, if the gods class matches 'god_class' the name of that god will be
    added to a list called 'god_class_list'.

    INPUTS
    ------

        god_class - String, The name of the class assigned to a god, can either be 
                    'Mage', 'Assassin', 'Hunter', 'Guardian' or 'Warrior'.

    OUTPUTS
    -------

        god_class_list - List, A list of gods names with classes matching the input.

    """
    god_class_list = []
    for i in range(len(all_gods)):
        god_dict = all_gods[i]
        if god_dict["class"] == god_class:
            god_class_list.append(god_dict["name"])
    return god_class_list

def random_god():
    """
    Selects a random god from all of the possible gods and returns the name
    and image link.

    A random number is generated using the length of the 'all_gods' list
    which is then used to index the 'all_gods' list to select a single value. 
    This value will be a dictionary.

    The dictionary conatins information abouta single god. The name of the god is accessed
    and saved as 'random_god'.

    A new dictionary is then created with the name of the god used as a key and its image link
    used as the value. This is found by using the 'name' of the god to acccess the corresponding image link 
    saved in 'image_file_2.json'.

    OUTPUTS
    -------

        god_dict - Dictionary, A dictionary containing a string key and strign value, the key being the
                    name of the god, and the value being the image directory.

    """
    random_god_dict = all_gods[random.randrange(len(all_gods))]
    random_god = random_god_dict["name"]
    god_dict = {}
    god_dict["name"] = random_god 
    god_dict["img"] = god_images[random_god]
    return god_dict

def random_warrior():
    """
    Selects a random god from the a list of 'Warrior' gods.

    Runs the 'god_class' function with 'Warrior' as the argument,
    returning a list of Warrior gods. The list is indexed using a 
    random number from 0 to the length of the list.

    A new dictionary is created as 'god_dict'.
    The name of the god is used as the key and the image directory is
    used as the value. This is found by using the 'name' of the god to 
    acccess the corresponding image link saved in 'image_file_2.json'.
    
    OUTPUTS
    -------

        god_dict - Dictionary, A dictionary containing a string key and strign value, the key being the
                    name of the god, and the value being the image directory.
    
    """
    warrior_gods = god_class("Warrior")
    random_warrior = warrior_gods[random.randrange(len(warrior_gods))]
    god_dict = {}
    god_dict["name"] = random_warrior
    god_dict["img"] = god_images[random_warrior]
    return god_dict

def random_guardian():
    """
    Selects a random god from the a list of 'Guardian' gods.

    Runs the 'god_class' function with 'Guardian' as the argument,
    returning a list of Guardian gods. The list is indexed using a 
    random number from 0 to the length of the list.

    A new dictionary is created as 'god_dict'.
    The name of the god is used as the key and the image directory is
    used as the value. This is found by using the 'name' of the god to 
    acccess the corresponding image link saved in 'image_file_2.json'.
    
    OUTPUTS
    -------

        god_dict - Dictionary, A dictionary containing a string key and strign value, the key being the
                    name of the god, and the value being the image directory.
    
    """
    guardian_gods = god_class("Guardian")
    random_guardian = guardian_gods[random.randrange(len(guardian_gods))]
    god_dict = {}
    god_dict["name"] = random_guardian
    god_dict["img"] = god_images[random_guardian]
    return god_dict

def random_hunter():
    """
    Selects a random god from the a list of 'Hunter' gods.

    Runs the 'god_class' function with 'Hunter' as the argument,
    returning a list of Hunter gods. The list is indexed using a 
    random number from 0 to the length of the list.

    A new dictionary is created as 'god_dict'.
    The name of the god is used as the key and the image directory is
    used as the value. This is found by using the 'name' of the god to 
    acccess the corresponding image link saved in 'image_file_2.json'.
    
    OUTPUTS
    -------

        god_dict - Dictionary, A dictionary containing a string key and strign value, the key being the
                    name of the god, and the value being the image directory.
    
    """
    hunter_gods = god_class("Hunter")
    random_hunter = hunter_gods[random.randrange(len(hunter_gods))]
    god_dict = {}
    god_dict["name"] = random_hunter
    god_dict["img"] = god_images[random_hunter]
    return god_dict

def random_assassin():
    """
    Selects a random god from the a list of 'Assassin' gods.

    Runs the 'god_class' function with 'Assassin' as the argument,
    returning a list of Assassin gods. The list is indexed using a 
    random number from 0 to the length of the list.

    A new dictionary is created as 'god_dict'.
    The name of the god is used as the key and the image directory is
    used as the value. This is found by using the 'name' of the god to 
    acccess the corresponding image link saved in 'image_file_2.json'.
    
    OUTPUTS
    -------

        god_dict - Dictionary, A dictionary containing a string key and strign value, the key being the
                    name of the god, and the value being the image directory.
    
    """
    assassin_gods = god_class("Assassin")
    random_assassin = assassin_gods[random.randrange(len(assassin_gods))]
    god_dict = {}
    god_dict["name"] = random_assassin
    god_dict["img"] = god_images[random_assassin]
    return god_dict

def random_mage():
    """
    Selects a random god from the a list of 'Mage' gods.

    Runs the 'god_class' function with 'Mage' as the argument,
    returning a list of Mage gods. The list is indexed using a 
    random number from 0 to the length of the list.

    A new dictionary is created as 'god_dict'.
    The name of the god is used as the key and the image directory is
    used as the value. This is found by using the 'name' of the god to 
    acccess the corresponding image link saved in 'image_file_2.json'.
    
    OUTPUTS
    -------

        god_dict - Dictionary, A dictionary containing a string key and strign value, the key being the
                    name of the god, and the value being the image directory.
    
    """
    mage_gods = god_class("Mage")
    random_mage = mage_gods[random.randrange(len(mage_gods))]
    god_dict = {}
    god_dict["name"] = random_mage
    god_dict["img"] = god_images[random_mage]
    return god_dict
