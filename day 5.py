# day 5
# strings
# count of alphabets and digits in string
# s=input()
# ca=0
# cd=0
# for char in s:
#     if char.isalpha():
#         ca+=1
#     if char.isdigit():
#         cd+=1
# print(ca,cd)


# count of vowels
# s=input()
# c=0
# v='aeiouAEIOU'
# for char in s:
#     if char in v:
#         c+=1
# print(c)


# count of consonants
# s=input()
# c=0
# v='aeiouAEIOU'
# for char in s:
#     if char not in v:
#         c+=1
# print(c)


# replacing space with hyphen using replace method
# s=input()
# s=s.replace(" ","-")
# print(s)


# # replacing space with hyphen without using replace method
# s=input()
# s1=""
# for char in s:
#     if char.isspace():
#         s1+='-'
#     else:
#         s1+=char
# print(s1)


# capitalizing first letters using title method
# s=input()
# s=s.title()
# print(s)


# capitalizing first letters without using title method
# s=input()
# words=s.split()
# res=''
# for word in words:
#     cap=word[0].upper()+word[1:]
#     res=res+' '+cap
# print(res)


# find length of longest word in sentence
# s=input()
# l=s.split()
# lword=''
# length=0
# for word in l:
#     if len(word)>length:
#         length=(len(word))
#         lword=word
# print(length)
# print(lword)


# reversing a string
# s=input()
# s1=''
# for i in range(len(s)-1,-1,-1):
#     s1+=s[i]
# print(s1)


# palindrome
# s=input()
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


# removing duplicates
# s=input()
# l=' '
# for char in s:
#     if char not in l:
#         l+=char
# print(l)


# most frequent char
# s=input()
# freq={}
# for char in s:
#     if char not in freq:
#         freq[char]=1
#     else:
#         freq[char]+=1
# m=max(freq.values())
# for i in freq:
#     if freq[i]==m:
#         print(i)


# password validator
# s=input()
# final=0
# lc,uc,lwc,dc,spc,cc=1,1,1,1,1,0
# sp_count=0
# l=len(s)
# if not lc>=6 and lc<22:
#     lc=0
# for i in range(len(s)):
#     if s[i].isupper():
#         uc=0
#     if s[i].islower():
#         lwc=0
#     if s[i].isdigit():
#         dc=0
#     if s[i]in "!@#$%^&*":
#         sp_count+=1
#     if sp_count>=2:
#         spc=0
#     if i+1<l and s[i]==s[i+1]:
#         cc=1
# final+=lc+uc+lwc+dc+spc+cc
# print(final)
    

# leetcode problems
# valid anagram
# check if sentence is panagram

s=input()
i,j=0,len(s)-1
while i<j:
    if s[i]==s[j]:
        i+=1
        j+=1
        print("palindrome")
        break
    else:
        print("Not palindrome")
        break