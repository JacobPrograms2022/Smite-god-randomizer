import json
import random

with open(r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\gods.json", "r") as f:
    data = json.load(f)
with open(r"personal_projects\smite_god_randomizer_2_0\image_file_2.json") as json_file:
    god_images = json.load(json_file)
all_gods = data["format"]

def god_class(god_class):
    god_class_list = []
    for i in range(len(all_gods)):
        god_dict = all_gods[i]
        if god_dict["class"] == god_class:
            god_class_list.append(god_dict["name"])
    return god_class_list

def random_god():
    random_god_dict = all_gods[random.randrange(len(all_gods))]
    random_god = random_god_dict["name"]
    god_dict = {}
    god_dict["name"] = random_god 
    god_dict["img"] = god_images[random_god]
    return god_dict

def random_warrior():
    warrior_gods = god_class("Warrior")
    random_warrior = warrior_gods[random.randrange(len(warrior_gods))]
    god_dict = {}
    god_dict["name"] = random_warrior
    god_dict["img"] = god_images[random_warrior]
    return god_dict

def random_guardian():
    guardian_gods = god_class("Guardian")
    random_guardian = guardian_gods[random.randrange(len(guardian_gods))]
    god_dict = {}
    god_dict["name"] = random_guardian
    god_dict["img"] = god_images[random_guardian]
    return god_dict

def random_hunter():
    hunter_gods = god_class("Hunter")
    random_hunter = hunter_gods[random.randrange(len(hunter_gods))]
    god_dict = {}
    god_dict["name"] = random_hunter
    god_dict["img"] = god_images[random_hunter]
    return god_dict

def random_assassin():
    assassin_gods = god_class("Assassin")
    random_assassin = assassin_gods[random.randrange(len(assassin_gods))]
    god_dict = {}
    god_dict["name"] = random_assassin
    god_dict["img"] = god_images[random_assassin]
    return god_dict

def random_mage():
    mage_gods = god_class("Mage")
    random_mage = mage_gods[random.randrange(len(mage_gods))]
    god_dict = {}
    god_dict["name"] = random_mage
    god_dict["img"] = god_images[random_mage]
    return god_dict