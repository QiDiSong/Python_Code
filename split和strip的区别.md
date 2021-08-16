 **[python](http://www.cppcns.com/jiaoben/python/) strip() 函数和 split() 函数的详解及实例**

一直以来都分不清楚strip和split的功能，实际上strip是删除的意思；而split则是分割的意思。因此也表示了这两个功能是完全不一样的，strip可以删除字符串的某些字符，而split则是根据规定的字符将字符串进行分割。下面就详细说一下这两个功能，

**1 Python strip()函数 介绍**

函数原型

声明：s为字符串，rm为要删除的字符序列

s.strip(rm)&nbsp;   删除s字符串中开头、结尾处，位于 rm删除序列的字符

s.lstrip(rm)   删除s字符串中开头处，位于 rm删除序列的字符

s.rstrip(rm)   删除s字符串中结尾处，位于 rm删除序列的字符

**注意：**

（1）当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')

（2）这里的rm删除序列是只要边（开头或结尾）上的字符在删除序列内，就删除掉。

例如，

```
>>> a = ' 123'>>> a' 123'>>> a.strip()'123'
```

（2）这里的rm删除序列是只要边（开头或结尾）上的字符在删除序列内，就删除掉。

例如，



```
>>> a = '123abc'>>> a.strip('21')'3abc'>>> a.strip('12')'3abc'
```

结果是一样的。

2 python split()函数 介绍

说明：

**Python中没有字符类型的说法，只有字符串**，这里所说的字符就是只包含一个字符的字符串！！！

这里这样写的原因只是为了方便理解，仅此而已。

（1）按某一个字符分割，如‘.'

```
>>> str = ('www.google.com')>>> print strwww.google.com>;>> str_split = str.split('.')>>> print str_split['www', 'google', 'com']
```

（2）按某一个字符分割，且分割n次。如按‘.'分割1次

```
>>> str_split = str.split('.',1)>>> print str_split['www', 'google.com']
```

（3）split()函数后面还可以加正则表达式，例如：

```
>>> str_split = str.split('.')[0]>>> print str_splitwww
```

split分隔后是一个列表，[0]表示取其第一个元素；

```
>>> str_split = str.split('.')[::-1]>>> print str_split['com', 'google', 'www']>>> str_split = str.split('.')[::]>>> print str_split['www', 'google', 'com']
```

按反序列排列，[::]安正序排列

```
>>> str = str + '.com.cn'>>;> str'www.google.com.com.cn'>>> str_split = str.split('.')[::-1]>>> print str_split['cn', 'com', 'com', 'google', 'www']>>> str_split = str.split('.')[:-1]>>> print str_split['www', 'google', 'com', 'com']
```

从首个元素开始到次末尾，最后一个元素删除掉。

split()函数典型应用之一，ip数字互换：

\# ip ==> 数字

```
>>> ip2num = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])>>> ip2num('192.168.0.1')3232235521
```

\# 数字 ==> ip # 数字范围[0, 255^4]

```
>>> num2ip = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])>>> num2ip(3232235521)'192.168.0.1' 
```

最后，python怎样将一个整数与IP地址相互转换？

```
>>> import socket>>> import struct>>> int_ip = 123456789>>> socket.inet_ntoa(struct.pack(‘I',socket.htonl(int_ip)))#整数转换为ip地址‘7.91.205.21'>>> str(socket.ntohl(struct.unpack(“I”,socket.inet_aton(“255.255.255.255″))[0]))#ip地址转换为整数‘4294967295'
```

感谢阅读，希望能帮助到大家，谢谢大家对本站的支持！
