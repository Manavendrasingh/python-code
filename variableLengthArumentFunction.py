def sum(*args):
    res=0
    if(len(args)!=0):
        for e in args:
            res+=e
    print(res)

sum(1,2,4,6)