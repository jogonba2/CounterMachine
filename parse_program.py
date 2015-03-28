#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Overxfl0w 13 #

def parse(file_name):
	with open(file_name,"rb") as fd:
		readed = fd.read()
		init_values = parse_values(readed[readed.rfind("# SEGMENT DATA #")+len("# SEGMENT DATA #"):readed.rfind("# SEGMENT CODE #")])
		program     = parse_program(readed[readed.rfind("# SEGMENT CODE #")+len("# SEGMENT CODE #"):])
	fd.close()
	return init_values,program

def parse_program(prg): return [x.strip() for x in prg.replace("\n","").split(";") if x!='']
	
def parse_values(init_values): 
	try: return eval(init_values)
	except Exception as e: print "Warning with evals :)" ;exit(-1)
