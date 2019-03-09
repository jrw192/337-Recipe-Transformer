import re

#imports from other files
from get_parts import parse_ingredient_list

#extract ingredients used in one step

def get_ingredients_in_step(step, ingredient_list):
	# print("STEP: ", step)
	ingredients_used = []

	i = 0

	for i in range(0, len(ingredient_list)):
		ingredient = ingredient_list[i]
		# print("INGREDIENT: ", ingredient)
		ingred_arr = ingredient.split(" ") #split the ingredient name into a tokenized array eg ['olive', 'oil']
		# print("ingred_arr: ", ingred_arr)
		if len(ingred_arr) == 1:
			ing_re = '\s' + ingred_arr[0] + '[\s.,]'
			ingred_search = re.search(ing_re, step)
			if ingred_search:
				ingred_name = ingred_search.group(0).lstrip().rstrip()
				ingredients_used.append(ingred_name)

		else:
			for start in range(0, len(ingred_arr)): #try different phrase start points
				found_ingredient = find_one_ingredient(step, ingred_arr, start)
				if found_ingredient:
					# skip = len(found_ingredient.split(' '))
					# ingredients_used.append(found_ingredient)
					skip = len(ingredient)
					if ingredient not in ingredients_used:
						ingredients_used.append(ingredient)
					break #break if we find one.... if we found 'olive oil' we don't need to find 'oil'	
	# print("ingredients used: ", ingredients_used)
	return ingredients_used

#fuck nested loops
def find_one_ingredient(step, ingred_arr, i):
	for count in range(len(ingred_arr), 1, -1): #try different phrase lengths, starting from longest possible strings
		#eg 'olive oil', 'oil'

		test_arr = ingred_arr[i:i+count]
		test_name = " ".join(test_arr)
		# print("test_name: ", test_name)
		ing_re = '\s' + test_name + '\W'
		ingred_search = re.search(ing_re, step)

		if ingred_search:
			ingred_name = ingred_search.group(0).lstrip().rstrip()
			# cprint("found: ", ingred_name)
			return ingred_name
			#stop after we find the longest version, since we prefer 'olive oil' over 'oil'
	return None










if __name__ == "__main__":
	steps = ['Preheat an oven to 450 degrees F (230 degrees C).', 'Place chicken breasts between two sheets of heavy plastic (resealable freezer bags work well) on a solid, level surface. Firmly pound chicken with the smooth side of a meat mallet to a thickness of 1/2-inch. Season chicken thoroughly with salt and pepper.', 'Beat eggs in a shallow bowl and set aside.', 'Mix bread crumbs and 1/2 cup Parmesan cheese in a separate bowl, set aside.', 'Place flour in a sifter or strainer; sprinkle over chicken breasts, evenly coating both sides.', 'Dip flour coated chicken breast in beaten eggs. Transfer breast to breadcrumb mixture, pressing the crumbs into both sides. Repeat for each breast. Set aside breaded chicken breasts for about 15 minutes.', 'Heat 1 cup olive oil in a large skillet on medium-high heat until it begins to shimmer. Cook chicken until golden, about 2 minutes on each side. The chicken will finish cooking in the oven.', 'Place chicken in a baking dish and top each breast with about 1/3 cup of tomato sauce. Layer each chicken breast with equal amounts of mozzarella cheese, fresh basil, and provolone cheese. Sprinkle 1 to 2 tablespoons of Parmesan cheese on top and drizzle with 1 tablespoon olive oil.', 'Bake in the preheated oven until cheese is browned and bubbly, and chicken breasts are no longer pink in the center, 15 to 20 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C).']
	ingredients = ['4 skinless, boneless chicken breast halves', 'salt and freshly ground black pepper to taste', '2 eggs', '1 cup panko bread crumbs, or more as needed', '1/2 cup grated Parmesan cheese', '2 tablespoons all-purpose flour, or more if needed', '1 cup olive oil for frying', '1/2 cup prepared tomato sauce', '1/4 cup fresh mozzarella, cut into small cubes', '1/4 cup chopped fresh basil', '1/2 cup grated provolone cheese', '1/4 cup grated Parmesan cheese', '1 tablespoon olive oil']
	parsed_ingredients = parse_ingredient_list(ingredients)
	print("parsed ingredients: ", parsed_ingredients)
	all_ingredients = [item['name'] for item in parsed_ingredients]
	print("all ingredients")
	for step in steps:
		print('step: ', step)
		ingredients_in_step = get_ingredients_in_step(step, all_ingredients)
		print(ingredients_in_step)
