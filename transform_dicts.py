meat_dict = {
	"chicken": "meat",
	"beef": "meat",
	"pork": "meat",
	"duck": "meat",
	"turkey": "meat",
	"sausage": "meat",
	"bacon": "meat",
	"steak": "meat",
	"goose": "meat",
	"patty": "meat"
}

fish_dict = {
	"salmon": "fish",
	"tuna": "fish",
	"halibut": "fish",
	"trout": "fish",
	"flounder": "fish",
	"tilapia": "fish",
	"sea bass": "fish",
	"fillet": "fish",
	"mackerel": "fish",
	"cod": "fish",
	"mussel": "fish",
	"shrimp": "fish",
	"prawn": "fish",
	"mahi-mahi": "fish",
	"char": "fish",
	"haddock": "fish",
	"sturgeon": "fish",
	"perch": "fish",
	"eel": "fish",
	"albacore": "fish",
	"perch": "fish",
	"grouper": "fish",
	"catfish": "fish",
	"herring": "fish",
	"shark": "fish",
	"swordfish": "fish",
	"anchovy": "fish"
}


#### To and from Vegetarian

veg_sub_dict = {
	"meat": ["tofu", "tempeh", "jackfruit", "mushroom", "seitan", "bean", "eggplant", "lentil", "beet"],
	"seasoned/smoked meat": ["crumbled tofu seasoned with fennel", "parsley and garlic", "roasted vegetables", "toasted nuts", "smoked tofu"],
	"sauce": ["soy sauce", "vegetarian oyster sauce"],
	"broth": ["mushroom broth", "vegetable broth"],
	"stock": ["vegetable stock", "bouillon cubes"],
	"gelatin" : ["agar-agar", "guar gum", "xanthan gum"]
}

non_veg_sub_dict = {
	"meat sub": ["chicken", "pork", "duck", "turkey", "sausage", "bacon", "salmmon", "tuna", "sea bass", "cod"],
	"seasoned meat sub": ["salami, prosciutto, chorizo, pepperoni, pancetta"],
	"sauce sub": ["fish sauce, oyster sauce"],
	"broth sub": ["chicken broth", "beef broth"],
	"stock sub": ["chicken stock", "beef stock", "fish stock"]
}

to_vegetariandict = {
	# Classifies an ingredient

  	# Meats, Poultry and Fish
	"chicken": "meat",
	"beef": "meat",
	"pork": "meat",
	"duck": "meat",
	"turkey": "meat",
	"sausage": "meat",
	"bacon": "meat",
	"steak": "meat",
	"goose": "meat",
	"salmon": "meat",
	"tuna": "meat",
	"halibut": "meat",
	"hot dog":'meat',
	"trout": "meat",
	"flounder": "meat",
	"tilapia": "meat",
	"sea bass": "meat",
	"fillet": "meat",
	"mackerel": "meat",
	"cod": "meat",
	"mussel": "meat",
	"shrimp": "meat",
	"prawn": "meat",
	"mahi-mahi": "meat",
	"char": "meat",
	"haddock": "meat",
	"sturgeon": "meat",
	"perch": "meat",
	"eel": "meat",
	"albacore": "meat",
	"perch": "meat",
	"grouper": "meat",
	"catfish": "meat",
	"herring": "meat",
	"shark": "meat",
	"swordfish": "meat",
	"anchovy": "meat",

	# Smoked Meats
	"salami": "seasoned/smoked meat",
	"prosciutto": "seasoned/smoked meat",
	"chorizo": "seasoned/smoked meat",
	"coppa": "seasoned/smoked meat",
	"cervelat": "seasoned/smoked meat",
	"culatello": "seasoned/smoked meat",
	"guanciale": "seasoned/smoked meat",
	"jamon": "seasoned/smoked meat",
	"lardo": "seasoned/smoked meat",
	"pancetta": "seasoned/smoked meat",
	"pepperoni": "seasoned/smoked meat",
	"soppressata": "seasoned/smoked meat",
	
	# Broths
	"chicken broth": "broth",
	"beef broth": "broth",
	"fish broth": "broth",
	"broth": "broth",

	# Stocks
	"chicken stock": "stock",
	"beef stock": "stock",
	"fish stock": "stock",

	# Sauces
	"fish sauce": "sauce",
	"oyster sauce": "sauce",
	"shrimp paste": "sauce", #idk if this is a sauce

	# Gelatin
	"gelatin": "gelatin",
}

to_non_vegetariandict = {
	# Meat sub
	"tofu": "meat sub",
	"tempeh": "meat sub",
	"jackfruit": "meat sub",
	"mushroom": "meat sub",
	"seitan": "meat sub",
	"bean": "meat sub",
	"eggplant": "meat sub",
	"lentil": "meat sub",
	"beet": "meat sub",

	# Seasoned meat sub
	"crumbled tofu seasoned with fennel": "seasoned meat sub",
	"parsley and garlic": "seasoned meat sub",
	"roasted vegetables": "seasoned meat sub",
	"toasted nuts": "seasoned meat sub",
	"smoked tofu": "seasoned meat sub",

	# Broth sub
	"mushroom broth": "broth sub",
	"vegetable broth": "broth sub",

	# stock sub
	"vegetable stock": "stock sub",
	"bouillon cubes": "stock sub",

	# Sauce sub
	"soy sauce": "sauce sub",
	"vegetarian oyster sauce": "sauce sub"
}

####### To and from healthy

#original to healthy
to_healthydict={
	'beef': 'turkey',
	'fried chicken': 'grilled chicken',
	'turkey burger': 'veggie burger',
	'burger': 'mushroom',
	'pork': 'jackfruit',
	'boneless':'',
	'plain':'',
	'meat':'meat/veggie',
	'pork chops':'jackfruit',
	# 'turkey': 'tofurkey',
	'chicken': 'tempeh',
	'ground beef': 'ground turkey',
	'ground pork': 'ground jackfruit',
	'bacon': 'turkey bacon',
	'sausage': 'turkey sausage',
	'white rice': 'brown rice',
	'rice': 'brown rice',
	'pasta': 'whole-grain pasta',
	'spaghetti': 'whole-grain spaghetti',
	'bread': 'whole-grain bread',
	'penne': 'whole-grain penne',
	'flour tortilla': 'corn tortilla',
	'tortilla' : 'lettuce',
	'butter': 'margarine',
	'sour cream': 'greek yogurt',
	'croutons': 'almonds',
	'sugar': 'stevia',
	'flour': 'coconut flour',
	'salt': 'himalayan salt',
	'breadcrumbs': 'chia seeds',
	'bread crumbs': 'chia seeds',
	'bread crumb': 'chia seed',
	'chocolate chips': 'cocoa nibs',
	'iceberg': 'romaine',
	'ranch dressing': 'olive oil',
	'ranch' :'olive oil',
	'peanut butter': 'almond butter',
	'milk' : 'almond milk',
	# 'oil' : 'vegetable oil',
	'soy sauce':'coconut aminos',
	# 'frying' : 'grilling or baking',
	# 'fried':'grilled or baked',
	# 'fry':'grill or bake',
	'cornstarch':'wheat flour',
	'chocolate':'dark-chocolate'
}

# original to nonhealthy
to_unhealthydict={
	'sugar ':'corn syrup',
	'olive oil':'lard',
	'coconut oil':'lard',
	'vegetable oil':'lard',
	' oil' : 'lard',
	'plain':'glazed',
	'bread':'donut',
	'milk' : 'heavy cream',
	'veggie burger':'burger',
	'veggie':'beef',
	'water':'sugarwater',
	'dark chocolate':'milk chocolate',
	# 'bake':'fry',
	# 'grill':'fry',
	'red pepper':'pepperoni',
	'salt':'salt coated in oil',
	'carrots':'licorice',
	'carrot':'licorice',
	'flour':'cornstarch',
	'egg':'artificial egg',
	# 'green onion':' fried green onion',
	# 'yellow onion':'fried yellow onion',
	# ''
	'onion':'fried onion',
	'green pepper':'fried green pepper'

}

####### To and from Sicilian

#style of cuisine: Sicilian Cuisine (Sicily in Italy)
to_siciliandict={
	'meatsauce': 'ragu',
	'tomato': 'Pachino tomato',
	'noodles': 'spaghetti',
	'broth': 'soup',
	'tilapi': 'sea bream',
	'salmon': 'bluefin tuna',
	'blueberry':'mulberry',
	'cilantro': 'mint',
	'shark': 'swordfish',
	'marlin': 'swordfish',
	'carp':'sea bream',
	'donut': 'cannoli',
	'red wine': 'Marsala',
	'wine': 'Marsala',
	'green bean': 'fava bean',
	'lima bean': 'fava bean',
	'salt': 'sea salt',
	'herring': 'sardines', 
	'pesto': 'zogghiu',
	'quinoa': 'couscous', 
	'vegetable oil': 'olive oil',
	'cocunut oil': 'olive oil',
	'regular oil':'olive oil',
	'any oil':'olive oil',
	'ground beef': 'ground veal',
	'ground turkey':'ground veal',
	'beef' :'lamb',
	'celery': 'fennels',
	'sorbert': 'granita',
	'flour': 'durum wheat/semolina flour',
	'orange': 'moro orange',
	'provolone': 'caciocavallo',
	'mozerella' :'caciocavallo',
	'american': 'pecorino',
	'chedder' :'caciocavallo',
	'parmesan': 'ricotta',
	'colby':'ricotta',
	'gruyere' :'maiorchino',
	'cottage': 'ricotta',
	'cream cheese' :'ricotta',
	'blue cheese' : 'gorgonzola',
	'meunster' : 'ragusano',
	'guda' : 'canestrato',
	'swiss': 'tuma',
	'feta':'ricotta',
	'garlic': 'Nubia Red Garlic',
	'chocolate': 'Modica chocolate',
	'lemon' :'Siracusa lemon',
	# 'grill': 'fry',
	'ice cream':'gelato',
	'garam masala':'cinnamon',
	'masala curry':'ragu',	
	'curry':'ragu',
	'tumeric':'saffron',
	'basmati rice':'orzo',
	'white rice':'orzo',
	'brown rice':'orzo',
	'cardamom pods':'fava beans',
	'green onion':'Giarratana Onion',
	'yellow onion':"Giarratana Onion",
	'red onion': 'Giarratana Onion',
	'white onion': 'Giarratana Onion',
	'onion':'Giarratana Onion',
	'iceberg lettuce':'arugula',
	'romaine lettuce':'arugula',
	'lettuce':'arugula',
	'soy sauce':'olive oil or Salmoriglio',
	'mushroom':'porcini mushroom',
	'tamarind pulp':'chickpeas',
	'tamarind':'chickpeas',
	'coriander':'menta',
}

to_korean_dict={
  'vegetable oil':'sesame oil',
  'olive oil':'sesame oil',
  'cocunut oil':'sesame oil',
  'oil': 'sesame oil',
  'ketchup': 'gochujang',
  'salt': 'soy sauce',
  'dill pickle':'kimchi',
  'pickle': 'kimchi',
  'pot roast': 'galbijjim',
  'maruchan': 'shin',
  'omelette': 'steamed egg',
  'pancakes': 'hoddeok',
  'noodle' : 'rice noodles',
} 

