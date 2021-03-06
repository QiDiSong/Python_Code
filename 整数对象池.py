a = [1, 2, 3]
b = [1, 2, 4]
print(id(a[0]) == id(b[0]))        # --->True
print((a[1]) is (b[1]))            # --->True

'''
id（object）是python的一个函数用于返回object的内存地址。但值得注意的是，python 为了提高内存利用效率会对一些简单的对象（如数值较小的int型对象，字符串等）采用重用对象内存的办法。
对于python而言，这些int类型的数据存储在一块区域内，任何形式的使用，都是从该区域内取数据

1、is 比较两个对象的 id 值是否相等，是否指向同一个内存地址；
2、== 比较的是两个对象的内容是否相等，值是否相等
在python3.6中对于小整数对象有一个小整数对象池，范围不止在[-5,257）之间。我试了百万以上的数地址都是相同的
'''
