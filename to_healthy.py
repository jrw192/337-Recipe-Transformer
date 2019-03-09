from parse_html import parse_html
from transform_dicts import tohealthy


def transform_healthy(recipe):
	#initialize a list and a counter and also get the parsed html
	newingredients=[]
	counti=-1
	countd=-1
	# recipe = parse_html()
	name=recipe['name']
	directions=recipe['directions']
	ingredients=recipe["ingredients"]
	# print(name.lower())
	# print(directions)

	#iterate through the name and change the name to the substitutions
	for subst in tohealthy:
		if subst in name.lower():
			subst1=subst.title()
			name=name.replace(subst1,tohealthy[subst].title())
	print(name)


	# version 1 (also works/ don't delete)
		#iterate through the ingredients list and see if the words are in the tohealthy dict and then change it accordingly.
	for word in ingredients:
		counti+=1
		for subst in tohealthy:
			if subst in word:
				# newingredients.append(subst)
				word=word.replace(subst, tohealthy[subst])
				ingredients[counti]=word
		
	print(ingredients)

	#iterate through the directions list and see if the words are in the tohealthy dict and then change it accordingly.
	for words in directions:
		countd+=1
		for ing in tohealthy:
			if ing in words:
				words=words.replace(ing,tohealthy[ing])
				directions[countd]=words

	print(directions)

	# # version 2(also works)
	# #iterate through the ingredients list and see if the words are in the tohealthy dict and then change it accordingly.
	# for word in ingredients:
	# 	counti+=1
	# 	for subst in tohealthy:
	# 		if subst in word:
	# 			newingredients.append(subst)
	# 			ingredients[counti]=word.replace(subst, tohealthy[subst])
		
	# print(ingredients)

	# #iterate through the directions list and see if the words are in the tohealthy dict and then change it accordingly.
	# for words in directions:
	# 	countd+=1
	# 	for ing in newingredients:
	# 		if ing in words:
	# 			words=words.replace(ing,tohealthy[ing])
	# 			directions[countd]=words

	# print(directions)
	return name, ingredients, directions




if __name__ == '__main__':
	transform_healthy()
