from random import randint
from parse_html import parse_html
from transform_dicts import veg_sub_dict, to_vegetariandict

## WIP: My old code was unnecessarily complex oops


def transform_vegetarian(name, ingredients, directions):
	#create counters for the ingredients and directions
	counti=-1
	countd=-1
	substitutes_dict = veg_sub_dict
	transformed = {}

	#change name
	name = "Vegetarian " + name

	#iterate through the ingredients list and see if the words are in the to_vegetariandict dict and then change it accordingly.
	for dicts in ingredients:
		counti+=1
		for subst in to_vegetariandict:
			if subst in dicts['name'].lower():
				category = to_vegetariandict[subst]
				tempList = substitutes_dict[category]

				# if no subs left, repopulate
				if tempList == []:
					tempList = veg_sub_dict[category]
					substitutes_dict[category] = veg_sub_dict[category]

				newingredient = tempList[randint(0, len(tempList)-1)] # pick sub at random
				substitutes_dict[category].remove(newingredient) # remove sub from list

				# newingredients.append(subst)
				dicts['name']=newingredient
				ingredients[counti]['name']=dicts['name']

				# save transformations
				transformed[subst] = newingredient
		

	# iterate through the directions list and see if the words are in the to_vegetariandict dict and then change it accordingly.
	for dcts in directions:
		countd+=1
		countpi=-1
		if "meat" in dcts['original'].lower():
			dcts['original']=dcts['original'].lower().replace(" meat "," vegetable ")
			directions[countd]['original']=dcts['original']
		for ing in to_vegetariandict:
			if ing in dcts['original'].lower():
				dcts['original']=dcts['original'].lower().replace(ing,transformed[ing])
				directions[countd]['original']=dcts['original']
		for ingredient in dcts['ingredients']:
			countpi+=1
			for ing in to_vegetariandict:
				if ing in ingredient.lower():
					ingredient=transformed[ing]
			dcts['ingredients'][countpi]=dcts['ingredients'][countpi].replace(dcts['ingredients'][countpi],ingredient)


	return name, ingredients, directions



