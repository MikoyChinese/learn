#-*- coding: utf-8 -*-
import math #导入数学库
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Cal angle!')
    parser.add_argument('--a', dest='a', default= 1, type=float)
    parser.add_argument('--b', dest='b', default= 1, type=float)
    parser.add_argument('--c', dest='c', default= 1, type=float)
    args = parser.parse_args()
    return args

def cos_angle(a, b, c):
    cos_angle = (b ** 2 + c ** 2 - a ** 2)/(2*b*c)
    return cos_angle
def cal_angle():
    a = args.a
    b = args.b
    c = args.c
    cos_A = cos_angle(a, b, c)
    cos_B = cos_angle(b, a, c)
    cos_C = cos_angle(c, a, b)
    A = 180*math.acos(cos_A)/math.pi
    B = 180*math.acos(cos_B)/math.pi
    C = 180*math.acos(cos_C)/math.pi
    
    print 'The angle of A is ' + str(A) + ' and the soild is ' + str(a) + '!!!'
    print 'The angle of B is ' + str(B) + ' and the soild is ' + str(b) + '!!!'
    print 'The angle of C is ' + str(C) + ' and the soild is ' + str(c) + '!!!'
    print A+B+C
if __name__ == '__main__':
    args = parse_args()
    test = cal_angle()

