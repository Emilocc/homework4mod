class InfiniteIterator:
    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        self.number += 1
        return self.number

# Создаем объект бесконечного итератора
infinite_iter = InfiniteIterator()

# Используем его в цикле for
for num in infinite_iter:
    print(num)  # Этот цикл никогда не завершится


