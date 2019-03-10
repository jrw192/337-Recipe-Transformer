from parse_html import parse_html
from transform_dicts import to_unhealthydict


def transform_unhealthy(name, ingredients, directions):
	#create counters for the ingredients and directions
	counti=-1
	countd=-1


	#iterate through the name and change the name to the substitutions
	for subst in to_unhealthydict:
		if subst in name.lower():
			subst1=subst.title()
			name=name.replace(subst1,to_unhealthydict[subst].title())


	#iterate through the ingredients list and see if the words are in the to_unhealthydict dict and then change it accordingly.
	for dicts in ingredients:
		counti+=1
		for subst in to_unhealthydict:
			if subst in dicts['name']:
				# newingredients.append(subst)
				dicts['name']=dicts['name'].replace(subst, to_unhealthydict[subst])
				ingredients[counti]['name']=dicts['name']
		

	#iterate through the directions list and see if the words are in the to_unhealthydict dict and then change it accordingly.
	for dcts in directions:
		countd+=1
		countpi=-1
		for ing in to_unhealthydict:
			if ing in dcts['original']:
				dcts['original']=dcts['original'].replace(ing,to_unhealthydict[ing])
				directions[countd]['original']=dcts['original']
			if ing in dcts['method']:
				dcts['method']=dcts['method'].replace(ing,to_unhealthydict[ing])
				directions[countd]['method']=dcts['method'] 
		for ingredient in dcts['ingredients']:
			countpi+=1
			for ing in to_unhealthydict:
				if ing in ingredient:
					ingredient=ingredient.replace(ing, to_unhealthydict[ing])
			dcts['ingredients'][countpi]=dcts['ingredients'][countpi].replace(dcts['ingredients'][countpi],ingredient)


	return name, ingredients, directions



