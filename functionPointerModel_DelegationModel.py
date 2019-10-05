def fun1():
    print("I am in fun1")
def fun2():
    print("I am in fun2")
def callback(func):
    func()
callback(fun1)
callback(fun2)
# fun1()
# fun2()