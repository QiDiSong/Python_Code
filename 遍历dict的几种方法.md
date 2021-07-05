<u>（1）遍历key值</u>

\>>> a
{'a': '1', 'b': '2', 'c': '3'}
\>>> **for key in a:**
print(key+':'+a[key])

a:1
b:2
c:3
\>>> **for key in a.keys():**
print(key+':'+a[key])

a:1
b:2
c:3



**在使用上，for key in a和 for key in a.keys():完全等价。**

<u>（2）遍历value值</u>

\>>> **for value in a.values():**
print(value)

1
2
3

<u>（3）遍历字典项</u>

\>>> for kv in a.items():
print(kv)

('a', '1')
('b', '2')
('c', '3')

<u>（4）遍历字典健值</u>



\>>> **for key,value in a.items():**
print(key+':'+value)

a:1
b:2
c:3
\>>> **for (key,value) in a.items():**
print(key+':'+value)

a:1
b:2
c:3
