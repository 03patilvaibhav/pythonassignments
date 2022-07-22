import sys
ch=0
my_list = [3,7, 9, 4, 6]
print(my_list)
while ch!=2:
 ch=int(input('1.Input\t\t2.Exit\n'))
 if ch==1:
  i=int(input('Enter Index : '))
 try:
  print(my_list[i])
 except IndexError as e:
  print (e)