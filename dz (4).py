#0. Создать список с числами(От 1 до 40 идут не по порядку).
#списак 1
nambers = [15,34,19,32,37,29,27,36,21,25,7,33,38,11,16,5,22,6,18,1,12,40,3,2,31,26,35,9,20,23,28,24,13,30,17,39,4,8,14,10]
r = 0
nambers2 = [15,34,19,32,37,29,27,36,21,25,7,33,38,11,16,5,22,6,18,1,12,40,3,2,31,26,35,9,20,23,28,24,13,30,17,39,4,8,14,10]
r2 = 0


#1. Написать программу, которая будет выводить числа которые больше 15 но меньше 25"
print('#1\n')
while r <= 39:
  if nambers[r] > 15 and nambers[r] < 25:
    print(nambers[r])
    r = (r + 1)
  else:
    r = (r + 1)


#2. Написать программу, которая будет выводить числа которые меньше 15 или больше 25"		
print('\n\n\n#2\n')
while r2 <= 39:
  if nambers2[r2] < 15 or nambers2[r2] > 25:
    print(nambers2[r2])
    r2 = (r2 + 1)
  else:
    r2 = (r2 + 1)  
		
































































































































































































































































































































































































































































































































































































































#from colorama import Fore, Back, Style
#0. Создать список с числами(От 1 до 40 идут не по порядку).
#списак 1
#nambers = [15,34,19,32,37,29,27,36,21,25,7,33,38,11,16,5,22,6,18,1,12,40,3,2,31,26,35,9,20,23,28,24,13,30,17,39,4,8,14,10]
#r = 0
#списак 2
#nambers2 = [15,34,19,32,37,29,27,36,21,25,7,33,38,11,16,5,22,6,18,1,12,40,3,2,31,26,35,9,20,23,28,24,13,30,17,39,4,8,14,10]
#r2 = 0

#1. Написать программу, которая будет выводить числа которые больше 15 но меньше 25"
#print(Fore.GREEN + '#1 больше 15 но меньше 25\n' + Fore.RESET)
#while r <= 39:
 # if nambers[r] > 15 and nambers[r] < 25:
 #   print(Fore.YELLOW + str(nambers[r]) + Fore.RESET)
 #   r = (r + 1)
 # else:
 #   r = (r + 1)


#2. Написать программу, которая будет выводить числа которые меньше 15 или больше 25"		
#print(Fore.GREEN + '\n\n\n#2 меньше 15 или больше 25\n' + Fore.RESET)
#while r2 <= 39:
 # if nambers2[r2] < 15 or nambers2[r2] > 25:
 #   print(Fore.YELLOW + str(nambers2[r2]) + Fore.RESET)
 #   r2 = (r2 + 1)
 # else:
#    r2 = (r2 + 1)  
		










