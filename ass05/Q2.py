class class1:
 def __init__(self):
  print("I am Class 1 .")
 def sub_class1(self,b):
  print("Printing from class 1:",b)
class class2(class1):
 def __init__(self):
  print("I am Class 2 .")
 super().__init__()
 def sub_class1(self,b):
  print("Printing from class 2 :", b)
  super().sub_class1(b+1)
class class3(class2):
 def __init__(self):
  print("I am class 3 .")
 super().__init__()
 def sub_class1(self,b):
  print("Printing from class 3:",b)
  super().sub_class1(b+1)
if __name__ == '__main__':
 ob =class3()
 ob.sub_class1(12)