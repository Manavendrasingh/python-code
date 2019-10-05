def myMap(callBack,iterable):#single iterator
    list1=[]
    for e in iterable:
        list1.append(callBack(e))
    return list1
def myFilter(callBack,iterable):#single iterator
    list1=[]
    for e in iterable:
        if(callBack(e)):
            list1.append(e)
    return list1

def myMap_Sp(callBack,*iterable):#Multiple iterator
    list1=[]

    for i in range(len(iterable[0])):
        li=[]
        for j in range(len(iterable)):
            li.append(iterable[j][i])
        e1=callBack(*li)
        list1.append(e1)
    return list1

def square(no):
    return no*no
list1=[2,3,5,6]
list2=[3,4,6,8]
# l1=myMap(lambda no:no*no,list1)
# l2=list(map(lambda no:no*no,list1))
l1=myMap_Sp(lambda no1,no2:no1+no2,list1,list2)
l2=list(map(lambda no1,no2:no1+no2,list1,list2))
print("myMap",l1)
print("Map",l2)

