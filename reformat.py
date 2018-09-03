import os 
import re
import tempfile
def create_temp(program_lines):
	reformat= open("reformat.c","w")
	with tempfile.TemporaryFile() as tmp:
		for j in program_lines:
			tmp.write(j)
		tmp.seek(0);
		for line in tmp:
			if line.isspace():
				continue;
			newline = ""
			line = line.strip()
			if line[-1] ==';' or line[-1]=='>'  or line[-1]=='}' or line[-1]=='{':
				newline="\n"
			if line[-1]=='{':
				line="\n"+line
			reformat.write(line+newline)
	reformat.close()
file = open("cprog.c","r")
lines = file.readline()
program_lines = []
insquotes = False
indquotes = False
while lines:
	string_to_inser = ""
	for j in range(len(lines)):
		if insquotes:
			string_to_inser+=lines[j]
			if lines[j]=="\'":
				insquotes=False
		elif indquotes:
			string_to_inser+=lines[j]
			if lines[j]=="\"":
				indquotes=False
		elif lines[j]=="\'":
			string_to_inser+=lines[j]
			insquotes=True
		elif lines[j]=="\"":
			string_to_inser+=lines[j]
			indquotes=True
		elif re.search("\s+",lines[j]):
			string_to_inser+=lines[j]
		elif lines[j]=="{" or lines[j]=="}":
			string_to_inser+="\n"+lines[j]+'\n'
		elif lines[j]==";":
			string_to_inser+=lines[j]+'\n'
		else:
			string_to_inser+=lines[j]
	program_lines.append(string_to_inser)
	lines=file.readline()
#print program_lines
create_temp(program_lines)
file.close()