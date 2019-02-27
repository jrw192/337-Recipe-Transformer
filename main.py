from parse_html import parse_html

# we can have links in main and pass to parser?

###
# Runs the body of the program 
#
# @param: string - url to an allrecipes recipe? 
# @return: ?
###
def main(url):
  # get dictionary of recipe parts 
  recipe_dict = parse_html(url)

if __name__ == '__main__':
  test_urls = ['https://www.allrecipes.com/recipe/223016/fresh-blueberry-cake/?internalSource=staff%20pick&referringId=17263&referringContentType=Recipe%20Hub', # cake
                'https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%203', # aglio e olio
                'https://www.allrecipes.com/recipe/230818/pork-fried-rice/?internalSource=hub%20recipe&referringContentType=Search&clickId=cardslot%202'] # fried rice
  main(test_urls[0])