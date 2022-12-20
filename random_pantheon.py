import json

with open(r"personal_projects\smite_god_randomizer_2_0\image_file_2.json", "r") as json_file:
    god_images = json.load(json_file)
with open(r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\gods.json", "r") as f:
    data = json.load(f)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

pantheon_dictionary = {}
def gods_by_pantheon(input):
    data_format = input["format"]
    all_pantheon_list = [];hindu_gods_list = [];babylonian_gods_list = []
    chinese_gods_list = [];roman_gods_list = [];celtic_gods_list = []
    norse_gods_list = [];greek_gods_list = [];voodoo_gods_list = []
    maya_gods_list = [];slavic_gods_list = [];egyptian_gods_list = []
    yoruba_gods_list = [];japanese_gods_list = [];great_old_ones_gods_list = []
    polynesian_gods_list = [];arthurian_gods_list = []
    
    for i in range(len(data_format)):
        god_dict = data_format[i]
        god_name = god_dict["name"]
        pantheon = god_dict["pantheon"]
        all_pantheon_list.append(pantheon)
        all_pantheon_list = set(all_pantheon_list)
        all_pantheon_list = list(all_pantheon_list)

        if god_dict["pantheon"] == "Hindu":
            hindu_gods_list.append(god_name)
            pantheon_dictionary["Hindu"] = hindu_gods_list
        elif god_dict["pantheon"] == "Babylonian":
            babylonian_gods_list.append(god_name)
            pantheon_dictionary["Babylonian"] = babylonian_gods_list
        elif god_dict["pantheon"] == "Chinese":
            chinese_gods_list.append(god_name)
            pantheon_dictionary["Chinese"] = chinese_gods_list
        elif god_dict["pantheon"] == "Roman":
            roman_gods_list.append(god_name)
            pantheon_dictionary["Roman"] = roman_gods_list
        elif god_dict["pantheon"] == "Celtic":
            celtic_gods_list.append(god_name)
            pantheon_dictionary["Celtic"] = celtic_gods_list
        elif god_dict["pantheon"] == "Norse":
            norse_gods_list.append(god_name)
            pantheon_dictionary["Norse"] = norse_gods_list
        elif god_dict["pantheon"] == "Greek":
            greek_gods_list.append(god_name)
            pantheon_dictionary["Greek"] = greek_gods_list
        elif god_dict["pantheon"] == "Voodoo":
            voodoo_gods_list.append(god_name)
            pantheon_dictionary["Voodoo"] = voodoo_gods_list
        elif god_dict["pantheon"] == "Maya":
            maya_gods_list.append(god_name)
            pantheon_dictionary["Maya"] = maya_gods_list
        elif god_dict["pantheon"] == "Slavic":
            slavic_gods_list.append(god_name)
            pantheon_dictionary["Slavic"] = slavic_gods_list
        elif god_dict["pantheon"] == "Egyptian":
            egyptian_gods_list.append(god_name)
            pantheon_dictionary["Egyptian"] = egyptian_gods_list
        elif god_dict["pantheon"] == "Yoruba":
            yoruba_gods_list.append(god_name)
            pantheon_dictionary["Yoruba"] = yoruba_gods_list
        elif god_dict["pantheon"] == "Japanese":
            japanese_gods_list.append(god_name)
            pantheon_dictionary["Japanese"] = japanese_gods_list 
        elif god_dict["pantheon"] == "Great Old Ones":
            great_old_ones_gods_list.append(god_name)
            pantheon_dictionary["Great Old Ones"] = great_old_ones_gods_list
        elif god_dict["pantheon"] == "Polynesian":
            polynesian_gods_list.append(god_name)
            pantheon_dictionary["Polynesian"] = polynesian_gods_list
        else:
            arthurian_gods_list.append(god_name)
            pantheon_dictionary["Arthurian"] = arthurian_gods_list

        
    return all_pantheon_list,hindu_gods_list,babylonian_gods_list,chinese_gods_list,roman_gods_list,celtic_gods_list,norse_gods_list,greek_gods_list,voodoo_gods_list,maya_gods_list,slavic_gods_list,egyptian_gods_list,yoruba_gods_list,japanese_gods_list,great_old_ones_gods_list,polynesian_gods_list,arthurian_gods_list

pantheon_list = list(gods_by_pantheon(data))

all_pantheon_list = pantheon_list[0]
del pantheon_list[0]

pan_dic = {}
class PantheonFunction():
    def __init__(self, pantheon_text, pantheon_gods, pantheon_colour):
        self.pantheon_text = pantheon_text
        self.pantheon_gods = pantheon_gods
        self.pantheon_colour = pantheon_colour
        
        pan_dic[self.pantheon_text] = self

for i in range(len(all_pantheon_list)):
    pantheon_name = all_pantheon_list[i]
    god_list = pantheon_dictionary[pantheon_name]
    PantheonFunction(all_pantheon_list[i], god_list, "red")

colours = [{"name":"Hindu",
"colour":(202,99,97)},
{"name":"Arthurian",
"colour":(137,31,30)},
{"name":"Egyptian",
"colour":(61,12,11)},
{"name":"Japanese",
"colour":(135,10,9)},
{"name":"Polynesian",
"colour":(194,61,0)},
{"name":"Babylonian",
"colour":(81,137,163)},
{"name":"Celtic",
"colour":(34,72,15)},
{"name":"Chinese",
"colour":(192,183,32)},
{"name":"Maya",
"colour":(199,150,2)},
{"name":"Roman",
"colour":(145,109,0)},
{"name":"Slavic",
"colour":(219,188,0)},
{"name":"Great Old Ones",
"colour":(38,23,71)},
{"name":"Greek",
"colour":(51,18,123)},
{"name":"Voodoo",
"colour":(121,67,237)},
{"name":"Norse",
"colour":(166,166,166)},
{"name":"Yoruba",
"colour":(216,216,98)}]