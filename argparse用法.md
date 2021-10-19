# 一、argparse介绍

argparse的官方文档请参考此链接：[官方文档](https://docs.python.org/zh-cn/3/library/argparse.html#argumentparser-objects)
argparse 模块是 Python 内置的一个用于命令项选项与参数解析的模块，argparse 模块可以让人轻松编写用户友好的命令行接口。通过在程序中定义好我们需要的参数，然后 argparse 将会从 sys.argv 解析出这些参数。argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。

# 二、argparse使用——代码示例

A simple demo for argparse.

```python
import argparse

parser = argparse.ArgumentParser(description='test')

parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')

args = parser.parse_args()
print(args.sparse)
print(args.seed)
print(args.epochs)
```

三个步骤：

- 1、创建一个解析器——创建 ArgumentParser() 对象
- 2、添加参数——调用 add_argument() 方法添加参数
- 3、解析参数——使用 parse_args() 解析添加的参数

## 1、创建一个解析器——创建 ArgumentParser() 对象

使用 argparse 的第一步是创建一个 ArgumentParser 对象：

```python
parser = argparse.ArgumentParser(description='test')
```

ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息。

### 描述description

大多数对 ArgumentParser 构造方法的调用都会使用 description= 关键字参数。这个参数简要描述这个程度做什么以及怎么做。在帮助消息中，这个描述会显示在命令行用法字符串和各种参数的帮助消息之间。

## 2、添加参数——调用 add_argument() 方法添加参数

给一个 ArgumentParser 添加程序参数信息是通过调用 add_argument() 方法完成的。通常，这些调用指定 ArgumentParser 如何获取命令行字符串并将其转换为对象。这些信息在 parse_args() 调用时被存储和使用。例如

```python
parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')
123
```

### add_argument() 方法定义如何解析命令行参数

```
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

```
每个参数解释如下:
**`name or flags` - 选项字符串的名字或者列表，例如 foo 或者 -f, --foo。**
**`action` - 命令行遇到参数时的动作，默认值是 store。**
**`store_const`，表示赋值为const；**
`append`，将遇到的值存储成列表，也就是如果参数重复则会保存多个值;
`append_const`，将参数规范中定义的一个值保存到一个列表；
`count`，存储遇到的次数；此外，也可以继承 argparse.Action 自定义参数解析；
`nargs` - 应该读取的命令行参数个数，可以是具体的数字，或者是?号，当不指定值时对于 Positional argument 使用 default，对于 Optional argument 使用 const；或者是 * 号，表示 0 或多个参数；或者是 + 号表示 1 或多个参数。
`const` - action 和 nargs 所需要的常量值。
**`default` - 不指定参数时的默认值。**
**`type` - 命令行参数应该被转换成的类型。**
**`choices` - 参数可允许的值的一个容器。**
`required` - 可选参数是否可以省略 (仅针对可选参数)。
**`help` - 参数的帮助信息，当指定为 argparse.SUPPRESS 时表示不显示该参数的帮助信息.**
`metavar` - 在 usage 说明中的参数名称，对于必选参数默认就是参数名称，对于可选参数默认是全大写的参数名称.
`dest` - 解析后的参数名称，默认情况下，对于可选参数选取最长的名称，中划线转换为下划线.
```



## 3、解析参数——使用 parse_args() 解析添加的参数

ArgumentParser 通过 parse_args() 方法解析参数。它将检查命令行，把每个参数转换为适当的类型然后调用相应的操作。在大多数情况下，这意味着一个简单的 Namespace 对象将从命令行解析出的属性构建：

```python
args = parser.parse_args()
```

在脚本中，通常 parse_args() 会被不带参数调用，而 ArgumentParser 将自动从 sys.argv 中确定命令行参数。

# 三、结果测试

```python
import argparse

parser = argparse.ArgumentParser(description='test')

parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')

args = parser.parse_args()

print(args.sparse)
print(args.seed)
print(args.epochs)
```

显示帮助文档：

![](C:\Users\qidson01\AppData\Roaming\Typora\typora-user-images\image-20211019232412651.png)
输错命令会告诉你usage用法：
![image-20211019232446697](C:\Users\qidson01\AppData\Roaming\Typora\typora-user-images\image-20211019232446697.png)
