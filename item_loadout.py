import json

class GetItems():
    def __init__(self, name, cost, type, build_type, restrictedRoles, starter, icon):
        self.name = name
        self.cost = cost
        self.type = type
        self.build_type = build_type
        self.restrictedRoles = restrictedRoles
        self.starter = starter
        self.icon = icon
        self.dictionary = {"name":self.name,"cost":self.cost,"type":self.type,"buildType":self.build_type,"restrictedRoles":self.restrictedRoles,"starter":self.starter, "icon":self.icon}
        
        possible_items.append(self.dictionary)
        if self.build_type == "Offensive":
            offensive.append(self.dictionary)
        elif self.build_type == "Defensive":
            defensive.append(self.dictionary)
        else:
            hybrid.append(self.dictionary)
        

def loadout(god):
    with open(r"personal_projects\smite_god_randomizer_2_0\random_items.json") as json_file:
        item_list = json.load(json_file)
    with open(r"personal_projects\smite_god_randomizer_2_0\gods.json") as json_file:
        god_list = json.load(json_file)
    global possible_items
    global offensive
    global defensive
    global hybrid
    possible_items = []
    offensive = []
    defensive = []
    hybrid = []
    gods = god_list["format"]
    for i in range(len(gods)):
        god_dict = gods[i]
        if god == god_dict["name"]:
            power = god_dict["power type"]
            god_class = god_dict["class"]
            for j in range(len(item_list)):
                item_dict = item_list[j]

                item_name = item_dict["name"]
                cost = item_dict["cost"]
                type = item_dict["type"]
                buildType = item_dict["buildType"]
                restrictedRoles = item_dict["restrictedRoles"]
                starter = item_dict["starter"]
                icon = item_dict["icon"]

                if (type == "Both" or type == power) and (god_class.lower() not in restrictedRoles):
                    GetItems(item_name, cost, type, buildType, restrictedRoles, starter, icon)
    return possible_items, offensive, defensive, hybrid
