from transform_dicts import to_korean_dict
from copy import deepcopy

###
# Transform to korean
#
# @param: steps - list of strings - steps of recipe
#         food_dict - dictionary - keys: string -, values: string - unhealthy/healthy substitute
#         ingredients - list of strings - ingredients list for current recipe
# @return: list of strings - transformed steps
#          list of strings - transformed ingredients list
###
def transform_korean(name, ingredients, directions):
  t_ingredients = []
  new_steps = []

  # transform recipe name
  name_parts = name.split()
  for part in name_parts:
    print (part)
    if part in to_korean_dict.keys():
      name.replace(part, to_korean_dict[part])

  # transform ingredients
  for ingredient in ingredients:
    ingred_name = ingredient['name']
    if ingred_name in to_korean_dict.keys():
      ingredient['name'] = ingredient['name'].replace(ingred_name, to_korean_dict[ingred_name])
  
  # transform steps
  for step in directions:
    print(step)
    new_ingredients = []
    for ingredient in step['ingredients']: 
      if ingredient in to_korean_dict.keys():
        new_ingredients.append(to_korean_dict[ingredient])
        step['original'] = step['original'].replace(ingredient, to_korean_dict[ingredient])
      else:
        new_ingredients.append(ingredient)
    step['ingredients'] = new_ingredients

  return name, ingredients, directions