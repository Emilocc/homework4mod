import time


# my_list = [time.sleep(x) for x in range(3)]
# my_gen = (time.sleep(x) for x in range(3))

# for item in my_gen:
#     print(item)

# print(type(range(1, 2)))

# def my_lazy_func():
#     for i in range(1,11):
#         print("До", i)
#         yield i
#         print("После", i)
#
#
# for i in my_lazy_func():
#     print(i)


def my_lazy_func(items):
    # for item in items:
    #     yield item
    yield from items


for i_item in my_lazy_func(["Яблоко, Апельсин,КИВИ  "]):
    print(i_item)


