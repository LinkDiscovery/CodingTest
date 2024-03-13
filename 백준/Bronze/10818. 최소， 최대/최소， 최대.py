a= int(input())
List = list(map(int,input().split()))

List.sort()
print(f"{List[0]} {List[-1]}")