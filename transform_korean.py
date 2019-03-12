from transform_dicts import to_korean_dict

###
# Transform to korean
#
# @param: steps - list of strings - steps of recipe
#         ingredients - list of dictionaries
#         directions - list of dictionaries 
# @return: string - name of recipe
#          list of strings - transformed steps
#          list of strings - transformed ingredients list
###
def transform_korean(name, ingredients, directions):
  # transform recipe name
  name_parts = name.split()
  for part in name_parts:
    if part in to_korean_dict.keys():
      name.replace(part, to_korean_dict[part])

  # transform ingredients
  for ingredient in ingredients:
    ingred_name = ingredient['name']
    ingreds = ingred_name.split()
    for ingred in ingreds:
      if ingred in to_korean_dict.keys():
        ingredient['name'] = ingredient['name'].replace(ingred, to_korean_dict[ingred])
  
  # transform steps
  for step in directions:
    flag = False
    new_ingredients = []
    for ingredient in step['ingredients']:
      ingreds = ingredient.split()
      for ingred in ingreds:
        if ingred in to_korean_dict.keys():
          step['original'] = step['original'].replace(ingred, to_korean_dict[ingred])
          new_ingredients.append(ingredient.replace(ingred, to_korean_dict[ingred]))
          flag = True
      if not flag:
        new_ingredients.append(ingredient)

    step['ingredients'] = new_ingredients

  # add garnishing step
  new_step = {}
  new_step['original'] = 'Garnish with green onions and ground sesame seeds'
  new_step['method'] = 'garnish'
  new_step['times'] = ''
  new_step['ingredients'] = ['green onions', 'sesame seeds']
  new_step['tools'] = []

  green_onion = {'name': 'green onion', 'quantity':'1', 'measurement': '', 'preparation': 'chopped'}
  sesame_seeds = {'name': 'sesame seeds', 'quantity':'1', 'measurement': 'teaspoon', 'preparation': 'ground'}

  ingredients.append(green_onion)
  ingredients.append(sesame_seeds)

  if 'serve' in directions[-1]['original']:
    directions.insert(new_step, len(directions)-2)
  else:
    directions.append(new_step)

    #Ingredient 2: poppyseed hot dog bun. Quantity: 1. Measure: . Preparation: 

  return name, ingredients, directions