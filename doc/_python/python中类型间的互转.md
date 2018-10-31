# python中类型间的互转
>因为在这学期使用python进行开发，每次语法都需要在需要时查找并且每次发现有很多都是之前找过的，所以想把每次找过的内容进行一次整理.

### 转bytes(字节流)
1. list,tuple,dict,set -> bytes
使用numpy.ndarray.tobytes函数
```
x = [1,2,3,4]
aims = np.ndarray.tobytes(np.array(x))   #先将其转为numpy.array,在转为bytes
```
2. str -> bytes
```
'中国'.encode()                   # b'\xe4\xb8\xad\xe5\x9b\xbd'
bytes('中国', encoding='utf-8')   # b'\xe4\xb8\xad\xe5\x9b\xbd'
```

3. 更多单个类型转bytes

[Python中对字节流/二进制流的操作:struct模块简易使用教程](https://www.jianshu.com/p/5a985f29fa81)

### 转int
仅float,str,bytes支持转int
1. float --> int 
去掉小数点及后面的数值，仅保留整数部分
```
int(-12.94)       #-12
```
2. str --> int 
如果有数字(0-9)和正负号(+/-)以外的字符，就会报错
```
int("+1209)    #1209
```
3. bytes --> int
如果 bytes 中有数字(0-9)和正负号(+/-)以外的字符，就会报错。
```
int(b'1209')         #1209
```

### 转float
支持转换为 float 类型的，仅有 int、str、bytes，其他类型均不支持。
1. int --> float
int 转换为 float 时，会自动给添加一位小数。
```
float(-1209)     # -1209.0
```
2. str -> float
如果字符串含有正负号(+/-)、数字(0-9)和小数点(.)以外的字符，则不支转换。
```
float('-1209')          # -1209.0
float('-0120.29023')    # -120.29023
```
3. bytes -> float
如果 bytes 中含有正负号(+/-)、数字(0-9)和小数点(.)以外的字符，则支持转换。
```
float(b'-1209')         # -1209.0
float(b'-0120.29023')   # -120.29023
```

### 转complex(复数)
仅支持 int、float、str 转换成 complex 类型。
1. int -> complex
int 转换 complex 时，会自动添加虚数部分并以0j表示。
```
complex(12)         # (12+0j)
```
2. float -> complex
float 转换 complex 时，会自动添加虚数部分并以0j表示。
```
complex(-12.09)     # (-12.09+0j)
```
3. str -> complex
str 转换 complex 时，如果能转换成 int 或 float，则会转换后再转为 complex。如果字符串完全符合 complex 表达式规则，也可以转换complex 类型值。
```
complex('-12.09')       # (-12.09+0j)
complex('-12.0')        # (-12+0j)，去除了小数部分
complex('-12')          # (-12+0j)
complex('-12+9j')       # (-12+9j)
complex('(-12+9j)')     # (-12+9j)
complex('-12.0-2.0j')   # (-12-2j)，去除了小数部分
complex('-12.0-2.09j')  # (-12-2.09j)
complex(b'12')          # 报错，不支持 bytes 转换为 complex
complex('12 + 9j')      # 报错，加号两侧不可有空格
```

### 转str
str() 函数可以将任意对象转换为字符串
1. float,int,complex 转 str
```
str(12)     # 12
str(-12.90)     # -12.9
str(complex(12 + 9j))   # (12+9j)
str(complex(12, 9))     # (12+9j)
```
2. bytes 转 str()

```
str(b'hello world')        # b'hello world'

b'hello world'.decode()                             # hello world
str(b'hello world', encoding='utf-8')               # hello world
str(b'\xe4\xb8\xad\xe5\x9b\xbd', encoding='utf-8')  # 中国
```
3. list,tuple,dict,set -> str

会先将值格式化为标准的对应类型的表达式，然后再转换为字符串。
```
str([])                      # []
str([1, 2, 3])              # [1, 2, 3]
''.join(['a', 'b', 'c'])    # abc

str(())                     # ()
str((1, 2, 3))              # (1, 2, 3)
''.join(('a', 'b', 'c'))    # abc

str({'name': 'hello', 'age': 18})       # {'name': 'hello', 'age': 18}
str({})                                 # {}
''.join({'name': 'hello', 'age': 18})   # nameage

str(set({}))                # set()
str({1, 2, 3})              # {1, 2, 3}
''.join({'a', 'b', 'c'})    # abc
```

### 转list
支持转换为 list 的类型，只能是序列，比如：str、tuple、dict、set等。
1. str,tuple,set  -> list

```
list('123abc')      # ['1', '2', '3', 'a', 'b', 'c']
list((1, 2, 3))     # [1, 2, 3]
list({1, 2, 3, 3, 2, 1})    # [1, 2, 3]
```
2. bytes -> list

bytes 转换列表，会取每个字节的 ASCII 十进制值并组合成列表
```
list(b'hello')      # [104, 101, 108, 108, 111]
```
3. dict -> list

字典转换列表，会取键名作为列表的值。
```
list({'name': 'hello', 'age': 18})  # ['name', 'age']
```

### 转tuple
与list一样
```
tuple('中国人')    # ('中', '国', '人')
tuple(b'hello')     # (104, 101, 108, 108, 111)
tuple([1, 2, 3])    # (1, 2, 3)
tuple({'name': 'hello', 'age': 18})     # ('name', 'age')
tuple({1, 2, 3, 3, 2, 1})       # (1, 2, 3)

```
### 转dict
1. str -> dict
    * 使用 json 模块

    >使用 json 模块转换 JSON 字符串为字典时，需要求完全符合 JSON 规范，尤其注意键和值只能由单引号包裹，否则会报错。

    ```
    import json
    
    user_info = '{"name": "john", "gender": "male", "age": 28}'
    print(json.loads(user_info))
     # {'name': 'john', 'gender': 'male', 'age': 28}
    ```

    * 使用 eval 函数

    >因为 eval 函数能执行任何符合语法的表达式字符串，所以存在严重的安全问题，不建议。
    ```
    user_info = "{'name': 'john', 'gender': 'male', 'age': 28}"
    print(eval(user_info))
    
    # {'name': 'john', 'gender': 'male', 'age': 28}
    ```
    * 使用 ast.literal_eval 方法

    >使用 ast.literal_eval 进行转换既不存在使用 json 进行转换的问题，也不存在使用 eval 进行转换的 安全性问题，因此推荐使用 ast.literal_eval。
    ```
    import ast
    
    user_info = "{'name': 'john', 'gender': 'male', 'age': 28}"
    user_dict = ast.literal_eval(user_info)
    print(user_dict)
    
    # {'name': 'john', 'gender': 'male', 'age': 28}
    ```
2. list -> dict
通过 zip 将 2 个列表映射为字典：

```
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
print(dict(zip(list1, list2)))
# {1: 1, 2: 2, 3: 3}
```

将嵌套的列表转换为字典：
```
li = [
    [1, 111],
    [2, 222],
    [3, 333],
]
print(dict(li))
# {1: 111, 2: 222, 3: 333}
```
3. tuple -> dict
**同list转dict**

4. set -> dict

通过 zip 将 2 个集合映射为字典：
```
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
print(dict(zip(set1, set2)))
# {1: 'c', 2: 'a', 3: 'b'}
```

### 转set
1. str,bytes,list,tuple -> set

```
print(set('hello'))     # {'l', 'o', 'e', 'h'}
set(b'hello')           # {104, 108, 101, 111}
set([1, 2, 3, 2, 1])    # {1, 2, 3}
set((1, 2, 3, 2, 1))    # {1, 2, 3}
```

2. dict -> set
```
set({'name': 'hello', 'age': 18})
# {'age', 'name'}
```

### 转矩阵
1. list -> 矩阵
```
x = [[1,2,3][1,3,4.5],[1,2,3.4]]
m = np.matrix(x)
```