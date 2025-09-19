#  day 3
# leetcode problems
#MISSING NUMBER
#LEMONADE CHANGE
#Running sum of 1d array
#Shuffle the array
#Third max num
#Baseball game
#Move zero
#Two sum
#plus one
#remove element
#left and right sum differences
# number of ones in bits
# replace element with greatest element on right side


# bitwise operator
# check even or odd using bitwise operator
# n=int(input("enter number"))
# if n&1==0:
#     print("even")
# else:
#     print("odd")


# swapping numbers using bitwise operator
# a=3
# b=5
# a=a^b
# b=a^b
# a=a^b
# print(a,b)

# finding xor from 1 to N
# def XoR(n):
#     if n%4==1:
#          return 1
#     if n%4==2:
#          return n+1
#     if n%4==3:
#          return 0
#     if n%4==0:
#          return n
# n=int(input("enter number"))
# print(XoR(n))


# left to right range XoR
# def XoR(n):
#     if n%4==1:
#          return 1
#     if n%4==2:
#          return n+1
#     if n%4==3:
#          return 0
#     if n%4==0:
#          return n
# l,r=map(int,input().split())
# a=XoR(r)
# b=XoR(l-1)
# print(a^b)