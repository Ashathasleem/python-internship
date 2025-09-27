# leetcode problems
# valid palindrome||
# reversing vowels of string


# find length of longest word in palindrome
# s="abba"
# m=0
# for c in range(len(s)):
#     l,r=c,c
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         m=max(m,r-l+1)
#         l-=1
#         r+=1
#     l,r=c,c+1
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         m=max(m,r-l+1)
#         l-=1
#         r+=1
# print(m)


# Functions
# def qwer():
#     print("hi")
# def asd():
#     print("hello")
#     qwer()
# qwer()
# print(2)


#required arguments
# def qwer(x,y):
#     print("hi",x,y)
# qwer(10,20) 

# def qwer(x):
#     print(x,"hi")
#     return 30
# c=qwer(10)+600
# print(c)
    
# variable number of arguments
# def qwer(y,z,*x):
#     print(x,"hey",y,z)
# qwer(3,5,6,1,2,8)

# def qwer(x):
#     if (x==6):
#         return
#     print(x)
#     qwer(x+1)
# qwer(1)

# to find square of number
# def sq(n):
#     return n*n
# n=int(input())
# res=sq(n)
# print(res)

# lambda function
# s=lambda n:n*n
# n=int(input())
# res=s(n)
# print(res)

# f=lambda a,b:a+b
# n=int(input())
# m=int(input())
# res=f(n,m)
# print(res)

# filtering even numbers 
# def even(n):
#     return n%2==0
# nums=[1,2,3,4,5,6,7]
# evens=list(filter(even,nums))
# print(evens)

# filtering even numbers using lambda
# nums=[1,2,3,4,5,6,7,8]
# evens=list(filter(lambda n:n%2==0,nums))
# print(evens)

# def update(n):
#     return n*2
# nums=[1,2,3,4,5,6,7,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# doubles=list(map(lambda n:n*2,evens))
# print(doubles)

# using lambda
# nums=[1,2,3,4,5,6,7,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# doubles=list(map(lambda n:n*2,evens))
# print(doubles)

# from functools import reduce
# nums=[1,2,3,4,5,6,7,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# doubles=list(map(lambda n:n*2,evens))
# num=reduce(lambda a,b:a+b,doubles)
# print(doubles)
# print(num)

#  to check googly number using functions
# def is_googly_number(num):
#     reversed_num = int(str(num)[::-1])
#     if reversed_num == num + 1:
#         return True
#     else:
#         return False
# num = int(input("Enter a number: "))
# if is_googly_number(num):
#     print(f"{num} is  not a googly number.")
# else:
#     print(f"{num} is  a googly number.")             


# tail recursion
# def nums(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     nums(n-1)
# n=int(input())
# nums(n)  


# head recursion
# def nums(n):
#     if n==0:
#         return
#     nums(n-1)
#     print(n,end=" ")
# n=int(input())
# nums(n)


# print 543212345 if input is 5
# def nums(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     nums(n-1)
#     if n!=1:
#         print(n,end=" ")
# n=int(input())
# nums(n)


# factorial using recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fact(n-1)*n
# n=int(input())
# print(fact(n))


# palindrome of numbers using recursion
# def is_palindrome(n,rev=0,temp=None):
#     if temp is None:
#         temp=n
#     if n==0:
#         return temp==rev
#     return is_palindrome(n//10,rev*10+n%10,temp)
# num=int(input())
# print(is_palindrome(num))


# reversing integers using recursion
# def rev_num(n,rev=0):
#     if n==0:
#         return rev
#     return rev_num(n//10,rev*10+n%10)
# num=int(input())
# print(rev_num(num))


# check if number is perfect square using recursion
# def perfect_square(n):
#     if n<0:
#         return False
#     root=int(n**0.5)
#     return n==root*root
# n=int(input())
# print(perfect_square(n))


# checking power of two using recursion
# def power_of_two(n):
#     if n==1:
#         return True
#     if n==0 or n%2!=0:
#         return False
#     return power_of_two(n//2)
# n=int(input())
# print(power_of_two(n))


# finding power of two numbers
# def power(a,b):
#     if b==0:
#         return 1
#     return a*power(a,b-1)
# num1=int(input())
# num2=int(input())
# print(power(num1,num2))


