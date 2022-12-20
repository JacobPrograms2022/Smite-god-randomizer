item_image_dict = {}
def image_resize():
    import cv2
    import numpy as np
    import requests
    import json

    with open(r"personal_projects\smite_god_randomizer_2_0\random_items.json") as json_file:
        all_items = json.load(json_file)
    
    for i in range(len(all_items)):
        item_dict = all_items[i]
        item_name = item_dict["name"]
        print(item_name)
        item_icon = item_dict["icon"]

        img = requests.get(item_icon)
        directory = r"personal_projects\smite_god_randomizer_2_0\item_images"+"\{}.png".format(item_name)
        with open(directory, "wb") as file:
            file.write(img.content)

        img = cv2.imread(directory)
        res = cv2.resize(img, dsize=(44, 44), interpolation=cv2.INTER_CUBIC)

        cv2.imwrite(directory, res)
        item_image_dict[item_name] = directory
        with open(r"personal_projects\smite_god_randomizer_2_0\item_image.json", "w") as json_file:
            json.dump(item_image_dict, json_file, indent='\t')
image_resize()
