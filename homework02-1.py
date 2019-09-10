#1.一元二次方程
import math
# a,b,c = input('Enter a,b,c:').split(',')
# a=float(a)
# b= float(b)
# c=float(c)
# r1 = ((-b)+(math.sqrt((b*b)-4*a*c)))/(2*a)
# r2 = ((-b)-(math.sqrt((b*b)-4*a*c)))/(2*a)
# r3 = math.sqrt((b*b)-4*a*c)
# if r3 > 0:
#     print('%.6f %.6f' %r1 %r2)
# elif r3 < 0:
#     print('The equation has no real roots')
# else:
#     print(r1)
#####################################################################################################
#2.加法
# import random
# a = random.randint(0,100)
# print(a)
# b = random.randint(0,100)
# print(b)
# S = int(input('两数之和：'))
# sum1 = a+b
# if S==sum1:
#     print(True)
# else:
#     print(False)
####################################################################################################
#3.未来数据
# A = ['monday','tuesday','wednesday','thursday','firday','satuday','sunday']
# TD = int(input('Enter today`s day:'))
# FD = int(input('Enter the number of days elapsed since today:'))
# f = (TD+FD)%7
# print('Today is ' + A[TD] +' and the future day is '+ A[f] )
####################################################################################################
#4.整数排序
# a = int(input('numb1='))
# b = int(input('numb2='))
# c = int(input('numb3='))
# if a<b<c:
#     print(a,b,c)
# elif a<c<b:
#     print(a,c,b)
# elif b<a<c:
#     print(b,a,c)
# elif b<c<a:
#     print(b,c,a)
# elif c<a<b:
#     print(c,a,b)
# elif c<b<a:
#     print(c,b,a)
###################################################################################################
#5.比较价钱
# b1,j1 = input('Enter weight and price for package 1:').split(',')
# b2,j2 = input('Enter weight and price for package 2:').split(',')
# g1 = float(j1)/float(b1)
# g2 = float(j2)/float(b2)
# if g1<g2:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')
###################################################################################################
#6.一个月中天数
# month = int(input('月份：'))
# year = int(input('年份：'))
# T = ['28','29','30','31']
# if year%4==0 and year%100!=0 and month==2:
#     print(year , month ,T[1]  )
# elif month==2:
#     print(year  , month   , T[0]  )    
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
#     print(year ,   month   , T[3]  )
# elif month==4 or month==6 or month==9 or month==11:
#     print(year ,   month   , T[2]  )
##################################################################################################
#7.头或尾
# import random
# choose = input('正or反：')
# s = random.randint(0,1)
# if s==0 and choose=='正':
#     print('正确')
# elif s==0 and choose=='反':
#     print('错误')
# elif s==1 and choose=='反':
#     print('正确')
# elif s==1 and choose=='正':
#     print('错误')
##################################################################################################
#8.剪刀石头布
# import random
# a = int(input('scissor(0),rock(1),paper(2)：'))
# b = random.randint(0,2)
# print(b)
# C = ['scissor','rock','paper']
# if a==b:
#     print("The computer is " +C[b]+ " . You are " +C[a]+ " too . It is a draw.")
# elif a==0 and b==2:
#     print("The computer is " +C[b]+ " . You are " +C[a]+ ". You won.")
# elif a==1 and b==0:
#     print("The computer is " +C[b]+ " . You are " +C[a]+ ". You won.")
# elif a==2 and b==1:
#     print("The computer is " +C[b]+ " . You are " +C[a]+ ". You won.")
# else:
#     print("The computer is " +C[b]+ " . You are " +C[a]+ ". You lose.")
##################################################################################################
#9.一周的星期几
# year = int(input("Enter year:"))
# m = int(input("Enter month:"))
# if m==1:
#     m = 13
#     year -= 1
# else:
#     pass
# if m==2:
#     m=14
#     year -= 1
# else:
#     pass
# q = int(input("Emter the day of the month:1-31:"))
# j = (year/100)//1
# k = year%100
# h = (q+(((26*(m+1)/10))//1)+k+(((k/4))//1)+(((j/4))//1)+(5*j))%7
# h = int(h)
# h1 = ['saturday','sunday','monday','tuesday','wednesday','thursday','firday']
# print('Day of the week is '+h1[h])
#################################################################################################
#10.选牌
# import random
# BS = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
# b = random.randint(0,12)
# color = ['plumblossom','heartwood','diamond','spades']
# c = random.randint(0,3)
# print('The card you picked is the '+BS[b] +' of '+color[c])
#################################################################################################
#11.回文数
# num1 = str(input('Enter a three-digit integer:'))
# if num1[0]==num1[2]:
#     print(num1+' is a palindrome')
# else:
#     print(num1+' is not a palindrome')
#################################################################################################
#12.三角形周长
# x,y,z = input('Enter three edges:').split(',')
# x = int(x)
# y = int(y)
# z = int(z)
# a = x + y
# b = x + z
# c = y + z
# if a > z :
#     print(a+z)
# elif b > y :
#     print(b+y)
# elif c > x :
#     print(c+x)
#################################################################################################




