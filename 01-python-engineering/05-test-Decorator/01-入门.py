def hello():
    print("Hello, World!")

# 函数名只是一个变量，指向函数对象
print(hello)    # <function hello at 0x000001EE767C72E0>
hello()


# 可以创建一个新的变量new_hello，指向hello函数对象
# hello 和 new_hello 指向同一个函数对象 -> hello()
new_hello = hello

new_hello()