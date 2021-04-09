user_favorites=[
    {"fav_planet_id":['3','7','8']},
    {'fav_character_id':['4','10']}
    
]
all_fav=[{'id': 1, 'user_id': 1, 'fav_planet_id': 1, 'fav_character_id': None},
 {'id': 2, 'user_id': 1, 'fav_planet_id': 6, 'fav_character_id': None}, 
 {'id': 3, 'user_id': 1, 'fav_planet_id': 7, 'fav_character_id': None},
  {'id': 4, 'user_id': 1, 'fav_planet_id': 8, 'fav_character_id': None},
   {'id': 5, 'user_id': 1, 'fav_planet_id': 3, 'fav_character_id': None},
   {'id': 5, 'user_id': 1, 'fav_planet_id': 3, 'fav_character_id': None},
    {'id': 14, 'user_id': 1, 'fav_planet_id': None, 'fav_character_id': 10}, 
    {'id': 15, 'user_id': 1, 'fav_planet_id': None, 'fav_character_id': 4}, 
    {'id': 16, 'user_id': 1, 'fav_planet_id': None, 'fav_character_id': 6}
   ]
all_fav_planets=set() #### planetas ya existentes en los favoritos de la base de datos
all_fav_characters=set() #### personajes ya existentes en los favoritos de la base de datos
for item in all_fav:
    if item['fav_planet_id'] is not None:
        all_fav_planets.add(item['fav_planet_id'])
    elif item['fav_character_id'] is not None:
        all_fav_characters.add(item['fav_character_id'])

########################################################################

new_fav_planets=set()  ## planetas provenientes en la solicitudpara ser añadidos
new_fav_characters=set() ## persojes provenientes en la solicitud para ser añadidos
for each_item in user_favorites:
    for key in each_item:
        if key =='fav_planet_id':
            new_fav_planets=set(each_item['fav_planet_id'])
        elif key == 'fav_character_id':
            new_fav_characters=set(each_item['fav_character_id'])

for ids in all_fav_planets:
    resultado=ids in new_fav_planets
    print(resultado)
        
##################################################################################

print(all_fav_planets)
print(new_fav_planets)
print('####################################################')
print(all_fav_characters)
print(new_fav_characters)

#
#
