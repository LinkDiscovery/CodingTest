n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

count = 0
for a in n_list :
	if v == a:
	 count += 1
	 
print(count)