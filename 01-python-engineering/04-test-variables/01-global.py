count = 0

# def add1():
#     # python会认为count是局部变量，但是count在函数外定义，所以会报错
#     # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#     count = count + 1
#     print(count)
#
# add1()

# def add2():
#     # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#     print(count)
#     # 函数内部定义的变量，默认是局部变量
#     count = 1
#
# add2()


# ---------------------------------------------------------------------------------
nums = []

def add3():
    nums.append(1)

add3()
print(nums)