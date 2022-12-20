import tkinter as tk
from tkinter import *
from tkinterweb import HtmlFrame
from random_pantheon import all_pantheon_list, pan_dic, colours
import random
import json
import item_loadout, random_god

with open(r"personal_projects\smite_god_randomizer_2_0\gods.json", "r") as f:
    data = json.load(f)

with open(r"personal_projects\smite_god_randomizer_2_0\random_items.json") as json_file:
    item_list = json.load(json_file)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

def god_photo(link="personal_projects\\smite_god_randomizer_2_0\\smite_god_images\\achilles_resized.png", name="Achilles"):
        god_image = PhotoImage(file=link) # image creation
        god_image_display = tk.Label(display_window,image = god_image)
        god_image_display.god_image = god_image 
        
        god_text = tk.Label(god_name, text=name) # text creation
        god_text.config(font = ("Penumbra Frame",15) ,padx=5, pady=0, relief = "groove",anchor='center',fg=rgb_hack((215, 183, 0)),bg = rgb_hack((0, 30, 44)))
        god_text.pack() # text display
        god_image_display.pack() # image display

def display(god_image_link, random_god_name):  
    for widget in god_name.winfo_children():
        widget.destroy()
    for widget in display_window.winfo_children():
        widget.destroy()
    god_photo(god_image_link, random_god_name)

def random_god_class(god_dict):
    global god_name_
    god_name_ = god_dict["name"]
    god_img = god_dict["img"]
    display(god_img, god_name_)
    item_image_display(god_name_,"possible_items")

def random_god_create():
    god_dict = random_god.random_god()
    random_god_class(god_dict)

def random_mage_create():
    god_dict = random_god.random_mage()
    random_god_class(god_dict)

def random_warrior_create():
    god_dict = random_god.random_warrior()
    random_god_class(god_dict)

def random_guardian_create():
    god_dict = random_god.random_guardian()
    random_god_class(god_dict)

def random_hunter_create():
    god_dict = random_god.random_hunter()
    random_god_class(god_dict)

def random_assassin_create():
    god_dict = random_god.random_assassin()
    random_god_class(god_dict)

ws = Tk()
ws.title('Smite God Randomizer')
ws.geometry('940x500')
ws.config(bg='black')

img = PhotoImage(file=r"C:\Users\jacob\Documents\escape\escape\images\smite_screen.png")
background = Label(ws, image=img)
background.place(x=-220, y=0)

display_window = tk.Frame(ws,height=180,width=310,bg="black")
display_window.place(x=320, y=180) # (black box, replaced by god image)

god_name = tk.Frame(ws,height=0,width=0)
god_name.place(x=320, y=337)

god_photo()
god_name_ = "Achilles" # GUI loads with image of Achilles, preventing error from calling random build with no god present
# button order = Solo,Jung,Mid,Sup,Car
class ClassButton():
    def __init__(self,frame, class_text, font_col, bg_col,grid_col, grid_row, com):
        self.frame = frame
        self.class_text = class_text
        self.font_col = font_col
        self.bg_col = bg_col
        self.grid_col = grid_col
        self.grid_row = grid_row
        self.com = com
        self.button = Button(self.frame, text=self.class_text, font=('Arial Bold', 16),
                            fg=self.font_col, bg=self.bg_col,width=8,height=1,command=self.com)
        self.button.grid(column=self.grid_col, row=self.grid_row, sticky="ew")

class_frame = Frame(ws, height=100, width=20)
class_frame.place(x=152, y=167)
ClassButton(class_frame,'Mage',rgb_hack((197, 138, 212)), "purple",0,3,random_mage_create)
ClassButton(class_frame,'Warrior',rgb_hack((240, 121, 121)),rgb_hack((160, 39, 39)),0,1,random_warrior_create)
ClassButton(class_frame,'Guardian',rgb_hack((148, 218, 91)),rgb_hack((10, 138, 21)),0,4,random_guardian_create)
ClassButton(class_frame,'Hunter',rgb_hack((229, 174, 128)),rgb_hack((177, 85, 10)),0,5,random_hunter_create)
ClassButton(class_frame,'Assassin',rgb_hack((230, 220, 117)),rgb_hack((150, 139, 16)),0,2,random_assassin_create)

random_frame = Frame(ws, height=30, width=40)
random_frame.place(x=399, y=420)
item_type_frame = Frame(ws, height=20, width=20)
item_type_frame.place(x=630, y=380)

randomize = Button(random_frame,text='Randomize!',font=('Arial Bold', 18),
                    fg="white", bg="green",command=random_god_create)
randomize.grid(column=1,row=0,sticky="ew")



class PantheonButton():
    def __init__(self, frame, pan_text, bg_col, col, row):
        self.frame = frame
        self.pan_text = pan_text
        self.bg_col = bg_col
        self.col = col
        self.row = row
        pantheon_dict = {}
        pantheon_dict[self.pan_text] = self 
        self.pantheon_button = Button(frame, text = self.pan_text, padx=1, 
                                pady=1,  font=('Arial Bold', 8),fg="white", bg=self.bg_col, command = lambda pan_text=pan_text: img_display(pan_text))
        self.pantheon_button.grid(column=grid_col, row=grid_row, sticky="ew")

pantheon_frame = Frame(ws, height=100, width=100)
pantheon_frame.place(x=680, y=170)

class ItemFrame():
    def __init__(self, item_text, item_icon, grid_row, grid_col):
        self.item_text = item_text
        self.item_icon = item_icon
        self.grid_col = grid_col
        self.grid_row = grid_row

        self.item_image_path = PhotoImage(file=self.item_icon)
        self.item = Label(item_frame, image = self.item_image_path)
        self.item.item_image_path = self.item_image_path 
        self.item.grid(column=self.grid_col, row = self.grid_row, sticky="ew")

item_frame = Frame(ws, height=5, width=5)
item_frame.place(x=477, y=387, anchor="center")

def item_image_display(god, buildtype):
    possible_items, offensive, defensive, hybrid = item_loadout.loadout(god) # list of possible items for god
    item_list = [] # final loadout
    t3_items = [] # tier 3 items
    starter_list = [] # starter items
    
    if buildtype=="Offensive":
        items = offensive
        
    elif buildtype=="Defensive":
        items = defensive
        
    elif buildtype=="possible_items":
        items = possible_items
       
    else:
        items = hybrid
        offen = offensive
        defen = defensive
        hybrid_off = []
        hybrid_def = []

    item_range = len(items)
    
    
    for i in range(item_range): # sort items into tier 3 and starter items
        item_dict = items[i]
        item_name = item_dict["name"]
        if item_dict["starter"] == True: 
            starter_list.append(item_dict)
        else:
            t3_items.append(item_name)

    item_list.insert(0,starter_list[random.randrange(len(starter_list))]) # random starter

    if items == hybrid:
        for i in range(len(offen)):
            item_dict = offen[i]
            item_name = item_dict["name"]
            if item_dict["starter"] == False: 
                hybrid_off.append(item_dict)
        item_list.append(hybrid_off[random.randrange(len(hybrid_off))])

        for i in range(len(defen)):
            item_dict = defen[i]
            item_name = item_dict["name"]
            if item_dict["starter"] == False: 
                hybrid_def.append(item_dict)
        item_list.append(hybrid_def[random.randrange(len(hybrid_def))])
        
        for i in range(3): # produces 5 random items, avoiding repetition
            random_index = random.randrange(len(t3_items)-i)
            random_item_= t3_items[random_index]
            for i in range(item_range):
                item_dict = items[i]
                item_name = item_dict["name"]
                if item_name == random_item_:
                    item_list.append(item_dict)
                    t3_items.remove(random_item_)
    else:
        
        for i in range(5): # produces 5 random items, avoiding repetition
            random_index = random.randrange(len(t3_items)-i)
            random_item_= t3_items[random_index]
            for i in range(item_range):
                item_dict = items[i]
                item_name = item_dict["name"]
                if item_name == random_item_:
                    item_list.append(item_dict)
                    t3_items.remove(random_item_)

    for i in range(len(item_list)): # displays item name text
        item_text = item_list[i]
        item_name = item_text["name"]
        with open(r"personal_projects\smite_god_randomizer_2_0\item_image.json") as json_file:
            item_image_dict = json.load(json_file)
        item_image_path = item_image_dict[item_name]
        ItemFrame(item_name,item_image_path, 0, i)

offensive = Button(item_type_frame,text='Offensive',font=('Arial Bold', 12),fg="white",bg=rgb_hack((135,10,9)),command=lambda text = "Offensive": item_image_display(god_name_,text))
offensive.grid(column=0,row=1,sticky="ew")

defensive = Button(item_type_frame,text='Defensive',font=('Arial Bold', 12),fg="white",bg=rgb_hack((10, 138, 21)),command=lambda text = "Defensive": item_image_display(god_name_,text))
defensive.grid(column=0,row=2,sticky="ew")

hybrid = Button(item_type_frame,text='Hybrid',font=('Arial Bold', 12),fg="white",bg=rgb_hack((199,150,2)),command=lambda text = "Hybrid": item_image_display(god_name_,text))
hybrid.grid(column=0,row=3,sticky="ew")

def img_display(pantheon):
    global god_name_
    for widget in god_name.winfo_children():
        widget.destroy()
    for widget in display_window.winfo_children():
        widget.destroy()
    for widget in item_frame.winfo_children():
        widget.destroy()
    god_list = pan_dic[pantheon].pantheon_gods
    god_index = random.randint(0,len(god_list)-1)
    god_name_ = god_list[god_index]

    item_image_display(god_name_,"possible_items")

    with open(r"personal_projects\smite_god_randomizer_2_0\image_file_2.json") as json_file:
        img_dict = json.load(json_file)
    img = img_dict[god_name_]
    god_photo(img, god_name_)

next_in = 0        
for i in range(2):
    grid_col = i
    for j in range(8):
        grid_row = j
        pan_text = all_pantheon_list[j+next_in]
        for i in range(len(colours)):
            colour_dict = colours[i]
            if colour_dict["name"] == pan_text:
                colour = rgb_hack(colour_dict["colour"])
                
        PantheonButton(pantheon_frame, pan_text, colour, grid_col, grid_row)
    next_in += 8

ws.mainloop()