"""
 * Project name(项目名称)：Python_set集合方法和frozenset集合
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 12:39
 * Version(版本): 1.0
 * Description(描述)：

 方法名	语法格式	功能	实例
add()	set1.add()	向 set1 集合中添加数字、字符串、元组或者布尔类型	>>> set1 = {1,2,3}
>>> set1.add((1,2))
>>> set1
{(1, 2), 1, 2, 3}
clear()	set1.clear()	清空 set1 集合中所有元素	>>> set1 = {1,2,3}
>>> set1.clear()
>>> set1
set()

set()才表示空集合，{}表示的是空字典
copy()	set2 = set1.copy()	拷贝 set1 集合给 set2	>>> set1 = {1,2,3}
>>> set2 = set1.copy()
>>> set1.add(4)
>>> set1
{1, 2, 3, 4}
>>> set1
{1, 2, 3}
difference()	 set3 = set1.difference(set2)	将 set1 中有而 set2 没有的元素给 set3	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set3 = set1.difference(set2)
>>> set3
{1, 2}
difference_update()	set1.difference_update(set2)	从 set1 中删除与 set2 相同的元素	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.difference_update(set2)
>>> set1
{1, 2}
discard()	set1.discard(elem)	删除 set1 中的 elem 元素	>>> set1 = {1,2,3}
>>> set1.discard(2)
>>> set1
{1, 3}
>>> set1.discard(4)
{1, 3}
intersection()	set3 = set1.intersection(set2)	取 set1 和 set2 的交集给 set3	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set3 = set1.intersection(set2)
>>> set3
{3}
intersection_update()	set1.intersection_update(set2)	取 set1和 set2 的交集，并更新给 set1	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.intersection_update(set2)
>>> set1
{3}
isdisjoint()	set1.isdisjoint(set2)	判断 set1 和 set2 是否没有交集，有交集返回 False；没有交集返回 True	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.isdisjoint(set2)
False
issubset()	set1.issubset(set2)	判断 set1 是否是 set2 的子集	>>> set1 = {1,2,3}
>>> set2 = {1,2}
>>> set1.issubset(set2)
False
issuperset()	set1.issuperset(set2)	判断 set2 是否是 set1 的子集	>>> set1 = {1,2,3}
>>> set2 = {1,2}
>>> set1.issuperset(set2)
True
pop()	a = set1.pop()	取 set1 中一个元素，并赋值给 a	>>> set1 = {1,2,3}
>>> a = set1.pop()
>>> set1
{2,3}
>>> a
1
remove()	set1.remove(elem)	移除 set1 中的 elem 元素	>>> set1 = {1,2,3}
>>> set1.remove(2)
>>> set1
{1, 3}
>>> set1.remove(4)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    set1.remove(4)
KeyError: 4
symmetric_difference()	set3 = set1.symmetric_difference(set2)	取 set1 和 set2 中互不相同的元素，给 set3	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set3 = set1.symmetric_difference(set2)
>>> set3
{1, 2, 4}
symmetric_difference_update()	set1.symmetric_difference_update(set2)	取 set1 和 set2 中互不相同的元素，并更新给 set1	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set1.symmetric_difference_update(set2)
>>> set1
{1, 2, 4}
union()	set3 = set1.union(set2)	取 set1 和 set2 的并集，赋给 set3	>>> set1 = {1,2,3}
>>> set2 = {3,4}
>>> set3=set1.union(set2)
>>> set3
{1, 2, 3, 4}
update()	set1.update(elem)	添加列表或集合中的元素到 set1	>>> set1 = {1,2,3}
>>> set1.update([3,4])
>>> set1
{1,2,3,4}
 """

if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5, 6, 7}
    print(set1)
    set1.add(8)
    print(set1)
    set1.add((1, 2))
    print(set1)
    # 返回一个集合的浅拷贝。
    set2 = set1.copy()
    print(set2)
    set1.clear()
    print(set1)
    set1 = {1, 2, 3, 4, 5, 6, 7}
    set1.add(8)
    set1.add(9)
    set1.add(12)
    # 将两个或多个集合的差作为新集合返回。
    # （即该集合中的所有元素，但不是其他元素。）
    set3 = set1.difference(set2)
    print(set3)
    # 从这个集合中移除另一个集合的所有元素。
    set1.difference_update(set2)
    print(set1)
    print(set2)
    set2.discard(2)
    print(set2)
    # 如果它是成员，则从集合中删除一个元素。
    # 如果元素不是成员，则什么也不做。
    set2.discard(0)
    print(set2)
    set4 = {4, 7, 11, 15, 18}
    print(set4)
    # 将两个集合的交集作为新集合返回。
    set5 = set2.intersection(set4)
    print(set5)
    print(set2 & set4)
    # 用它自己和另一个的交集更新一个集合。
    set2.intersection_update(set4)
    print(set2)
    # 如果两个集合有一个空交集，则返回 True。
    print(set2.isdisjoint(set4))
    # 报告另一个集合是否包含该集合。
    print(set2.issubset(set4))
    print(set4.issubset(set2))
    print(set4)
    # 移除并返回任意集合元素。如果集合为空，则引发 KeyError。
    print(set4.pop())
    print(set4)
    print(set4.pop())
    print(set4)
    print(set4.pop())
    print(set4)
    # 从集合中移除一个元素；它必须是成员。
    # 如果元素不是成员，则引发 KeyError。
    set4.remove(11)
    print(set4)
    set6 = {1, 2, 3, 4}
    set7 = {3, 4, 1, 8}
    # 将两个集合的对称差作为新集合返回。
    # （即恰好在一组中的所有元素。）
    set8 = set6.symmetric_difference(set7)
    print(set6)
    print(set7)
    print(set8)
    # 将集合的并集作为新集合返回。
    # （即任一集合中的所有元素。）
    set9 = set6.union(set7)
    print(set9)
    # 用它自己和其他人的并集更新一个集合。
    set9.update([1, 2])
    print(set9)
    set9.update([1, 9])
    print(set9)
    set9.update([77, 13, 87])
    print(set9)

    input()
