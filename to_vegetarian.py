from parse_html import parse_html
from transform_dicts import to_healthydict

## WIP: My old code was unnecessarily complex oops


# def transform_vegetarian(name, ingredients, directions):
# 	#create counters for the ingredients and directions
# 	counti=-1
# 	countd=-1


# 	#iterate through the name and change the name to the substitutions
# 	for subst in to_healthydict:
# 		if subst in name.lower():
# 			subst1=subst.title()
# 			name=name.replace(subst1,to_healthydict[subst].title())


# 	#iterate through the ingredients list and see if the words are in the to_healthydict dict and then change it accordingly.
# 	for dicts in ingredients:
# 		counti+=1
# 		for subst in to_healthydict:
# 			if subst in dicts['name'].lower():
# 				# newingredients.append(subst)
# 				dicts['name']=dicts['name'].lower().replace(subst, to_healthydict[subst])
# 				ingredients[counti]['name']=dicts['name']
		

# 	#iterate through the directions list and see if the words are in the to_healthydict dict and then change it accordingly.
# 	for dcts in directions:
# 		countd+=1
# 		countpi=-1
# 		for ing in to_healthydict:
# 			if ing in dcts['original'].lower():
# 				dcts['original']=dcts['original'].lower().replace(ing,to_healthydict[ing])
# 				directions[countd]['original']=dcts['original']
# 			if ing in dcts['method'].lower():
# 				dcts['method']=dcts['method'].lower().replace(ing,to_healthydict[ing])
# 				directions[countd]['method']=dcts['method'] 
# 		for ingredient in dcts['ingredients']:
# 			countpi+=1
# 			for ing in to_healthydict:
# 				if ing in ingredient.lower():
# 					ingredient=ingredient.lower().replace(ing, to_healthydict[ing])
# 			dcts['ingredients'][countpi]=dcts['ingredients'][countpi].replace(dcts['ingredients'][countpi],ingredient)


# 	return name, ingredients, directions



