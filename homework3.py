import numpy as np
import math
import random
#1.五角数
# n=0
# i=0
# def getPentagonalNumber():
#     global n,i
#     for n in range(1,100):
#         i +=1
#         five = n*(3*n-1)/2
#         print(five,end=' ')
#         if i%10==0:
#             print('\n')
# getPentagonalNumber()
#####################################################################################################
#2.整数各个数的和
# l1=[]
# n=str(input('please >>'))
# def sumDigits():
#     global l1
#     for i in n[:]:
#         print(i)
#         l1.append(i)
#     su = int(l1[0])
#     for a in range(1,len(l1)):
#         su = su + int(l1[a]) 
#     print(int(su))
# sumDigits()
#####################################################################################################
#3.排序
# num1,num2,num3=input('Enter three numbers:').split(',')
# def displaySortedNumbers(num1,num2,num3):
#     num1 = float(num1)
#     num2 = float(num2)
#     num3 = float(num3)
#     if num1>num2>num3:
#         print('The sorted numbers:%f %f %f'%(num3 ,num2 ,num1))
#     elif num1>num3>num2:
#         print('The sorted numbers:%f %f %f'%(num2 ,num3 ,num1))
#     elif num2>num1>num3:
#         print('The sorted numbers:%f %f %f'%(num3 ,num1 ,num2))
#     elif num2>num3>num1:
#         print('The sorted numbers:%f %f %f'%(num1 ,num3 ,num2))
#     elif num3>num2>num1:
#         print('The sorted numbers:%f %f %f'%(num1 ,num2 ,num3))
#     else:
#         print('The sorted numbers:%f %f %f'%(num2 ,num1 ,num3))   
# displaySortedNumbers(num1,num2,num3)
# ###################################################################################################
#5.显示字符
# ch1 = int(input('>>'))
# ch2 = int(input('>>'))
# numberPerLine = 10
# l1=[]
# def printChars(ch1,ch2,numberPerLine):
#     b=1
#     for _ in range(ch1,ch2):
#         l1.append(_)
#     for a in l1[:]:
#         if a>48 and a<91:
#             a = chr(a)
#             b+=1
#             print(a,end=' ')
#             if b%numberPerLine==0:
#                 print(end='\n')
# printChars(ch1,ch2,numberPerLine)
###################################################################################################
#6.一年的天数
# year = int(input('>>'))
# l1=[]
# l2=[]
# def numberOfDaysInAYear(year):
#     for _ in range(2010,2021):
#         if _%4==0 and _%100!=0:
#             print('%d' %_ ,'年366天')
#             l1.append(_)
#         else:
#             print('%d' %_ ,'年365天')
#             l2.append(_)
#     for _ in l1[:]:
#         if year==_:
#             print('%d'%year,'年366天')
#             break
#     for _ in l2[:]:
#         if year==_:
#             print('%d'%year,'年365天')
#             break
#numberOfDaysInAYear(year)
###################################################################################################
#7.显示角
# x1,y1,x2,y2=input('(x1,y1,x2,y2)>>').split(',')
# def distance(x1,y1,x2,y2):
#     x1=int(x1)
#     y1=int(y1)
#     x2=int(x2)
#     y2=int(y2)
#     dis1 = math.sqrt((((x1-x2)**2)+((y1-y2)**2)))
#     print(dis1)
# distance(x1,y1,x2,y2)
##################################################################################################
#8.梅森素数
# def jo(A):
#     for i in range(3,A):
#         b = A%i
#         if b==0:
#             return(-1)
#             break
#     else:
#         return A
# for p in range(1,32):
#     A = (2**p)-1
#     s1 = jo(A)
#     if A==s1:
#         print(p,A)
##################################################################################################
#9.时间和日期
# import time
# def t1():
#     print('Current date and time is :',time.asctime(time.localtime(time.time())))
# t1()
##################################################################################################
#10.掷骰子
# def s1():
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     c = a+b
#     if c==7 or c==11:
#         print('you win')
#     elif c==2 or c==3 or c==12:
#         print('you lose')
#     else:
#         print(c)
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     d = a+b
#     if c==d and d!=7:
#         print('you win')
#     else:
#         print('you lose')
# s1()
#################################################################################################
            

