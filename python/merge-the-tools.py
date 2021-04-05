def merge_the_tools(string, k):
   
    l=list()
    i=0
    u=''
    while(i<len(string)):
       t=i+k
       u= string[i:t]
       i=i+k
       l.append(u)
    li=list()
    for e in l :
        o=''
        for c in e :
            if(c not in o):
                o=o+c
        li.append(o)
    for e in li :
        print (e)
        
   
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)