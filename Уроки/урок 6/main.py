# class Year:
#     def __int__(self):
#         self.__days = 365
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#
#         else:
#             raise  ValueError(f"В году не может быть {days}дней")
#
#
#
#
#
# year = Year()
# #year.__days = 370
# print(year.get_days())
# year.set_days(366)
# print(year.get_days())

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError(f"Недопусимый возраст {age}")
        self.__age = age


person = Person("Emil", 16)
print(person.age)
person.age = 20
print(person.age)


class CustomList:
    def __init__(self, items=[]):
        self.items = items

    def __repr__(self):
        return str(self.items)

    def append(self, item):
        self.items.append(item)

    def extend(self, items):
        self.items.extend(items)

    def remove(self, item):
        self.items.remove(item)

    def delete_last_item(self):
        if len(self.items) > 0:
            self.items.pop()

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
