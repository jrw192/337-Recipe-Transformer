import re

# Ingredients
	# Ingredient name
	# Quantity
	# Measurement (cup, teaspoon, pinch, etc.)
	# (optional) Descriptor (e.g. fresh, extra-virgin)
	# (optional) Preparation (e.g. finely chopped

def parse_one_ingredient(listing):
	print(listing)
	listing = listing.split(",")[0]
	fraction_re = '[0-9]+((/|\.)[0-9]+)?'
	quantity = re.search(fraction_re, listing)
	if quantity:
		quantity = quantity.group(0)
	else:
		quantity = "N/A"
	# print(quantity)
	# print(listing.split(quantity))
	rest = listing
	if quantity != "N/A":
		rest = listing.split(quantity)[1]

	#read measures.txt file of measures in as an array
	with open("measures.txt", "r") as m_f:
		known_measures = m_f.read().splitlines()
	m_f.close()


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
		rest = listing.split(measurement)[0]
	elif measurement != "N/A":
		rest = listing.split(measurement)[1]

	name = rest
	print("name: %s, quantity: %s, measurement: %s" % (name, quantity, measurement))







if __name__ == "__main__":
	ingredients = ['1 pound uncooked spaghetti', '6 cloves garlic, thinly sliced', '1/2 cup olive oil', '1/4 teaspoon red pepper flakes, or to taste', 'salt and freshly ground black pepper to taste', '1/4 cup chopped fresh Italian parsley', '1 cup finely grated Parmigiano-Reggiano cheese']
	for ingredient in ingredients:
		parse_one_ingredient(ingredient)
	# parse_one_ingredient(ingredients[0])