"""
 * Project name(项目名称)：Python_set集合方法和frozenset集合
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 13:01
 * Version(版本): 1.0
 * Description(描述)： 两种情况下可以使用 fronzenset：
当集合的元素不需要改变时，我们可以使用 fronzenset 替代 set，这样更加安全。
有时候程序要求必须是不可变对象，这个时候也要使用 fronzenset 替代 set。比如，字典（dict）的键（key）就要求是不可变对象。
 """

if __name__ == '__main__':
    s = {1, 2, 3, 4}
    print(s)
    s.add(5)
    print(s)
    s1 = frozenset(s)
    print(s1)
    print(type(s1))

    input()
