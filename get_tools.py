import requests
from lxml import html
from utilities import list_formatter
from parse_html import parse_html


def get_tools():
	#call the parse html function
	directions = parse_html()["directions"]

	#get the tools from tools text and make it a list
	with open("tools.txt", "r") as kf:
		known_tools = kf.read().splitlines()
	kf.close()

	#iterate through directions and find the tool for each step
	prevtools=[]
	for step in directions:
		tools = []
		for tool in known_tools:
			if tool in step:
				tools.append(tool)
				prevtools.append(tool)
		if not tools:
			tools=prevtools[0:] #if none of the tools are in the step most likely you are using previous tools from the previous step
		print(tools)


if __name__ == '__main__':
	get_tools()