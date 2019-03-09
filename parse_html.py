import requests
from lxml import html
from utilities import list_formatter

###
# Given a url, parses it and extracts all the materials
#
# @param: string - url
# @return: dictionary - keys: part of the recipe; values: list of strings or string of contents
###
def parse_html(url):
	#added on for user input
	# url = input("Enter the url for the recipe, then hit enter:\n")

	# for testing
	# url = 'https://www.allrecipes.com/recipe/241601/sesame-chicken-for-slow-cooker/'
	# url = 'https://www.allrecipes.com/recipe/230818/pork-fried-rice/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202'
  
	# retrieve page contents
	page = requests.get(url)
	tree = html.fromstring(page.content)

  # get each recipe part from xml and add to dictionary
	recipe_parts = {} 
	recipe_parts['ingredients'] = tree.xpath('//span[@class = "recipe-ingred_txt added"]/text()')
	recipe_parts['directions'] = list_formatter(tree.xpath('//span[@class = "recipe-directions__list--item"]/text()')) # join into one string later?
	recipe_parts['name'] = tree.xpath('//h1[@class = "recipe-summary__h1"]/text()')[0]
	recipe_parts['type'] = list_formatter(tree.xpath('//span[@class = "toggle-similar__title"]/text()'))[2:] # first two are 'home' and 'recipe'
	try:
		recipe_parts['time'] = tree.xpath('//span[@class = "ready-in-time"]/text()')[0]
	except:
		recipe_parts['time'] = 'N/A'
	
	# print(recipe_parts['type'])
	# print(recipe_parts)
	return recipe_parts
	
# for testing purposes
if __name__ == '__main__':
	
	test_urls = ['https://www.allrecipes.com/recipe/223016/fresh-blueberry-cake/?internalSource=staff%20pick&referringId=17263&referringContentType=Recipe%20Hub',] # cake
	# 'https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%203', # aglio e olio
	# 'https://www.allrecipes.com/recipe/230818/pork-fried-rice/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202'] # fried rice
	parse_html(test_urls[0])
	# print(parse_html(test_urls[0]))
	# print(parse_html(test_urls[1]))
	# print(parse_html(test_urls[2]))