import os
import re
import reformat
import nary_tree as n_tree
keywords = ["printf","if","else","else if","scanf"]
def solve(str,func_names,parent_list):
	parent_list.append(str)
	call_functions = []
	print str
	for lines in func_names[str]:
		match  = re.search("\b\w+\(.*\)",lines)
		if match:
			string = re.search("\w+",lines)
			check_keyword = string.group().strip()
			if check_keyword in keywords:
				n_tree.curr.insert_key_value(lines)
				continue
			call_functions.append(string.group())
			if string.group() not in parent_list :
				#print str, parent_list , "parent"
				solve(string.group(),func_names,parent_list)
		elif lines[-1]=="{":
			child = n_tree.Tree(n_tree.curr,str)
			n_tree.curr.add_child(child)
			n_tree.curr = child
		elif lines[-1]=='}':
			n_tree.curr = n_tree.curr.get_parent()
		else:
			n_tree.curr.insert_key_value(lines)
			print n_tree.curr.get_dict()
		#print str ," now ",lines


	print str, "calls ",call_functions , parent_list
	parent_list.pop()
file = open("reformat.c","r")
lines = file.readline();
func_names = dict()
func_names["glob"] =  []
curr = "glob"
stack = [curr]
func_param = dict()
curl_bracket_count = 0
while lines:
	#print lines
	if lines.isspace():
		lines = file.readline()
		continue
	match = re.search("(int|float|void|double)\s+\w+\s*\(.*\)",lines)
	if match:
		words  = re.split("\s+",lines);
		function_header  = re.search("\w+",words[1])
		curr = function_header.group()
		func_names[curr] = []
		func_param[curr] = re.search("\(.*\)",lines).group()
		stack.append(curr)
		print stack
		print "curr",curr 
	elif "{" in lines:
		func_names[stack[-1]].append(lines.strip())
		curl_bracket_count+=1
	elif "}" in lines:
		func_names[stack[-1]].append(lines.strip())
		curl_bracket_count-=1
		if curl_bracket_count==0 and len(stack)>1:
			stack.pop()
	else:
		func_names[stack[-1]].append(lines.strip())
	
	lines = file.readline()
	#print func_names
	#print stack
print func_names
print func_param
solve("main",func_names,[])
print "\n\n\n\n\n\n"
def traverse(root):
	print root.get_dict()
	print root.child_len()
	for j in range(root.child_len()):
		traverse(root.get_child(j))
traverse(n_tree.curr)
