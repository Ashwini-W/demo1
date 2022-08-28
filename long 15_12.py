



############


# 19/!2/21

# Q3
# try:
#     t=int(input())
#     for i in range(t):
#         n=int(input())
#         a=1
#         for i in range(2,n):
#             if (n%i==1):
#                 a=a+1
#         print(a)

# except:
#     pass

# import math
# try:
#     t=int(input())
#     for i in range(t):
#         n=int(input())
#         a=2
#         x=int(math.sqrt(n)+1)
#         print(x)
#         for i in range(2,x):
#             if (n%i==1):
#                 a=a+1
#         print(a)

# except:
#     pass


# import math
# try:
#     t=int(input())
#     for i in range(t):
#         n=int(input())
#         cnt=0
#         for i in range(1,n):
#             if (i*i<n):
#                 if (n % i == 0):
#                     cnt += 2         
#             else:
#                 break
#         if(math.pow(math.sqrt(n),2)==n):
#             cnt+=1
#         print(cnt)

# except:
#     pass




import math
try:
    t=int(input())
    for i in range(t):
        n=int(input())
        x=int(math.ceil(math.sqrt(n)))
        print('x',x)
        cnt=0
        for i in range(1,x):
            print(i)
            if(n%i==0):
                print('a')
                if(n//i==i):
                    print('b')
                    cnt=cnt+2
                else:
                    print('c')
                    cnt=cnt+1
        print(cnt)

except:
    pass







# Q1
# div 3
# try:
#     t=int(input())
#     for i in range(t):
#         x1,y1,x2,y2= list(map(str,input().split()))
#         if (x1==x2) or (y1==y2):
#            print('Yes')
#         else:
#             print('No')
# except:
#     pass






#15_!2
# Q1
# try:
#     x,y=list(map(str,input().split()))
#     # R>B>G
#     if ((x or y) =='R'):
#         print('R')
#     elif (x =='G' and y =='B') or (x =='B' and y=='G'):
#         print('B')
#     elif(x==y):
#         print(x)
        
# except:
#     pass



# # Q2
# try:
#     t=int(input())
#     for i in range(t):
#         n=int(input())
#         if n%2==0:
#             p=''
#             for i in range(n/2):
#                 p+='10'
#             print(p)
#         else:
#             print('-1')
        
# except:
#     pass




# Q1
# try:
#     t=int(input())
#     for i in range(t):
#         f,s,t=list(map(str,input().split()))
#         x,y=list(map(str,input().split()))
    
#         if (x==f or y==f):
            
#             print(f)
#         else:
#             print(s)
        
# except:
#     pass



# # Q2
# import collections
# try:
#     t=int(input())
#     for i in range(t):
#         N=int(input())
#         lst_=list(map(int,input().split()))
#         elements_count = collections.Counter(lst_)
#         # for key,value in elements_count.items():
#         print(elements_count.most_common())
#         k=elements_count.most_common(1)
#         print(k)
#         max_key = max(elements_count, key=elements_count.get)
#         print(max_key)
#         #OR to find the key of the maximum value in counter
#         # maxkey = max(zip(elements_count.values(), elements_count.keys()))[1]
#         # print(maxkey)
#         max_val=max(elements_count.values())  #max_freq
#         print(max_val)

#         ans =-10
#         if (N==1 or max_val==N):
#             ans=0
#         elif (max_val==1):
#             ans=-1
#         else:
#             ans=(N-max_val)+1
#         print(ans)
# except:
#     pass