import re

T = input()
in_css = False
for _ in xrange(T):
	s = raw_input()
	if '{' in s:
		in_css = True
	elif '}' in s:
		in_css = False
	elif in_css:
		for color in re.findall('#[0-9a-fA-F]{3,6}', s):
			print color
