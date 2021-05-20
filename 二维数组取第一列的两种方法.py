#方法1：
list = [['a', 1], ['b', 2], ['c', 3]]
list_first = [iter[0] for iter in list]
print(list_first)
# output:
# ['a', 'b', 'c']

#方法2：
import numpy as np
list_np = np.array(list)
list_first_np = list_np[:, 0]
print(list_first_np)
# output:
# ['a' 'b' 'c']
