1. 词典(dict)
    * 相当于map,词典元素没有顺序，只能通过键来引用
    * 示例代码
        ```
        dic = {}                            # 初始化空词典
        dic = {'tom':11,'sam':57,'jun':12}  # 初始化
        dic['tom'] = 33                     # 修改值
        del dic['sam']                      # 删除dic['sam']

        for key in dic: 
            print(key,dic[key])     # 循环中,**dict的每个键**被赋值给key
        ```

2. 文件操作
    * 过程代码
        ```
        f = open(文件名, 模式, 编码打开方式)    # 可直接打开同级文件
        f = open('test.txt','r',encoding='utf-8') # 其中'test.txt' = './test.txt'
        content = f.read(N)                     # 读N bytes
        content = f.readline()                  # 读一行,包括换行符
        content = f.readlines()                 # 将所有行读如一个list中,每个元素为一行(包括行)
        f.write('I like you')                   # f.writelines([])   写
        f.close()                               # 关闭

        # 根据__next__()自动迭代
        for line in open('123.txt','r',encoding='utf-8'):
            print(line)
        ```
    * vscode中加上下面两句用于定位
        ```
        import os, sys
        os.chdir(sys.path[0])
        ```

3. 模块，包，库
    * 模块：就是**一个.py文件**，导入方式如下
        ```
        import mod
        from mod import method1
        from mod import *
        from mod import method2 as m2
        ```
    * 包：包含**模块们**,**__init__.py**,**或子包**的**文件夹**。包用来将相同类型的模块放在一起，并且可利用__init__.py的自动执行。
        ```
        import test.mod # 在导入的同时会自动执行__init__.py文件

        ```
    * 库：很多包组成的一个完整的项目。如pytorch

4. 循环对象：包含__next__()方法的对象，这时便可用(for in)遍历,其自动调用__next__()方法。通常循环对象和迭代器互指代对方
    * 生成器构造:**将return改为yield**$\{red}{可有多个yield}$,**每次for一下为一次yield值**
        ```
        def gen():      # 生成器
            for i in range(30):
                yield i
        for i in gen():
            print(i)
        ```
    * 表推导
        ```
        # 生成器简便写法和表推导区别在于，一个(),一个[]
        gen = (x for x in range(30))        # gen = gen(),生成器快速写法
        L = [x**2 for x in range(30)]       # 这生成一个表

        # 表推导中可用enumerate和zip
        x1 = [1,3,5]
        y1 = [9,12,13]
        L = [x**2 for (x,y) in zip(x1,y1) if y >10]
        L2 = [key**2 for (index,key) in enumerate(x1) if index > 1]
        ```

5. 函数对象
    * **函数是一种对象**,可赋值给其他对象或者作为参数传递
    * lambda函数：$\{red}{只能有一个表达式}$,不能包含命令
        ```
        L = lambda x,y:x*y
        print(L(2,3))   # 6
        ```
    * 函数作为参数：函数作为一个对象，传入函数
        ```
        def test(f,a,b):
            return f(a,b)
        print(test(L,3,4))                  # 12
        print(test((lambda x,y: x+y),4,5))  # 9
        ```

6. 异常处理
    * 和Java中的异常处理类似
    * 形式
    ```
    # 1. 捕获异常结构
    try: ……
    except exception1: ……
    except exception2: ……
    except: ……
    else: ……
    finally: ……

    # 2. 流程
    try -> 异常 -> except -> finally
    try -> 无异常 -> else -> finally

    # 3. 程序员自己抛出
    raise exception
    ```

7. 动态类型
    * 核心：$\{red}{引用和对象分离}\$，常用的list,tuple,dict等都算对象
    * $\{red}{基本数据类型和对象不同}\$
        ```
        # 基本数据类型
        a = 5
        b = a
        a = a + 2
        # 此时 a = 7,b = 5

        # 对象
        L1 = [1,2,3]
        L2 = L1
        L1[0] = 10
        # 此时 L1 = [10,2,3],L2=[10,2,3]
        ```

