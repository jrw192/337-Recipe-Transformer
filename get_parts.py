import re
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
stop_words = list(stopwords.words("english"))
tt = TweetTokenizer()
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

#takes in one ingredient listing and returns a dictionary of name, quantity, measurement, preparation
def parse_one_ingredient(listing):
	split_information = []
	# print(listing)
	rest = listing #we will be splitting the listing several times based on found values

	# this assumes that if parenthesis contains measurement/quantity,
	# it describes how the amount that a packet/package holds
	parens_found = re.search(r'[(][\S\s]+[)]', rest)
	quantity = 0
	other_measurement = ""
	quantity_measurement_found = False
	if parens_found:
		temp = parens_found.group(0)[1:-1]

		for measure in known_measures:
			if measure in temp:
				# measure
				if measure == "to taste":
					continue
				other_measurement = measure

				# quantity
				fraction_re = '\d+[\s]{0,1}\d*((/|\.)\d+)?|[.]\d+'
				quantity = re.search(fraction_re, temp)
				if quantity:
					quantity = quantity.group(0).lstrip().rstrip()

				break
		
		# if quantity != 1:
		# 	measurement = measurement + " s"
		rest = rest.replace(parens_found.group(0), '')
		quantity_measurement_found = True

	#find preparation
	preparation = ''
	for method in known_methods:
		method_re = '[a-z]*' + method + '[a-z]*'
		prep_word = re.search(method_re, rest)

		if prep_word:
			prep_word = prep_word.group(0)

			prep_re = '[a-z]+ly ' + prep_word
			prep_phrase = re.search(prep_re, rest)

			if prep_phrase: #find adverb (eg: thinly, finely)
				preparation = prep_phrase.group(0)
				rest = rest.replace(preparation, '')
			else:
				preparation = prep_word
				rest = rest.replace(preparation, '')


	# if',' in rest:
	# 	temp_rest = rest.split(",")[1]
	# 	for sw in stop_words:
	# 		if sw in temp_rest:
	# 			rest = rest.split(",")[0]
	# 			break
	
	if not quantity_measurement_found:
		#find quantity
		fraction_re = '\d+[\s]{0,1}\d*((/|\.)\d+)?|[.]\d+'
		quantity = re.search(fraction_re, rest)
		# print(quantity)
		if quantity:
			quantity = quantity.group(0).lstrip().rstrip()
			
		else:
			quantity = ''
		if quantity != '':
			rest = rest.split(quantity)[1]

	#find measure
	measurement = ''
	for measure in known_measures:
		if measure in rest:
			if measure == "to taste":
				measurement = "to taste" #apparently we have a problem with this measure....
			else:
				word_index = rest.index(measure)
				measurement = rest[word_index:].split(" ")[0] #find where word is, extract the entire word to get plurality (eg clove -> cloves)

			break
	measurement = measurement.lstrip()
	measurement = measurement.rstrip()

	if measurement == "to taste": #to taste is usually found at the end....
		rest = rest.split(measurement)[0]
	elif measurement != '':
		rest = rest.split(measurement)[1]
	#find name
	#strip leading and trailing spaces
	# name = rest.lstrip().rstrip()
	name = get_ingredient_name(rest)

	if quantity_measurement_found:
		measurement = other_measurement

	if ' and ' in name:
		name1, name2 = name.split('and')
		names =  [name1.lstrip().rstrip(), name2.lstrip().rstrip()]
		for name in names:
			ingred_dict = {}
			ingred_dict['name'] = name
			ingred_dict['quantity'] = quantity
			ingred_dict['measurement'] = measurement
			ingred_dict['preparation'] = preparation
			split_information.append(ingred_dict)
	else:
		ingred_dict = {}
		ingred_dict['name'] = name
		ingred_dict['quantity'] = quantity
		ingred_dict['measurement'] = measurement
		ingred_dict['preparation'] = preparation

		split_information.append(ingred_dict);

	# print("split_information: ", split_information)
	return split_information

#takes in an array of the ingredient list
def parse_ingredient_list(ingredients):
	# print(stop_words)
	parsed_ingredients = []
	for ingredient in ingredients:
		parsed = parse_one_ingredient(ingredient)
		for item in parsed:
			parsed_ingredients.append(item)
		# print(ingredient)
		# print(parsed)
	return parsed_ingredients

#if 'JJ' in tag => adjective
#if 'NN' in tag => noun

def get_ingredient_name(string):
	entities = []
	tokenized = tt.tokenize(string)
	tagged = nltk.pos_tag(tokenized)
	for item in tagged:
		if item[0] in stop_words and item[0] != 'and':
			break
		if 'NN' in item[1] or 'JJ' in item[1] or item[0] == 'and':
			entities.append(item[0])
	entities = ' '.join(entities)
	return entities




if __name__ == "__main__":
	ingredients =  ['2 pounds white carp, cut into large chunks', '1 tablespoon vegetable oil', '1 tablespoon red chile powder', '1 tablespoon ground turmeric', '1 1/2 teaspoons salt', '1/4 cup tamarind pulp', '1 cup warm water', '1/4 cup oil', '1/2 teaspoon cumin seeds', '1 large onion, minced', '1 1/2 tablespoons garlic paste', '2 tablespoons red chile powder', '2 tablespoons ground coriander', '1 pinch salt to taste', '1 tablespoon chopped fresh coriander (cilantro), or to taste']
	steps = ['Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes. Drain and transfer to a pasta bowl.', 'Combine garlic and olive oil in a cold skillet. Cook over medium heat to slowly toast garlic, about 10 minutes. Reduce heat to medium-low when olive oil begins to bubble. Cook and stir until garlic is golden brown, about another 5 minutes. Remove from heat.', 'Stir red pepper flakes, black pepper, and salt into the pasta. Pour in olive oil and garlic, and sprinkle on Italian parsley and half of the Parmigiano-Reggiano cheese; stir until combined.', 'Serve pasta topped with the remaining Parmigiano-Reggiano cheese.']
	# ingredients = ["1 (18.25 ounce) package devil's food cake mix", "1 (5.9 ounce) package instant chocolate pudding mix", "1 cup sour cream", "1 cup vegetable oil", "1/2 cup warm water", "2 cups semisweet chocolate chips"]
	# parsed = parse_ingredient_list(ingredients)
	parsed = parse_one_ingredient(ingredients[4])
	# print(parsed)
	# myName = get_ingredient_name("one pound of flour")
	# print(myName)












