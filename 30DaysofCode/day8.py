# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
dic= dict()
i=0
while(i<n):
    name=input()
    l=name.split()
    dic[l[0]]=l[1]
    i=i+1
p=input()
while (p):
    myValue = dic.get(p, None)
    if myValue:
        s=p+'='+dic[p]
        print(s)
    else:
        print('Not found')
    
    try:
        p=input()
    except:
        p=0
