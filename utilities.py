###
# File meant for helper functions
# comment code with @param and @return with the datatype and data info 
###

###
# ACTION ITEMS:
#
# - transform code: Kimberly
# - transformation dictionaries: Ilham
# - transformation dictionaries: Diane
# - ingredients from steps and times(?): Jodie
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
