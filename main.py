from parse_html import parse_html
from transform_healthy import transform_healthy
from transform_vegetarian import transform_vegetarian
# from transform_dicts import to_healthy, to_vegetarian

from get_parts import parse_ingredient_list
from get_ingredients import get_ingredients_in_step
from get_steptimes import get_steptimes
from get_methods import get_cooking_method
from get_tools import get_tools

# we can have links in main and pass to parser?

###
# Runs the body of the program 
#
# @param: string - url to an allrecipes recipe? 
# @return: ?
###
def main():
  # get dictionary of recipe parts 
  recipe_dict = parse_html()
  name = recipe_dict['name']
  ingredients = recipe_dict['ingredients']
  directions = recipe_dict['directions']

  
  # parse each section and print

  #parse ingredients list
  parsed_ingredients = parse_ingredient_list(ingredients)
  # print(parsed_ingredients)

  #get list of all ingredient names
  all_ingredients = [item['name'] for item in parsed_ingredients]

  #parse directions
  parsed_directions = []
  for step in directions:
    parsed_step = []
    parsed_step['times'] = get_steptimes(step)
    parsed_step['method'] = get_methods(step)
    parsed_step['ingredients'] = get_ingredients_in_step(step, all_ingredients)
    parsed_directions.append(parsed_step)
  print(parsed_directions)





  # vegetarian transform test
  # steps, ingredients = transform_vegetarian(recipe_dict, to_vegetarian)

  # healthy transform test
  # steps, ingredients = transform_healthy(recipe_dict, to_healthy)

  # print (readable_recipe(ingredients, steps))



def readable_recipe(ingredients, steps):
  output = 'Ingredients:\n'
  for ingredient in ingredients:
    output += '\t- ' + ingredient + '\n'
    
  output += '\nDirections:\n'

  for step in steps:
    output += step + '\n\n'
  return output





if __name__ == '__main__':
  test_urls = ['https://www.allrecipes.com/recipe/223016/fresh-blueberry-cake/?internalSource=staff%20pick&referringId=17263&referringContentType=Recipe%20Hub', # cake
                'https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%203', # aglio e olio
                'https://www.allrecipes.com/recipe/230818/pork-fried-rice/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202'] # fried rice
  main()