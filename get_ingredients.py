import re

#imports from other files
from get_parts import parse_ingredient_list

#extract ingredients used in one step

def get_ingredients_in_step(step, ingredient_list):
	print("STEP: ", step)
	ingredients_used = []

	i = 0

	for i in range(0, len(ingredient_list)):
		ingredient = ingredient_list[i]
		print("INGREDIENT: ", ingredient)
		ingred_arr = ingredient.split(" ") #split the ingredient name into a tokenized array eg ['olive', 'oil']
		# print("ingred_arr: ", ingred_arr)
		if len(ingred_arr) == 1:
			ing_re = '\s' + ingred_arr[0] + '\W'
			ingred_search = re.search(ing_re, step)
			if ingred_search:
				ingred_name = ingred_search.group(0).lstrip().rstrip()
				ingredients_used.append(ingred_name)

		else:
			for start in range(0, len(ingred_arr)): #try different phrase start points
				found_ingredient = find_one_ingredient(step, ingred_arr, start)
				if found_ingredient:
					skip = len(found_ingredient.split(' '))
					ingredients_used.append(found_ingredient)
					break #break if we find one.... if we found 'olive oil' we don't need to find 'oil'	

	return ingredients_used

#fuck nested loops
def find_one_ingredient(step, ingred_arr, i):
	for count in range(len(ingred_arr), 1, -1): #try different phrase lengths, starting from longest possible strings
		#eg 'olive oil', 'oil'

		test_arr = ingred_arr[i:i+count]
		test_name = " ".join(test_arr)
		print("test_name: ", test_name)
		ing_re = '\s' + test_name + '\W'
		ingred_search = re.search(ing_re, step)

		if ingred_search:
			ingred_name = ingred_search.group(0).lstrip().rstrip()
			# cprint("found: ", ingred_name)
			return ingred_name
			#stop after we find the longest version, since we prefer 'olive oil' over 'oil'
	return None










if __name__ == "__main__":
	steps = ['Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes. Drain and transfer to a pasta bowl.', 'Combine garlic and olive oil in a cold skillet. Cook over medium heat to slowly toast garlic, about 10 minutes. Reduce heat to medium-low when olive oil begins to bubble. Cook and stir until garlic is golden brown, about another 5 minutes. Remove from heat.', 'Stir red pepper flakes, black pepper, and salt into the pasta. Pour in olive oil and garlic, and sprinkle on Italian parsley and half of the Parmigiano-Reggiano cheese; stir until combined.', 'Serve pasta topped with the remaining Parmigiano-Reggiano cheese.']
	ingredients = ['1 pound uncooked spaghetti', '6 cloves garlic, thinly sliced', '1/2 cup olive oil', '1/4 teaspoon red pepper flakes, or to taste', 'salt and freshly ground black pepper to taste', '1/4 cup chopped fresh Italian parsley', '1 cup finely grated Parmigiano-Reggiano cheese']	
	parsed_ingredients = parse_ingredient_list(ingredients)
	# print("parsed ingredients: ", parsed_ingredients)
	all_ingredients = [item['name'] for item in parsed_ingredients]
	# for step in steps:
	ingredients_in_step = get_ingredients_in_step(steps[2], all_ingredients)
	print(ingredients_in_step)
