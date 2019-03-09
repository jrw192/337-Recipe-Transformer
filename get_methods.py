import re

#read in some lists
with open("methods.txt", "r") as m_f:
	known_methods = m_f.read().splitlines()
m_f.close()

with open("measures.txt", "r") as m_f:
	known_measures = m_f.read().splitlines()
m_f.close()


# Primary cooking method (e.g. sauté, broil, boil, poach, etc.)
# (optional) Other cooking methods used (e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.)
#takes in a step in the recipe, and returns the primary cooking method for the step
def get_cooking_method(step):
	# print(step)

	methods = []
	for method in known_methods:
		method_re = '\A' + method + '\s|\s' + method + '\s'
		method_search = re.search(method_re, step.lower())
		if method_search:
			found_method = method_search.group(0).lstrip().rstrip()
			methods.append(found_method)

	# print('methods: ', methods)
	primary_method = ''
	if len(methods) > 0:
		primary_method = methods[0]

	return primary_method


if __name__ == "__main__":
	# ingredients = ['1 pound uncooked spaghetti', '6 cloves garlic, thinly sliced', '1/2 cup olive oil', '1/4 teaspoon red pepper flakes, or to taste', 'salt and freshly ground black pepper to taste', '1/4 cup chopped fresh Italian parsley', '1 cup finely grated Parmigiano-Reggiano cheese']
	# steps = ['Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes. Drain and transfer to a pasta bowl.', 'Combine garlic and olive oil in a cold skillet. Cook over medium heat to slowly toast garlic, about 10 minutes. Reduce heat to medium-low when olive oil begins to bubble. Cook and stir until garlic is golden brown, about another 5 minutes. Remove from heat.', 'Stir red pepper flakes, black pepper, and salt into the pasta. Pour in olive oil and garlic, and sprinkle on Italian parsley and half of the Parmigiano-Reggiano cheese; stir until combined.', 'Serve pasta topped with the remaining Parmigiano-Reggiano cheese.']
	steps = ['Preheat oven to 350 degrees F (175 degrees C)', 'Grease an 8x8-inch pan.', 'Sift flour, baking powder, sugar, and salt together in a large bowl', 'Beat shortening in a separate bowl until creamy; stir into flour mixture, alternating with milk', 'Beat flour-shortening mixture until mixed, about 2 minutes', 'Add egg and beat until mixed, about 1 minute.', 'Combine lemon zest with blueberries in a bowl; fold into batter', 'Pour batter into prepared pan.', 'Bake in the preheated oven until a toothpick inserted in the center comes out clean, about 50 minutes.']
	# parse_ingredient_list(ingredients)

	for step in steps:
		get_cooking_method(step)