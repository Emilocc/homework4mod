from contextlib import contextmanager


# #file = open("test.txt", "w", encoding="utf-8")
# #file.write("Веб по контекст менеджеру ")
# #file.close()
#
# with open("test.txt", "r", encoding="utf-8") as f:
#     print(f.read())
#     print(f.closed)
#
# print(f.closed)


# @contextmanager
# def reverse_str(string):
#     yield string[::-1]
#
#
# with reverse_str("helo") as reversed_str:
#     print(reversed_str)

@contextmanager
def exc_handler(args):
    try:
        yield True
    except args:
        print("Было искл но меня не волнует ")


with exc_handler(ValueError,):
    raise AttributeError