def hello():
    print("Hello")

a = hello
b = a

hello = 123
a = 456

b()             # Hello
print(hello)    # 123
print(a)        # 456