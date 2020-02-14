for i in range(1,9):
    for j in range(-1+i,-1,-1):
        print(format(2**j,"4d"), end=' ')
    print("")



   


# if __name__ == '__main__':
#     L=[]
#     N = int(input())
#     for i in range(N):
#         command=str(input())
#         command=command.split(' ')
#         if command[0]=='insert':
#             L.insert(int(command[1]),int(command[2]))
#         elif command[0]=='print':
#             print(L)
#         elif command[0]=='append':
#             L.append(int(command[1]))
#         elif command[0]=='remove':
#             L.remove(int(command[1]))
#         elif command[0]=='sort':
#             L.sort()
#         elif command[0]=='reverse':
#             L.reverse()
#         elif command[0]=='pop':
#             L.pop()

# s = input()
# 
# vowels = 'AEIOU'
# 
# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#     else:
#         stusc += (len(s)-i)
# 
# if kevsc > stusc:
#     print ("Kevin", kevsc)
# elif kevsc < stusc:
#     print ("Stuart", stusc)
# else:
#     print ("Draw")


# from itertools import product
# 
# A = input().split()
# 
# A = list(map(int, A))
# 
# B = input().split()
# B = list(map(int, B))
# 
# for i in product(A, B):
#     print (i)
    
# from itertools import permutations
# 
# S = input().split()
# p=permutations(S[0], int(S[1]))
# print(type(p))
# for i in sorted(p):
#     print(''.join(i))
    
# from itertools import combinations
# 
# S = input().split()
# for i in range(1, int(S[1]) + 1):
#     for j in combinations(sorted(S[0]), i):
#         print (''.join(j))
    




    
    