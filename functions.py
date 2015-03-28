#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Overxfl0w 13 #

def suc(i,registers,cp): 
	registers[i] += 1
	return cp+1

def pre(i,k,registers,cp):
	if registers[i]-1<0: return k
	else: registers[i] -= 1; return cp+1

def goto(n,registers,cp): return n
