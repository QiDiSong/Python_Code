## 方式1：

```
from builtins import str
import os
def getCommitID():
    cmd = 'git rev-parse HEAD'
    work_dir = os.getcwd() # 获取当前路径
    os.chdir(work_dir)
    result = os.popen(cmd)  # 执行输入的命令
    commitID = result.read()
```

运行结果：

```
b54bc2a14730c42119ab78fe85786d0af45f51fa
```

## 方式2：

```
cmd = 'git rev-parse HEAD'
work_dir = os.getcwd() # 获取当前路径
listdir = os.listdir(work_dir) # 返回path指定的文件夹包含的文件或文件夹的名字的列表
for dirName in listdir:
    file_path = os.path.join(work_dir, dirName)  # 拼接完整的路径
    print(file_path)
    if os.path.isdir(file_path):  # 判断是否是目录
        try:
            os.chdir(file_path)  # 移动到制定的目录下
            result = os.popen(cmd)  # 执行输入的命令
            print(result.read())  # 打印命令执行的结果
        except:
            print()
        finally:
            print()
```

运行结果：

```
D:\master\tools\camera
b54bc2a14730c42119ab78fe85786d0af45f51fa

D:\master\tools\getClick.py

D:\master\tools\radar
b54bc2a14730c42119ab78fe85786d0af45f51fa
```

