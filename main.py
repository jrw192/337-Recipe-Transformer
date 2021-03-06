from parse_html import parse_html
from transform_dicts import to_healthydict,to_unhealthydict, to_vegetariandict
from to_vegetarian import transform_vegetarian
from to_nonvegetarian import transform_nonvegetarian
from to_unhealthy import transform_unhealthy
from to_healthy import transform_healthy
from to_sicilian import transform_siciliancuisine
from transform_korean import transform_korean

from get_parts import parse_ingredient_list
from get_ingredients import get_ingredients_in_step
from get_steptimes import get_steptimes
from get_methods import get_cooking_method
from get_tools import get_tools

# we can have links in main and pass to parser?

  # print('INGREDIENTS: ', parsed_ingredients)
  # print('DIRECTIONS: ', parsed_directions)


  # vegetarian transform test
  # steps, ingredients = transform_vegetarian(recipe_dict, to_vegetarian)

  # healthy transform test
  # steps, ingredients = transform_healthy(recipe_dict, to_healthy)
###
# Runs the body of the program 
#
# @param: string - url to an allrecipes recipe? 
# @return: ?
###
def main():
  # get dictionary of recipe parts 
  #added on for user input
  url = input("Enter the full url for the recipe, then hit enter:\n")
  reiteration(url) #added this function because in class he said the code shouldnt just exit, it should keep asking about transforms until you exit out of it

def reiteration(url): #added this function because in class he said the code shouldnt just exit, it should keep asking about transforms until you exit out of it
  transform_type = input("\nEnter Corresponding Number for Transformation: \n"
    " 0 for Original Recipe \n" " 1 for transformation to healthy \n" " 2 for transformation unhealthy \n" " 3 for transformation to vegetarian \n" 
    " 4 for transformation to non-vegetarian \n" " 5 for transformation to Style of Cuisine: Sicilian Cuisine \n" " 6 for transformation to Style of Cuisine: Korean Cuisine \n" " 7 to enter a url for a different recipe\n" " 8 to Exit \n")
     # 6 for transformation to Style of Cuisine: Indonesian Cuisine
  # display_type = input("Enter 0 to view the full recipe, 1 to view the ingredients list, 2 to view all required tools, 3 to view all methods, 4 to view all steps.\n")
  
  recipe_dict = parse_html(url)
  name = recipe_dict['name']
  ingredients = recipe_dict['ingredients']



  #parse ingredients list
  parsed_ingredients = parse_ingredient_list(ingredients)



  #split directions, steps should be split by sentences NOT the actual steps described in allrecipes
  directions = []
  temp_directions = recipe_dict['directions']
  for direc in temp_directions:
    split_direc = direc.split('. ')
    directions += split_direc


  #get list of all ingredient names
  all_ingredients = [item['name'] for item in parsed_ingredients]

  #parse directions
  parsed_directions = []
  prevtools=[]
  for step in directions:
    parsed_step = {}
    parsed_step['original'] = step
    parsed_step['times'] = get_steptimes(step)
    parsed_step['method'] = get_cooking_method(step)
    parsed_step['ingredients'] = get_ingredients_in_step(step, all_ingredients)
    parsed_step['tools'], prevtools = get_tools(step, prevtools)


    parsed_directions.append(parsed_step)
  
  # print('parsed directions: ' , parsed_directions)
  # print('parsed ingredients: ', parsed_ingredients)

  #original recipe
  if transform_type == "0":
    readable = readable_recipe(name, parsed_ingredients, parsed_directions)
    for item in readable:
      print(item)
    reiteration(url)

  #transform to healthy
  elif transform_type == "1":
    recipe_name,p_ingredients, p_directions = transform_healthy(name,parsed_ingredients,parsed_directions)
    readable = readable_recipe(recipe_name, p_ingredients, p_directions)
    for item in readable:
      print(item)
    reiteration(url)

  #transform to unhealthy
  elif transform_type == "2":
    recipe_names,p_ingredient, p_direction = transform_unhealthy(name,parsed_ingredients,parsed_directions)
    readable = readable_recipe(recipe_names, p_ingredient, p_direction)
    for item in readable:
      print(item)
    reiteration(url)

  #transform to vegetarian
  elif transform_type =="3":
    recipe_names,p_ingredient, p_direction = transform_vegetarian(name,parsed_ingredients,parsed_directions)
    readable = readable_recipe(recipe_names, p_ingredient, p_direction)
    for item in readable:
      print(item)
    reiteration(url)

  #transform to non-vegetarian
  elif transform_type =="4":
    recipe_names,p_ingredient, p_direction = transform_nonvegetarian(name,parsed_ingredients,parsed_directions)
    readable = readable_recipe(recipe_names, p_ingredient, p_direction)
    for item in readable:
      print(item)
    reiteration(url)


  #transform to Sicilian Cuisine
  elif transform_type == "5":
    recipe_names,p_ingredient, p_direction = transform_siciliancuisine(name,parsed_ingredients,parsed_directions)
    readable = readable_recipe(recipe_names, p_ingredient, p_direction)
    print('\nSicilian Style Cuisine:')
    for item in readable:
      print(item)
    reiteration(url)

  #transform to Korean Cuisine
  elif transform_type == "6":
    recipe_names,p_ingredient, p_direction = transform_korean(name,parsed_ingredients,parsed_directions)
    readable = readable_recipe(recipe_names, p_ingredient, p_direction)
    print('\nKorean Style Cuisine:')
    for item in readable:
      print(item)
    reiteration(url)

  elif transform_type == "7":
    main()

  #exit out of the code
  elif transform_type == '8':
    print("Now exiting...")



def readable_recipe(name, ingredients, steps):
  output = ['\nRecipe Name: ' + name + '\n' +'\nIngredients:\n', ]
  count=0
  for ingredient in ingredients:
    count+=1
    ing_name = 'Ingredient ' +str(count) + ': ' + ingredient['name']
    ing_quant = 'Quantity: ' + str(ingredient['quantity'])
    ing_meas = 'Measure: ' + str(ingredient['measurement'])
    ing_prep = 'Preparation: ' + str(ingredient['preparation'])
    ingred_arr = [ing_name, ing_quant, ing_meas, ing_prep]
    output.append('. '.join(ingred_arr))
    
  output.append('\nDirections:')

  for i in range(0, len(steps)):
    step = steps[i]
    step_num = '\nStep ' + str(i) + ':'
    step_og = step['original']


    step_time = 'Time: '
    step_ingred = 'Ingredients: '
    step_method = 'Method: '
    step_tools = 'Tools: '

    if len(step['times']) > 0:
      step_time += ', or '.join(step['times'])
    else:
      step_time += 'N/A'

    if step['method'] == '':
      step_method += 'N/A'
    else:
      step_method += step['method']

    if len(step['ingredients']) > 0:
      step_ingred += ', '.join(step['ingredients'])
    else:
      step_ingred += 'N/A'

    # If there are no tools, step['tools'] = [[]], so old code didn't work
    if len(step['tools']) == 0:
      step_tools += 'N/A'
    elif step['tools'][0] == []:
      step_tools += 'N/A'
    else:
      step_tools += ', '.join(step['tools'])


    step_arr = [step_method, step_ingred, step_tools, step_time]
    output.append(step_num)
    output.append(step_og)
    output.append('. '.join(step_arr))


  return output






if __name__ == '__main__':
  test_urls = ['https://www.allrecipes.com/recipe/223016/fresh-blueberry-cake/?internalSource=staff%20pick&referringId=17263&referringContentType=Recipe%20Hub', # cake
                'https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%203', # aglio e olio
                'https://www.allrecipes.com/recipe/230818/pork-fried-rice/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202'] # fried rice
  main()





