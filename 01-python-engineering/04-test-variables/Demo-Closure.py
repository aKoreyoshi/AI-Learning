def outer():
    nums = []

    def inner():
        nums.append(1)
        print(nums)

    return inner

f1 = outer()
f2 = outer()

f1()    # [1]
f1()    # [1, 1]
f2()    # [1]
f2()    # [1, 1]