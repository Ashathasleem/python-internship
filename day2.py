
# Day2
# merging and sorting of list
# L1=list(map(int,input("enter list elements:").split()))
# L2=list(map(int,input("enter list elements:").split()))
# L=L1+L2
# L.sort()
# print(L)

# swapping
# l1=list(map(int,input("enter list elements:").split()))
# l1[0],l1[-1]=l1[-1],l1[0]
# print(l1)

# removing duplicate elements
# l=list(map(int,input("enter list elements:").split()))
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# elements occurred odd number times
# l=list(map(int,input("enter list elements:").split()))
# l1=[]
# for i in l:
#     if l.count(i)%2!=0 and i not in l1:
#         l1.append(i)
# print(l1)


# sum of three min elements
# l=list(map(int,input("enter list elements:").split()))
# l.sort()
# print(sum(l[:3]))

# even num from desc to asc and odd num from asc to desc
# l=list(map(int,input("enter list elements:").split()))
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# even.sort(reverse=True)
# odd.sort()
# res=even+odd
# print(res)

# even and odd in single list
# l=list(map(int,input("enter list elements:").split()))
# l.sort()
# l1=[]
# for i in l:
#     if i%2!=0:
#         l1.insert(0,i)
#     else:
#         l1.append(i)
# l1.reverse()
# print(l1)

# police recruit
# l=[1,-1,1,-1,-1,1,1,1]
# p=0
# unsolved=0
# for i in l:
#     if i==-1:
#        if p>0:
#           p-=1
#        else:
#            unsolved+=1
#     else:
#         p+=i
# print(unsolved)