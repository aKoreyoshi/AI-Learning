"""
   :author: Kairos
   :description: 描述符的作用
   :version: 1.0
   :date: 2026年07月23日,16:54:46
 """

# 定义一个描述符
class Descriptor:
    def __get__(self, instance, owner):
        print("get 方法执行了")
        print(instance)     # instance 参数为实例对象 <__main__.Person object at 0x0000020E92526A50>
        print(owner)        # owner 参数为当前实例对象对应的类 <class '__main__.Person'>

# 定义一个类
class Person:
    name = Descriptor()

person = Person()
person.name


class User:
    pass

user = User()
user.name = Descriptor()
print(user.name)        # <__main__.Descriptor object at 0x0000020E92704910>

"""
    综上，Descriptor描述符只会在类属性中起作用，而在实例对象中无效。
    也就是 -> 只有Descriptor在类中，python才会将其当做Descriptor；
             但是如果Descriptor在实例对象中，python不会将其当做Descriptor，只会将其当做一个普通对象
"""
