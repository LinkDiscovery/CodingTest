a = int(input())

for i in range(a):
    num,word = input().split()
    num = int(num)
    for i in word:
        print(num*i,end='')
    print()