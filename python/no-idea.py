numbers=input().split()

mylist=input().split()
A=set(input().split())
B=set(input().split())

print(sum( [1 if e in A else -1 if e in B else 0  for e in mylist] ))