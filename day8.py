# OOPs concepts
# class bikes:
#     def perf(self):
#         print("gt","650cc",15,4)
# gt=bikes()
# duke=bikes()
# gt.perf()
# duke.perf()

# example for encapsulation
# class bikes:
#     def __init__(self,name,cc,m,cost):
#         self.name=name
#         self.cc=cc
#         self.m=m
#         self.cost=cost
#     def performance(self):
#         print("abt bikes:",self.name,self.cc,self.m,self.cost)
# gt=bikes("GT",650,12,4)
# duke=bikes("duke",390,30,2)
# gt.performance()
# duke.performance()
        
#  example for static variables       # 
# class bikes:
#     wheels=2
#     handle=1
#     mirror=2
#     def __init__(self,name,cc,m,cost):
#         self.name=name
#         self.cc=cc
#         self.m=m
#         self.cost=cost
#     def performance(self):
#         print("abt bikes:",self.name,self.cc,self.m,self.cost)
# gt=bikes("GT",650,12,4)
# duke=bikes("duke",390,30,2)
# gt.performance()
# duke.performance() 
# print(gt.wheels)
# print(duke.handle)       

# exapmle for instance,static variables and instance,static,class methods
# class cars:
#     wheels=4
#     def __init__(self,mil,car):
#         self.mil=mil
#         self.car=car
#     def get_mil(self):
#         return c1.mil
#     def set_mil(self):
#         c1.mil=12
#     @staticmethod
#     def info():
#         print("hi hello")
#     @classmethod
#     def infor(cls):
#         return cls.wheels
# print(cars.infor())
# c1=cars(10,"BMW")
# c2=cars(15,"audi")
# c1.wheels=9
# print(c1.mil)
# print(c1.wheels)
# print(c2.wheels)
# print(c1.get_mil())
# print(c1.set_mil())
# print(c1.mil)
# print()
    
# example for duck typing
# class pycharm:
#     def execute(self):
#         print("compiling")
#         print("running")
# class myeditor:
#     def execute(self):
#         print("debugging")
#         print("printing error")
#         print("compiling")
#         print("running")
# class laptop:
#     def code(self,ide):
#         ide.execute()
# ide=myeditor()
# lap1=laptop()
# lap1.code(ide)

# a=4
# b=6
# print(a+b)
# print(int.__add__(a,b))


# magic method
# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self,other):
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         s3=Student(m1,m2)
#         return s3
#     def __gt__(self,other):
#         r1=self.m1+self.m2
#         r2=other.m1+other.m2
#         if r1>r2:
#             return True
#         else:
#             return False
# s1=Student(59,65)
# s2=Student(67,85)
# s3=s1+s2
# print(s3.m1)
# print(s3.m2)
# if s1>s2:
#     print("s1 is having more marks then s2")
# else:
#     print("s2 is having more marks then s1")


# example for method overloading
# class math:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
# m=math()
# print(m.add(1,2))
# print(m.add(1,2,3))
# print(m.add())


# inheritance
# class Animal:
#     def sound(self):
#         return "Animals make different sound"
# class Dog(Animal):
#     def sound(self):
#         return "Dog barks"
# d=Dog()
# print(d.sound())


# multiple inheritance
# class engine:
#     def engine_info(self):
#         return "this is an engine"
# class wheels:
#     def wheels_info(self):
#         return "car has 4 wheels"
# class car(engine,wheels):
#     def car_info(self):
#         return "this is a car"
# c=car()
# print(c.engine_info())
# print(c.wheels_info())
# print(c.car_info())


# multilevel inheritance
# class Animal:
#     def species(self):
#         return "this is an animal"
# class Mammal(Animal):
#     def category(self):
#         return "this is a mammal"
# class Human(Mammal):
#     def speak(self):
#         return "Humans can speak"
# h=Human()
# print(h.species())
# print(h.category())
# print(h.speak())


# hierarchical inheriance
# class vehicle:
#     def fuel_type(self):
#         return "vehicles can use petrol,disel and LPG"
# class car(vehicle):
#     def type(self):
#         return "car is a 4-wheeler"
# class bike(vehicle):
#     def type(self):
#         return "bike is a 2 wheeler"
# c=car()
# b=bike()
# print(c.fuel_type())
# print(c.type())
# print(b.type())


# hybrid inheritance
# class Animal:
#     def sound(self):
#         return "Animals make different sound"
# class Dog(Animal):
#     def sound(self):
#         return "Dog barks"
# class Cat(Animal):
#     def ssound(self):
#         return "cat meows"
# class Rat(Dog,Cat):
#     def sound(self):
#         return "rat bites"
# a=Animal()
# print(a.sound())
# d=Dog()
# print(d.sound())
# c=Cat()
# print(c.sound())
# r=Rat()
# print(r.sound())


# linear search
# arr=[7,5,1,3,8,9,2,6]
# key=2
# for i in range(len(arr)):
#     if (arr[i]==key):
#         print("key found")
#         break
    

# binary search
# arr=[1,2,3,5,8,10,11,12]
# key=2
# low=0
# high=len(arr)-1
# result=-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==key:
#         result=mid
#         break
#     elif arr[mid]<key:
#         low=mid+1
#     else:
#         high=mid-1
# print(result)


# finding first occurences using binary search
# arr=[1,2,2,3,3,5,6,7,8]
# key=3
# low=0
# high=len(arr)-1
# result=-1
# while (low<=high):
#     mid=(low+high)//2
#     if key==arr[mid]:
#         result=mid
#         high=mid-1
#     elif key<arr[mid]:
#         high=mid-1
#     else:
#         low=mid+1
# print(result)

# finding last occurences using binary search
# arr=[1,2,2,3,3,5,6,7,8]
# key=3
# low=0
# high=len(arr)-1
# result=-1
# while (low<=high):
#     mid=(low+high)//2
#     if key==arr[mid]:
#         result=mid
#         low=mid+1
#     elif key<arr[mid]:
#         high=mid-1
#     else:
#         low=mid+1
# print(result)


# find the minimum number from rotated sorted array
# arr=[5,6,7,0,1,2,3]
# low=0
# high=len(arr)-1
# while(low<high):
#     mid=(low+high)//2
#     if arr[mid]>arr[high]:
#         low=mid+1
#     else:
#         high=mid
# print(arr[low])


# finding peak value 
# arr=[1,2,3,1]
# low=0
# high=len(arr)-1
# while(low<high):
#     mid=(low+high)//2
#     if arr[mid]<arr[mid+1]:
#         low=mid+1
#     else:
#         high=mid
# print(arr[low])


n=16
low,high=0,n
result=0
while low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        result=mid
        low=mid+1
    else:
        high=mid-1
print(result)