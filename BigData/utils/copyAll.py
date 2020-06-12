#coding: utf-8
'''
	author = Mikoy
	purpose: 根据指定的序列，索引对应的图片，并保留文件目录结构。
'''
import os
import shutil

sourceDir = '/media/commaai/480G/454sku/RAWDATA/images' #被索引图片所在的根目录
desDir = '/home/commaai/Desktop/img' #存放找到的图片目录 

data = open('/home/commaai/Desktop/class.txt', 'r').read() #读取指定序列的内容
data_lst = data.split('\n') #转化成list
source_lst = os.listdir(sourceDir) #将根目录内的图片目录进行分解
#在根目录内查询是否存在指定序列
for i in source_lst:
	if i in data_lst:
		chirdDir = sourceDir + '/' + str(i) + '/' #记录找到的目录
		for a, b, c in os.walk(chirdDir): #对目录内容进行读取
			for img in range(len(c)):
				img_sourcedir = a + '/' + c[img] #记录文件的位置
				target_Dir = desDir + '/' + str(i) + '/' + c[img].split('_')[3]+ '/' + c[img].split('_')[4] #存放的文件名及目录
				if not os.path.exists(target_Dir):
					os.makedirs(target_Dir)
				shutil.copy(img_sourcedir, target_Dir)#完成复制

