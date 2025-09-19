# buzz number
# n=int(input("enter number"))
# n1=n//10
# n2=n%10
# if n1==n2:
#  print("yes")
# else:
#  print("no")


# elephant
# x=int(input("enter steps"))
# if (x%5==0):
#      print(x//5)
# else:
#     print(x//5+1)


# fizzbuzz
# n=int(input("enter number"))
# if n%3==0 and n%5==0:
#     print("Fizzbuzz number")
# elif n%5==0:
#     print("Buzz number")
# elif n%3==0:
#     print("Fizz number")


# watermelon
# if (w%2==0 and w>2):
#     x=w//2
#     if x%2==0:
#         print(x,x)
#     else:
#         print(x-1,x+1)
# else:
#     print("no")


# to find even or odd
# n=int(input("enter number"))
# if (n%2==0):
#     print("even")
# else:
#     print("odd")


# to find greatest of three
# a,b,c=map(int,input().split(","))
# if a>b and a>c:
#     print("a")
# elif b>=c:
#     print("b")
# else:
#     print("c")


# to check the age for movie
# age=int(input("enter the age"))
# if age>18:
#     print("allowed")
#     if age>=75:
#         print("risky")
#     elif age>=40:
#         print("panic attack")
#     elif age>=25:
#         print("dont scream")
#     else:
#         print("enjoy")
# else:
#     print("your not allowed")

 
# to print even numbers from 50-100
# for i in range(50,101,2):
#     print(i,end=" ")
# for i in range(50,101):
#     if i%2==0:
#         print(i,end=" ")


# to check number is prime or not
# n=int(input("enter number"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")


# to get count of prime numbers between 5-15
# def isprime(n):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             return False
#     return True
# l=int(input())
# r=int(input())
# c=0
# for i in range(l,r+1):
#     if isprime(i):
#         c+=1
# print(c)

# to count given numbers
# n=int(input("enter number"))
# count=0
# while n!=0:
#     count+=1
#     n=n//10
# print(count)


# to find sum of given number
# n=int(input("enter number"))
# sum=0
# while n!=0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# print(sum)

# to find reverse of numbers
# n=int(input("enter number"))
# rev=0
# while n!=0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# print(rev)

# to find number of years for limak has more weight than bob
# limak,bob=map(int,input().split())
# year=0
# while limak<=bob:
#     limak*=3
#     bob*=2
#     year+=1
# print(year)

# to check googly number
# n=int(input("enter number"))
# sum=0
# while n!=0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# flag=0
# for i in range(2,sum):
#     if sum%i==0:
#         flag+=1
# if flag==0:
#     print("Googly")
# else:
#     print("Not Googly")


# to check armstrong number
# n=int(input("enter number"))
# temp1=n
# temp2=n
# count=0
# while temp1>0:
#     count+=1
#     temp1=temp1//10
# print(count)
# arm=0
# while temp2>0:
#     d=temp2%10
#     arm=arm+d**count
#     temp2=temp2//10
# if arm==n:
#     print("armstrong number")
# else:
#     print("not armstrong number")

# to check neon number
# n=int(input("enter number"))
# x=n*n
# sum=0
# while x>0:
#     d=x%10
#     sum=sum+d
#     x=x//10
# if sum==n:
#     print("neon number")
# else:
#     print("not neon number")


# to check magic number
# n=int(input("enter number"))
# while n>9:
#     sum=0
#     while n>0:
#         d=n%10
#         sum+=d
#         n//=10
#     n=sum
# if n==1:
#     print("magic number")
# else:
#     print("not magic number")

# to find composite numbers
# n=int(input("enter number"))
# if n<=1:
#     print("not composite")
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")
#         c+=1
# if c>2:
#     print("composite")
# else:
#     print("not composite")

# to find perfect number
# n=int(input("enter number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if n==sum:
#     print("perfect number")
# else:
#     print("not perfect number")

# to find niven number
# n=int(input("enter number"))
# sum=0
# while n>0:
#     d=n%10
#     sum+=d
#     n//=10
# if n%sum==0:
#     print("niven number")
# else:
#     print("not niven number")

# to find strong number
# n=int(input("enter number"))
# org_n=n
# fact=1
# sum=0
# while n>0:
#     d=n%10
#     for i in range(1,d+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
#     fact=1
# if org_n==sum:
#     print("strong number")
# else:
#     print("not strong number")

# finding spy number
# n=int(input("enter number"))
# sum=0
# mul=1
# while n>0:
#     d=n%10
#     sum+=d
#     mul*=d
#     n=n//10
# if sum==mul:
#     print("spy number")
# else:
#     print("not spy number")