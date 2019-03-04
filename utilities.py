###
# File meant for helper functions
# comment code with @param and @return with the datatype and data info 
###

###
# ACTION ITEMS:
#
# get ingredients, name, descriptor, tools, quantity - Ilham, Diane, Jodie, Kimberly
###

import string

###
# Removes empty strings in list and formats each item 
#
# @param: list of strings
# @return: list of strings 
###
def list_formatter(lst):
  # remove line breaks and extra spaces
  for x in range(len(lst)):
    lst[x] = ' '.join(lst[x].split())

  # remove empty strings from list
  lst = list(filter(None, lst))

  return lst
