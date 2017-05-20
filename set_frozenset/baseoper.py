# -*- coding: utf-8 -*-


"""
describe:

set and frozenset usage of operation

usage:

code style: PEP8
os: Mac

"""

__version__ = "v.1.0"
__author__ = "PyGo"
__time__ = "2017/5/19"
__mail__ = "gaomingliang971366@163.com"

"""
set 无序 可变 唯一 的元素集合
frozenset 无序 不可变 唯一的元素结合
set一种数据类型
使用系统mac
可以进行
交
叉
并
补
的运算
for 。。。 in
推导式
"""

# -------------set operations

# set创建

# set接受迭代器
# string
# tuple
# list
# dict value变成set集合的值

# set 集合推导式
al = [i for i in range(100) if i % 2 == 0]

aset = set(al)
print type(aset)
print aset

# set 可变 因为set对象没有hash值

# 哈希值：将长度不一样的输入数据源，通过算法转换为长度一直的的数据输出，提高查询速度
# MD5：对文件或者数据源（字符串，数值）进行计算得道一个固定的值，
# 用来验证文件或者数据源是否被篡改，一般用于文件签名


# 元素的唯一性
astring = "asdfghjkasdfghjkasdfghjk"
aset = set(astring)
print aset
afrzset = frozenset(astring)
print afrzset

# 增加add()，添加一个元素到set集合末尾
aset = set(range(10))
print aset
aset.add(100)
print aset

# 删除remove()，删除一个set集合中的元素，存在将删除，不存在返回一个错误
# 一次只能删除一个元素
# 无返回值
print aset.remove(100)
# 删除不存在报异常
# KeyError: 100
try:
    print aset.remove(100)
except Exception as e:
    print e.message
    print aset
# pop()删除
# 随机删除一个元素
# 返回删除元素
# 删除空集合将返回错误
print aset.pop()
aset = set()
# KeyError: 'pop from an empty set'
try:
    print aset.pop()
except Exception as e:
    print e.message

# discard 删除一个元素，如果删除元素不存在，不做任何措施
# 无返回值
aset = set(range(10))
print aset.discard(5)
# 删除不存在的
print aset.discard(100)

# copy 复制 深拷贝
aset_copy = aset.copy()
print 'copy:', aset_copy
print aset == aset_copy

# clear 清空集合
# 无返回值
print aset.clear()
print aset

# ---------------frozenset operations

"""
frozenset 不可变集合 唯一 
无法进行增删改
最大优点：使用hash实现，查询速度快
frozenset可以使用dict的key作为集合元素
"""

# 创建
# 空不可变集合
afrset = frozenset()
print afrset
# 也可以使用set的string, list, tuple, dict
afrset = frozenset(range(10))
print afrset

# 比较set与frozenset集合
# 得出结论，frozenset是继承了set集合
aset = set(range(10))

print aset == afrset

# frozenset可以作为dict的key, set不可以作为dict的key
adict = {'11': afrset}
print adict
adict = {afrset: '123'}
print adict

# ---------------set frozenset 共有的内建函数
"""
交
叉
并
补

内建函数含有update的函数，frozenset是禁止使用的（不可变）

"""

# ###### 交集 intersection 返回集合的交集 可传递不同的交集类型对象

# 只有集合与集合求交集才可以可以用符号 "&" 代替
# 集合 & 集合 (set or frozenset)
aset1 = set(range(10))
aset2 = set(range(5, 10, 1))

aset_intersection = aset1.intersection(aset2)
print aset_intersection
aset_intersection = aset1 & aset2
print aset_intersection

# 集合 & 列表
alist = [i for i in range(10)]
print aset2.intersection(alist)

# set & tuple
atuple = (i for i in range(10))
print aset2.intersection(atuple)

# set & string
astring = "".join(str(range(10)))
print astring
print aset2.intersection(astring)

# set & dict
# 只与字典中的key进行交集
adict = {1: 1, 2: 2}
print aset1.intersection(adict)

# ###### 交集 intersection_update 返回集合的交集
# 把交集的结果返回给取交集的原对象
aset = set(range(10))
print "source: ", aset
alist = [2, 3, 4, 5]
aset.intersection_update(alist)
print "update: ", aset

# ###### 并集 union 返回集合的并集

# 只有集合与集合求并集才可以可以用符号 "|" 代替
# 集合 & 集合 (set or frozenset)
aset1 = set(range(10))
aset2 = set(range(5, 10, 1))

aset_union = aset1.union(aset2)
print aset_union
aset_union = aset1 | aset2
aset_inter = aset1 & aset2
print "intersection: ", aset_inter
print "union: ", aset_union

# 集合 | 列表
alist = [i for i in range(10)]
print aset2.union(alist)

# set | tuple
atuple = (i for i in range(10))
print aset2.union(atuple)

# set | string
astring = "".join(str(range(10)))
print astring
print aset2.union(astring)

# set | dict
# 只与字典中的key进行并集
adict = {1: 1, 2: 2}
print aset1.union(adict)

# ###### 并集 update 返回集合的并集给数据源集合对象

aset1.update(aset2)
print 'union aset1: ', aset1

# ###### 差 difference 求集合对象之间的差， 返回一个新的集合
# 求差对象也可是list，tuple，dict，string
# 可以用 "-" 代替使用
aset3 = aset1.difference(aset2)
print 'difference:', aset3
print aset1.difference(astring)
print aset1.difference(alist)
print aset1.difference(atuple)
print aset1 - aset2

# ###### difference_update 返回集合之间的赋值原集合对象
aset1.difference_update(aset2)
print aset1

# ###### symmetric_difference 返回集合之间彼此之间的差值生产新的集合对象
# 求的是（set1 - set2 |（set2 - set1）
# "^" 代替
# 求差对象也可是list，tuple，dict，string

as1 = {1, 2, 3, 4, 5, "sa"}
as2 = {4, 5, 6, 7, "sa"}
as3 = as1.symmetric_difference(as2)
print "symmetric_difference:", as3
as4 = as1 ^ as2
print "symmetric_difference:", as4

# ###### symmetric_difference_update 返回集合之间彼此的差值赋值原集合对象
# 求的是（set1 - set2 |（set2 - set1）
# 求差对象也可是list，tuple，dict，strin
aset1.symmetric_difference_update(aset2)
print "symmetric_difference_update: ", aset1

# ########## 集合之间的关系
"""
相等：2个set集合相同元素时，相等比较对象可以是set与frozenset
大于：一个集合是另一个集合的超集
小于：一个集合是另一个集合的子集
"""
aset1 = set(range(10))
aset2 = set(range(3, 12, 1))

# 判断是否相等, 返回True 或者 False
# 用 "=="
print aset1 == aset2

# isdisjoint 判断是否相交, 返回True 或者 False
print aset2.isdisjoint(aset1)

# 判断是否相交，子集，超集，可以用<=; >= 进行判断

# issuperset 判断一个集合是否包含另一个集合 返回True 或者 False

print aset1.issuperset(aset2)

# issubset 判断一个集合是否是另一个集合的子集 返回True 或者 False
print aset2.issubset(aset1)

# ############ 集合与其他数据类型的转换

aset = set(range(10))
alist = [i for i in range(10)]
atuple = (i for i in range(10))
astring = '12345789'
adict = {1: "1", 2: "2", 3: "3"}
print "set transfer to list string tuple dict:"
print 'set: ', aset
print 'list: ', alist
print 'string: ', astring
print 'tuple: ', atuple
print 'dict: ', adict

# list
aset_to_list = list(aset)
print 'set to list: ', type(aset_to_list), aset_to_list
alist_to_set = set(alist)
print 'list to set: ', type(alist_to_set), alist_to_set
# string
aset_to_string = str(aset)
print 'set to string: ', type(aset_to_string), aset_to_string
astring_to_set = set(astring)
print 'string to set: ', type(astring_to_set), astring_to_set
# dict
adict_to_set = set(adict)
print 'set to dict: ', type(adict_to_set), adict_to_set
aset_to_dict = dict(enumerate(aset))
print 'set to dict: ', type(aset_to_dict), aset_to_dict
# tuple
aset_to_tuple = tuple(atuple)
print 'set to tuple: ', type(aset_to_tuple), aset_to_tuple
atuple_to_set = set(aset)
print 'tuple to set: ', type(atuple_to_set), atuple_to_set


# ############ 成员关系判断
print 'k' in aset
