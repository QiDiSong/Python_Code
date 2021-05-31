# 当内部作用域想修改外部变量时，需要使用global声明。

counter = 1
def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        counter += 1
doLotsOfStuff()
print counter

# output: 4
