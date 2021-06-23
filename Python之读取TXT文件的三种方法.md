方法一：

```python
#read txt method one
f = open("./image/abc.txt")
line = f.readline()
while line:
    print line
    line = f.readline()
f.close() 
```


方法二：

```python
#read txt method two
f = open("./image/abc.txt")
for line2 in open("./image/abc.txt"):
    print line2
```


方法三：

```python
#read txt method three
f2 = open("./image/abc.txt","r")
lines = f2.readlines()
for line3 in lines:
    print line3
```

1、如果TXT文件中有两列，可以设定数组，然后分别获取数据

2、上述文件使用的是相对路径，当然也可以使用绝对路径
