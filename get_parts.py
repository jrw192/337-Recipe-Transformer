import re

# Ingredients
	# Ingredient name
	# Quantity
	# Measurement (cup, teaspoon, pinch, etc.)
	# (optional) Descriptor (e.g. fresh, extra-virgin)
	# (optional) Preparation (e.g. finely chopped


#read in some lists
with open("methods.txt", "r") as m_f:
	known_methods = m_f.read().splitlines()
m_f.close()

with open("measures.txt", "r") as m_f:
	known_measures = m_f.read().splitlines()
m_f.close()

#takes in one ingredient listing and returns an array of name, quantity, measurement, preparation
def parse_one_ingredient(listing):
	print(listing)
	rest = listing #we will be splitting the listing several times based on found values
	#find preparation
	preparation = "N/A"
	for method in known_methods:
		if method in listing.lower():
			
			word_index = rest.index(method)
			prep_word = rest[word_index:].split(" ")[0]
			prep_re = '[a-z]+ly ' + prep_word
			prep_phrase = re.search(prep_re, rest)

			if prep_phrase: #find adverb (eg: thinly, finely)
				preparation = prep_phrase.group(0)
				rest = rest.replace(preparation, '')
			else:
				rest = rest.replace(preparation, '')

	rest = rest.split(",")[0]
	
	#find quantity
	fraction_re = '[0-9]+((/|\.)[0-9]+)?'
	quantity = re.search(fraction_re, rest)
	if quantity:
		quantity = quantity.group(0)
	else:
		quantity = "N/A"
	# print(quantity)
	# print(listing.split(quantity))
	if quantity != "N/A":
		rest = rest.split(quantity)[1]

	#find measure
	measurement = "N/A"
	for measure in known_measures:
		if measure in rest:
			if measure == "to taste":
				measurement = "to taste" #apparently we have a problem with this  measure....
			else:
				word_index = rest.index(measure)
				measurement = rest[word_index:].split(" ")[0] #find where word is, extract the entire word to get plurality (eg clove -> cloves)

			break
	# print(measurement)

	if measurement == "to taste": #to taste is usually found at the end....
		rest = rest.split(measurement)[0]
	elif measurement != "N/A":
		rest = rest.split(measurement)[1]

	#find name
	name = rest
	print("name: %s, quantity: %s, measurement: %s, preparation: %s" % (name, quantity, measurement, preparation))
	return [name, quantity, measurement, preparation]

#takes in an array of the ingredient list
def parse_ingredient_list(ingredients):
	parsed_ingredients = []
	for ingredient in ingredients:
		parsed_ingredients.append(parse_one_ingredient(ingredient))

	return parsed_ingredients


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



#takes in one step (e.g. cook for 15 minutes) and parses it into a dictionary of ingredient, tool, method, time
def parse_one_step(step):
	primary_method = get_cooking_method(step)
	return

#takes in all steps and parses it into a list of dictionary where keys=step number and value = parsed step 
def parse_all_steps(steps_list):
	return





if __name__ == "__main__":
	ingredients = ['1 pound uncooked spaghetti', '6 cloves garlic, thinly sliced', '1/2 cup olive oil', '1/4 teaspoon red pepper flakes, or to taste', 'salt and freshly ground black pepper to taste', '1/4 cup chopped fresh Italian parsley', '1 cup finely grated Parmigiano-Reggiano cheese']
	steps = ['Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes. Drain and transfer to a pasta bowl.', 'Combine garlic and olive oil in a cold skillet. Cook over medium heat to slowly toast garlic, about 10 minutes. Reduce heat to medium-low when olive oil begins to bubble. Cook and stir until garlic is golden brown, about another 5 minutes. Remove from heat.', 'Stir red pepper flakes, black pepper, and salt into the pasta. Pour in olive oil and garlic, and sprinkle on Italian parsley and half of the Parmigiano-Reggiano cheese; stir until combined.', 'Serve pasta topped with the remaining Parmigiano-Reggiano cheese.']
	parse_ingredient_list(ingredients)

	for step in steps:
		get_cooking_method(step)
	# get_cooking_method(steps[0])













