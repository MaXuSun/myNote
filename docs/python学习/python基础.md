1. tuple和list:
    * 区别
        * tuple: 元组'()'，各个元素不可重新赋值
        * list: 列表'[]'，各个元素可重新赋值
    * 引用
        * [下限:上限:步长]，不包括上限; 上限可 < 0
        * 步长<0:倒着取，此时下限 > 上限;
            ```
            print(s[0: 2: -1]) #[]
            print(s[0:-1]) #s[-1]不取
            ```
        * 字符串是tuple
    
2. 运算符号
    * is : 判断引用地址的一致性
    * is not : 同is
    * in : 判断一个元素是否在(list,tuple,……)中，3 in [1,2,3]
    * ** : 幂指运算，3**3 = 27
    * bool运算 : not, or, and
    * del : 用于删除对象， del dic['tom']
3. 循环
    * for循环:
        ```
        for 元素 in 序列:   # for i in range(5):[0,1,2,3,4]
            statement           #print(i)
        ```
    * while循环:
        ```
            while 条件:
                statement
        ```

4. 函数
    * 返回值：可多个,相当于一个tuple; return a,b = return (a,b)
    * 参数
        * 参数本质: 基本数据类型: 值传递。 表等数据机构: 指针传递
        * $\color{red}{参数形式}$：
            ```
            def f(a,b,c):
                return a+b+c
            def f1(a,b,c=10):       # 参数默认值,必须放在最后
                return a+b+c
            def f2(*data,**dic):    #包裹传递,*用于元素,**用于键值
                print(type(data),name)
                print(type(dic),dic)
            
            print(f(1,2,3))         # 位置传递,a=1,b=2,c=3
            print(f(c=1,a=2,b=3))   # 关键字传递,a=2,b=3,c=1
            print(f(1,c=3,b=2))     # 混用,a=1,b=2,c=3

            # 包裹传递
            f2(1,4,5,a=1,b=2,c=3)   # (1,4,5)被打包成tuple,{a=1,b=2,c=3}被打包为dict
            f2(1,2,a=1)             # (1,2)被打包成tuple,{a=1}被打包为dict

            # 解包传递,dic同理。这和打包传递并不是可逆的，两者独立
            args1 = (1,2,3)
            f(*args)
            ```
        * 混合使用：先位置，再参数默认值，再包裹位置
            ```
            def f(arg1,arg2=2,*arg3,**arg4):
                print(type(arg1), arg1) # arg1=1
                print(type(arg2), arg2) # arg2=3
                print(type(arg3), arg3) # arg3=(4,)
                print(type(arg4), arg4) # arg4={'a': 2, 'b': 3}
            f(1, 3, 4,a=2,b=3)
            # 下面是错误写法,只要用了值默认方法，就不能用关键字方法
            f(1,3,4,arg1=2,a=2,b=3)
            f(1,3,4,arg2=2,a=2,b=3)
            
            ```

5. 对象
    * 继承结果和java一样,可对父类的方法进行重写、添加，子类可调用父类方法
    * 定义: 
        ```
        class Obj(Father):  # 括号里是继承的类，根类是object
            attr1 = 123
            def __init__(self,m):
                print('__init__()是初始化方法')
            def method1(self,m1):
                print('test object',self.attr1,m1)
            def method2(self):
                self.method1(m2)
        
        obj = Obj()
        print obj.attr1
        ```
    * 属性: **外部**使用(对象.属性)引用一个对象的所有属性。**内部**使用self.属性引用对象的所有属性
        * self.attr = attr: attr 是对象属性
        * attr = attr : attr 是类属性
    * 方法：方法的第一个参数必须是self,用于引用自身**对象**; 特殊方法使用'__'开头。
    * python中所有非基本类型都是自带的类，所有运算符都是特殊方法，list中的__add__()就是对‘+’的重载

6. 内置函数
    * 辅助函数
        * dir(): 查询一个类或者对象所有属性, dir(list)
        * help(): 查询说明文档
        * len(): 返回list,tuple,dict的长度.对象可对其重写
    * 循环设计
        * range():
            ```
            s='qwertyuioafdfsd'
            for i in range(0,len(s),2): # 和list的取值类似[下限,上限,步长]
            ```
        * enumerate():每次循环中同时取到下标和元素
            ```
            s='qwertyuioafdfsd'
            for (index,key) in enumerate(s):
            ```
        * zip():从多个等长序列中，依次取一个元素，合成一个元组返回
            ```
            d1=[1,2,3,4]
            d2=[4,5,6,7]
            d3=['afd','ert','tyu','dcd']
            for data in zip(d1,d2,d3):    # data=(1,2,'afd')等
            for (a,b,c) in zip(d1,d2,d3): # a=1,b=2,c='afd'
            ```
    * 3个重要函数(EJS中有类似的)
        * map():map(函数,表(s):list,tuple),return:带__next__()的对象，可用list(),tuple()改成对应数据结构
            ```
            # map():依次作用于表的每一个元素
            re = map((lambda x,y:x+y),[1,2,3],[4,5,6])
            print(list(re)) #[5,7,9]
            ```
        * filter():filter(函数,表(s):list,tuple),return:带__next__()的对象,可用list(),tuple()改为对应数据结构
            ```
            # filter():如果函数对象返回的是True,则该次的元素被存储于返回的表中
            re = filter((lambda x,y: return x > y),[2,3,4],[4,3,2])
            print(list(re))
            ```
        * reduce():reduce(函数,表(s):list,tuple),return:带__next__()的对象,可用list(),tuple()改为对应的数据结构
            ```
            # reduce():可以累进地将函数作用域各个参数,在python3.0中只能在functools包中引用
            print(list(reduce(lambda x,y: x+y),[1,2,5,7,9]))    #其执行过程为 ((((1+2)+5)+7)+9)

            ```