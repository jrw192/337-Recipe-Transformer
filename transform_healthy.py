from get_parts import parse_one_ingredient

###
# Transform ingredients to and from healthy
#
# @param: steps - list of strings - steps of recipe
#         food_dict - dictionary - keys: string - healthy/unhealty, values: string - unhealthy/healthy substitute
#         ingredients - list of strings - ingredients list for current recipe
# @return: list of strings - transformed steps
#          list of strings - transformed ingredients list
###
def transform_healthy(recipe_dict, food_dict):
  print("Transforming " + recipe_dict['name'] + " to a healthy version...\n")

  t_ingredients = []
  new_ingredients = []
  new_steps = []

  # transform recipe name

  # transform ingredients
  for ingredient in recipe_dict['ingredients']:
    ingred_name = parse_one_ingredient(ingredient)[0]
    if ingred_name in food_dict.keys():
      new_ingredients.append(ingredient.replace(ingred_name, food_dict[ingred_name]))
      t_ingredients.append(ingred_name)
    else:
      new_ingredients.append(ingredient)
  
  # transform steps
  for step in recipe_dict['directions']:
    for ingredient in t_ingredients: # change t_ingredients later to finding ingredients within step
      if ingredient in step and ingredient in food_dict.keys():
        step = step.replace(ingredient, food_dict[ingredient])
    new_steps.append(step)

  return new_steps, new_ingredients
    




  