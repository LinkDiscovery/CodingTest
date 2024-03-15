a , b = map(int,input().split())
c = int(input())

total = a*60+b+c

if total/60 >= 24:
    total -= 24*60
hr = total//60
mi= total%60

print(hr,mi)