#1.五边形面积1
import math
# r = float(input('顶点到中心：'))
# s = 2*r*math.sin(math.pi/5) 
# area = (5*s*s)/(4*math.tan(math.pi/5))
# print('The area of the pentagon is %.2f' %area)
############################################################################################
#2.大圆距离
# import math
# x1,y1 = input('Enter point 1 (latitude and longitude) in degress:').split(',')
# x2,y2 = input('Enter point 1 (latitude and longitude) in degress:').split(',')
# x1 = math.radians(float(x1))
# y1 = math.radians(float(y1))
# x2 = math.radians(float(x2))
# y2 = math.radians(float(y2))
# radians = 6371.01
# d = radians * math.acos((math.sin(x1)*math.sin(x2))+(math.cos(x1)*math.cos(x2)*math.cos((y1-y2))))
# print('The distance between the two points is %f km' %d)
#############################################################################################
#3.五角形面积2
# s = float(input('Enter the side:'))
# area = (5*pow(s,2))/(4*math.tan(math.pi/5))
# print('The area of the pentagon is\000' + str(area))
#############################################################################################
#4.正多边形面积
# n = int(input('Enter the number of sides:'))
# s = float(input('Enter the side:'))
# area = (n*pow(s,2))/(4*math.tan(math.pi/n))
# print('The area of the polygon is %f' %area)
##############################################################################################
#5.ASCII码找字符chr()
# a = int(input('Enter an ASCII code:'))
# a= chr(a)
# print('The character is %s' %a)
###############################################################################################
#6.工资表
# name = input('Enter employees name:')
# worktime = input('Enter number of hours worked in a week:')
# money = input('Enter hourly pay rate:')
# bang = input('Enter federal tax withholding rate:')
# zhou = input('Enter state tax withholding rate:')
# name=str(name)
# worktime=float(worktime)
# money=float(money)
# bang=float(bang)
# zhou=float(zhou)
# print('Employee Name:',name)
# print('Hours Worked: %.1f' %worktime)
# print('Pay Rate: $ %.2f' %money)
# print('Gross Pay: $ %.1f' %(money*worktime))
# print("Deductions: " )
# print("\000\000Federal Withholding (20.0%%) : $ %.1f " %(money*worktime*0.2))
# print("\000\000State Withholding (9.0%%): $ %.2f " %(money*worktime*0.09))
# print("\000\000Total Deduction: $ %.2f " %((money*worktime*0.2)+(money*worktime*0.09)))
# print('Net Pay: $ %.2f ' %((money*worktime)-((money*worktime*0.2)+(money*worktime*0.09))))
##################################################################################################
#7.反向数字
# numb1 = int(input('Enter an integer:'))
# numb1 = str(numb1)
# i = numb1[::-1]
# print('The reversed number is ',i)
#################################################################################################
#8.加密文本
# import hashlib
# m = hashlib.md5()
# a = 'qwe123'
# m.update(a.encode(encoding='UTF-8'))
# c = m.hexdigest()
# print(c)
#################################################################################################






