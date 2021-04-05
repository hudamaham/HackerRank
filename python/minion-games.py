def minion_game(string):
    # your code goes her
   
    i=0
    l=list()
    le=list()
    while i < len(string):
        if string[i] in 'AEIOU':
            l.append(i)
        else:
            le.append(i)
        i=i+1
    n=len(l)
    for b in l :

        n=n+len(string)-b-1
    nl=len(le)
    for k in le:
        nl=nl+len(string)-k-1

    if(n>nl):
        print('Kevin',n)
    elif (nl>n):
        print('Stuart',nl)
    else:
        print('Draw')

f __name__ == '__main__':
    s = input()
    minion_game(s)