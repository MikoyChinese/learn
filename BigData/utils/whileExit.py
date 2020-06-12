#-*- coding: utf-8 -*-
'''
	author = Mikoy
	purpose:
	递归指定文件夹，对其子内容进行读取，如果是文件夹，则继续递归，如果是文件，则记录Dir地址
'''

import os

dir_lst = []

def whileExit(sourceDir):
	for organ_file in os.listdir(sourceDir):
		
	
	
