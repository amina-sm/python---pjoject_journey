# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum += n
# #     return sum


# # print(add(2.3, 5, 5))


# # def calculate(n, **kwargs):
# #     print(kwargs)
# #     n += kwargs["add"]
# #     n *= kwargs["multiply"]
# #     print(n)


# # calculate(2, add=3, multiply=5)


# def bar(spam, eggs, toast='yes please', ham=0):
#     print(spam, eggs, toast, ham)


# bar(1, 2)

def test(a, *args, **kwargs):
    print(a, args, kwargs)


test(4, 7, 3, 0, x=10, y=64)
