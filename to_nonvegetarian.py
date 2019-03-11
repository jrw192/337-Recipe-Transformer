from random import randint
from parse_html import parse_html
from transform_dicts import non_veg_sub_dict, to_non_vegetariandict

## WIP: My old code was unnecessarily complex oops


def transform_nonvegetarian(name, ingredients, directions):
	#create counters for the ingredients and directions
	counti=-1
	countd=-1
	substitutes_dict = non_veg_sub_dict
	transformed = {}

	#change name
	# if "Meatless" in name:
	# 	name = name.lower().replace("Meatless", " ")
	if "Vegetarian" in name:
		name = name.lower().replace("Vegetarian", "Non-Vegetarian").title()
	else:
		name = "Non-Vegetarian " + name

	#iterate through the ingredients list and see if the words are in the to_non_vegetariandict dict and then change it accordingly.
	for dicts in ingredients:
		counti+=1
		for subst in to_non_vegetariandict:
			if subst in dicts['name'].lower():
				category = to_non_vegetariandict[subst]
				tempList = substitutes_dict[category]

				# if no subs left, repopulate
				if tempList == []:
					tempList = non_veg_sub_dict[category]
					substitutes_dict[category] = non_veg_sub_dict[category]

				newingredient = tempList[randint(0, len(tempList)-1)] # pick sub at random
				substitutes_dict[category].remove(newingredient) # remove sub from list

				# newingredients.append(subst)
				dicts['name']=newingredient
				ingredients[counti]['name']=dicts['name']

				# save transformations
				transformed[subst] = newingredient
		

	# iterate through the directions list and see if the words are in the transformed dict and then change it accordingly.
	for dcts in directions:
		countd+=1
		countpi=-1
		if "meat" in dcts['original'].lower():
			dcts['original']=dcts['original'].lower().replace(" vegetable "," meat ")
			directions[countd]['original']=dcts['original']
		for ing in transformed:
			if ing in dcts['original'].lower():
				if ing == "potato":
					temp_index = dcts['original'].lower().index("potato")
					dcts['original']= dcts['original'][:temp_index] + transformed[ing] + dcts['original'][temp_index + 7:]
					directions[countd]['original']=dcts['original']
		for ingredient in dcts['ingredients']:
			countpi+=1
			for ing in transformed:
				if ing in ingredient.lower():
					ingredient=transformed[ing]
			dcts['ingredients'][countpi]=dcts['ingredients'][countpi].replace(dcts['ingredients'][countpi],ingredient)


	return name, ingredients, directions



