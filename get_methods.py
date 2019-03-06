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
	print(step)

	methods = []
	for method in known_methods:
		if method in step.lower():
			methods.append(method)

	print(methods)
	primary_method = methods[0]

	return primary_method


if __name__ == "__main__":
	ingredients = ['1 pound uncooked spaghetti', '6 cloves garlic, thinly sliced', '1/2 cup olive oil', '1/4 teaspoon red pepper flakes, or to taste', 'salt and freshly ground black pepper to taste', '1/4 cup chopped fresh Italian parsley', '1 cup finely grated Parmigiano-Reggiano cheese']
	steps = ['Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes. Drain and transfer to a pasta bowl.', 'Combine garlic and olive oil in a cold skillet. Cook over medium heat to slowly toast garlic, about 10 minutes. Reduce heat to medium-low when olive oil begins to bubble. Cook and stir until garlic is golden brown, about another 5 minutes. Remove from heat.', 'Stir red pepper flakes, black pepper, and salt into the pasta. Pour in olive oil and garlic, and sprinkle on Italian parsley and half of the Parmigiano-Reggiano cheese; stir until combined.', 'Serve pasta topped with the remaining Parmigiano-Reggiano cheese.']
	parse_ingredient_list(ingredients)

	for step in steps:
		get_cooking_method(step)