#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os
import re

def find_file(file_path, o_post, lis):
	ls = os.listdir(file_path)
	for i in ls:
		son_path = os.path.join(file_path,i)
		if os.path.isdir(son_path):
			find_file(son_path,o_post,lis)
		else:
			file_ext = str(i.split('.')[-1])
			if file_ext == o_post and not(os.path.isdir(son_path)):
				#print(os.path.join(son_path))
				lis.append(os.path.join(son_path))
			#readFile(os.path.join(son_path))
	return lis
	
# readfile print each line
def readFile(filename):
	fopen = open(filename, 'r') # r-read
	for eachLine in fopen:
		print "content:",eachLine
	fopen.close()

def alter(file,old_str,new_str):
	file_data = ""
	with open(file, "r") as f:
		for line in f:
			if old_str in line:
				indexList = findCloumn(line,old_str,[])
				data="";
				inx = 0
				for index in indexList:
					next = index + inx + 1 
					#close-open
					line = line if data == "" else data
					cut = line[0:next]
					residue = "" 
					null = line[next:next+4]
					_null = line[next:next+5]
					residue = line[next:]
					matchObj = re.match(r'=? *null',residue)
					if null == "null" and _null == "=null":
						data = line
					elif matchObj:
						data = line
					elif old_str == "!=" and new_str == "!==":
						alf = residue[0:1]
						if alf != "=":
							cut = cut[0:next-2]+new_str
							data = cut + residue
							inx = inx+1
						else:
							data = line	
					elif old_str == "==" and new_str =="===":
						pre = cut[-3]
						alf = residue[0:1]
						if (pre != "=" and pre != "!" and alf != "="):
							cut = cut[0:next-2]+new_str
							data = cut + residue
							inx = inx+1
						else:	
							data = line
					else:
						data = line
				file_data += data	
			else:
				file_data += line
		with open(file,"w") as f:
			f.write(file_data)
		
def findCloumn(str,form,ls):
	count=0
	str_list=list(str)
	lens = len(form)
	combo = ""
	i=0
	for each_char in str_list:
		combo += each_char
		if len(combo) < lens:
			i=i+1
		else:
			if len(combo) == lens:
				if combo == form:
					ls.append(i);
				split_combo = combo.strip()
				#first = split_combo[0]
				combo = ''
				for inx,c in enumerate(split_combo):
					if inx != 0:
						combo = combo + c
				i=i+1
	return ls				
		
	
f_path = r'C:\Users\lihro\Desktop\Python'
old_post = 'js'
files = find_file(f_path, old_post, [])
for file in files:
	alter(file,"!=","!==")
	alter(file,"==","===")
"""
print(findCloumn('i=23456i=iasda ','i=',[]))
"""
