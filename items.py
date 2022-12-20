import json

with open(r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\all_items.json") as json_file:
    item_json = json.load(json_file)
item_list = item_json["items"]

item_tier3_dict = []

class Tier3():
    
    def __init__(self, name, cost, type, build_type, restrictedRoles, starter, icon):
        self.name = name
        self.cost = cost
        self.type = type
        self.build_type = build_type
        self.restrictedRoles = restrictedRoles
        self.starter = starter
        self.icon = icon
        self.dictionary = {"name":self.name,"cost":self.cost,"type":self.type,"buildType":self.build_type,"restrictedRoles":self.restrictedRoles,"starter":self.starter, "icon":self.icon}
        
        item_tier3_dict.append(self.dictionary)

def tier_3(item_dict):
    # have to re-write the dictionary
    for i in range(len(item_dict)):
        item = item_dict[i]
        item_tier = item["tier"]
        if item_tier == 3 or "starter" in item and item_tier == 2:
            item_name = item["name"]
            item_cost = item["cost"]
            item_type = item["type"]
            item_icon = item["icon"]
            if "restrictedRoles" in item:
                restrictedRoles = item["restrictedRoles"]
            else:
                restrictedRoles = "None"
            if "starter" in item:
                starter = item["starter"]
            else:
                starter = False
            if ("physicalPower" in item or "magicalPower" in item)  and ("physicalProtection" in item or "magicalProtection" in item):
                build_type = "Hybrid"
            elif ("physicalPower" in item or "magicalPower" in item) :
                build_type = "Offensive"
            elif("health"in item or "physicalProtection" in item or "magicalProtection" in item):
                build_type = "Defensive"
            else:
                build_type = "Utility"


            Tier3(item_name, item_cost, item_type, build_type, restrictedRoles, starter, item_icon)
            
tier_3(item_list)

with open(r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\random_items.json", "w") as json_file:
    json.dump(item_tier3_dict, json_file, indent='\t')
