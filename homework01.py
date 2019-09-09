#1.摄氏转华氏
# C = float(input('celsius：'))
# F = (9/5)*C + 32
# print(str(C)+' celsius is %.1f fahrenheit' %F)
#########################################################
#2.圆柱体
# import math
# radius = float(input('半径：'))
# length = float(input('高：'))
# pi = math.pi
# area = (radius**2) * pi
# volume = area * length
# print('The area is %.4f' %area) 
# print('The volume is %.1f' %volume)
#########################################################
#3.英尺转米
# feet = float(input('英尺：'))
# meter = feet*0.305
# print(str(feet)+' feet is %.4f meters' %meter)
#########################################################
#4.water energy
# M = float(input('水量：'))
# initialtemperature = float(input('初始温度：'))
# finaltemperature = float(input('最终温度：'))
# Q = M * (finaltemperature - initialtemperature) * 4184
# print('The energy needed is %.1f' %Q)
#########################################################
#5.利息1
# balance,interestrate= input('差额,年利率：').split(',')
# interest = float(balance) * (float(interestrate)/1200)
# print('The interest is %.5f' %interest)
#########################################################
#6.加速度
# v0,v1,t= input('初始速度,末速度,时间：').split(',')
# a = (float(v1) - float(v0))/float(t)
# print('The average acceleration is %.4f' %a)
#########################################################
#7.六月
# amount = int(input('每月存款：'))
# interestrate = 1+0.00417
# month = ['1','2','3','4','5','6','7']
# six = 0
# for m in month: 
#     if int(m) < 7:
#         six = (six+amount)*interestrate
#     else:
#         print('After the sixth mmonth, the account value is %.2f' %six) 
##########################################################
#8.运算
# number = int(input('整数0~1000：'))
# h = number//100
# t = number//10%10
# o = number%10
# S = h+t+o
# print('The sum of the digits is %d' %S)
##########################################################


