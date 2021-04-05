# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(input())
k=0
l=list()
while(k<i):
    l.append(input())
    k=k+1

fin=list()
for e in l :
    t=0
    odd=''
    even=''
    while(t<len(e)):
        if(t%2==0):
            odd=odd+e[t]
        else:
            even=even+e[t]
         
        t=t+1
        
    s=odd+' '+even
  
    fin.append(s)
for e in fin :
    print(e)
