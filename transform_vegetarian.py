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
def transform_vegetarian(steps, food_dict, ingredients):
  t_ingredients = []

  # transform ingredients
  for ingredient in ingredients:
    ingred_name = parse_one_ingredient(ingredient)[0]
    ingredient.replace(ingred_name, food_dict[ingred_name])
    t_ingredients.append(food_dict[ingred_name])

  # transform steps
  for step in steps:
    for ingredient in t_ingredients:
      if ingredient in step:
        step.replace(ingredient, food_dict[ingredient])
    