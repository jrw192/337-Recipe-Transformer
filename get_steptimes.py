import re
from datetime import time

#get the time instructed in each step
#eg: "cook for 5 minutes" => 5 minutes, "cook until browned" => until browned


time_units = ['second', 'minute', 'hour', 'day', 'until']

#gets the times mentioned in ONE step of the recipe
def get_steptimes(step):
	print(step)
	times = []
	for unit in time_units:
		temp_step = step #set a temp step variable 
		if unit == 'until':
			time_re = 'until [\w\s]+'

		else:
			time_re = '\d+ ' + unit + '[s]{0,1}'

		while re.search(time_re, temp_step): #keep searching until we don't find any more time units
			time_search = re.search(time_re, temp_step)

			if time_search:
				time = time_search.group(0)
				times.append(time)
				temp_step  = temp_step.split(time)[1] #continue searching with the rest of the step

	# print(times)
	# time = ', or '.join(times)
	return times





if __name__ == "__main__":
	ingredients = ['1 pound uncooked spaghetti', '6 cloves garlic, thinly sliced', '1/2 cup olive oil', '1/4 teaspoon red pepper flakes, or to taste', 'salt and freshly ground black pepper to taste', '1/4 cup chopped fresh Italian parsley', '1 cup finely grated Parmigiano-Reggiano cheese']
	steps = ['Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes. Drain and transfer to a pasta bowl.', 'Combine garlic and olive oil in a cold skillet. Cook over medium heat to slowly toast garlic, about 10 minutes. Reduce heat to medium-low when olive oil begins to bubble. Cook and stir until garlic is golden brown, about another 5 minutes. Remove from heat.', 'Stir red pepper flakes, black pepper, and salt into the pasta. Pour in olive oil and garlic, and sprinkle on Italian parsley and half of the Parmigiano-Reggiano cheese; stir until combined.', 'Serve pasta topped with the remaining Parmigiano-Reggiano cheese.']

	for step in steps:
		get_steptimes(step)



