#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Overxfl0w 13 #

import functions,sys
from parse_program import parse

def usage():
	print "\nUsage: python countermachine.py RegistersNumber ProgramName\n"
	
def generate_registers(registers,size): return [0 for i in xrange(size)]

def load_program(program,control_unit):
	for inst in program: control_unit.append(inst)

def load_registers(init_values,registers):
	for value in init_values: 
		try: registers[value[0]] = value[1]
		except TypeError as te: pass # Ignore bad args #

def main(registers,control_unit,init_values,program,n_registers):
	cp = 0
	load_program(program,control_unit)
	registers = generate_registers(registers,n_registers)
	load_registers(init_values,registers) if init_values!=[] else generate_registers(registers)
	try:
		while True: cp = eval("functions."+program[cp][0:program[cp].rfind(")")]+",registers,cp)")			
	except IndexError as ie: print "\nExecution completed successfully.\n"
	except Exception as e:   print "\nExecution ended for unknown reasons (check the source code).\n"
	finally:
		with open(sys.argv[2]+".sum","wb") as fd:
			for x in xrange(len(registers)): fd.write("Reg "+str(x)+": "+str(registers[x])+"\n")
		fd.close()
		print "Summary saved in: "+sys.argv[2]+".sum"
		
if __name__ == "__main__":
	if len(sys.argv)!=3: usage(); exit(-1)
	(registers,control_unit,n_registers,(init_values,program))=[],[],int(sys.argv[1]),parse(sys.argv[2])
	main(registers,control_unit,init_values,program,n_registers)
