import os
import re
file = open("trial.c")
for lines in file:
	callback = re.search("(int|float|double|void)\s+\(\s*\*\s*\w+\)\s*\(.*\)",lines)
	if callback:
		print callback.group()
		if "=" in lines:
			value = re.split("=",lines)
			print value[1].strip()
			print re.split("\(.*\)",callback.group())