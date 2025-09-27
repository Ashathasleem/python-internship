# reduce number to 1 using recursion
# def fun(n):
#     if n==1:
#         return 0
#     elif n%2==0:
#         return 1+fun(n//2)
#     else:
#         return 1+min(fun(n-1),fun(n+1))
# n=int(input())
# print(fun(n))


# stack
# stack=[]
# stack.append(3)
# stack.append(5)
# stack.append(6)
# stack.append(9)
# stack.append(1)
# stack.pop()
# print(stack)


s='ab*c**def'
stack=[]
for i in s:
    if i!='*':
        stack.append(i)
    else:
        stack.pop()
x="".join(stack)
print(x)