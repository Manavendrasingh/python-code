def isSpecial(myFunc):
    def inner():
        print("I am special")
        myFunc()
    return inner

# def isSpecial(fun1):
#     print("I am special")
#     fun1()
@isSpecial
def ordinary():
    print("I am ordinary")

ordinary()
# isSpecial(ordinary)

