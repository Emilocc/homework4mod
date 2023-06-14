# name = input('Введите имя: ')
# salary = int(input('Введите зарплату: '))

# print('У ' + name + ' зарплата составляет ' + str(salary))
# print(f'У {name} зарплата составляет {salary}')

# employee = {
#     'name': 'Дмитрий',
#     'salary': 350_000,
#     'age': 16,
# }
#
# print(employee)
#
# employee['name'] = 'Валера'
#
# print(employee)
#
# print(employee.get('name'), employee.get('salary'), employee.get('age'))

# employees_list = [
#     {
#         'name': 'Валерий',
#         'salary': 200,
#         'age': 4,
#     },
#     {
#         'name': 'Денис',
#         'salary': 20,
#         'age': 16,
#     },
#     {
#         'name': 'Дмитрий',
#         'salary': 0,
#         'age': 15,
#     }
# ]

# for employee in employees_list:
#     print(employee.get('name'))

# employees_list.remove()
# del employees_list[-1]
# print(employees_list)
# employees_list.append(1)
# print(employees_list)


class Employee:
    def __init__(self, name, salary, ):
        self.name = name
        self.salary = salary

    def print_hi(self):
        print("Hi!")


employee1 = Employee('Никита', 200_000)
employee1.print_hi()


# ДЗ

class Employee:
    def __init__(self, name, salary, on_vacation):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation

    def print_hi(self):
        print("Hi!")

    def get_vacation_status(self):
        if self.on_vacation:
            print(f"{self.name} is currently on vacation.")
        else:
            print(f"{self.name} is not on vacation.")


employee1 = Employee('Никита', 200_000, True)
employee1.get_vacation_status()

employee2 = Employee('Мария', 150_000, False)
employee2.get_vacation_status()


class Employee:
    def __init__(self, name, salary, is_good_employee=True):
        self.name = name
        self.salary = salary
        self.is_good_employee = is_good_employee

    def print_hi(self):
        print("Hi!")


employee1 = Employee('Никита', 200_000, True)
employee2 = Employee('Эмиль', 180_000, True)
employee3 = Employee('Леонид', 190_000, True)
employee4 = Employee('Мария', 210_000, True)
employee5 = Employee('Данил', 150_000, False)

employees = [employee1, employee2, employee3, employee4, employee5]

for employee in employees:
    if not employee.is_good_employee:
        employees.pop(employees.index(employee))  # удаляем из списка плохого работника
        print(f"{employee.name} был уволен за нехватку квалификации")

print("Остались только лучшие сотрудники:")
for employee in employees:
    print(employee.name)
