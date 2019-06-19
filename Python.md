# Python学习

## 统计列表元素的频数

```

def frequency_counter(fc):

    counter = {}

    for item in fc:
  
        if item in counter:
            
            counter[item] += 1
            
        else:
            
            counter[item] = 1
            
    return counter

```
