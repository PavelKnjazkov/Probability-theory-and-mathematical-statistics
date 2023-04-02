from math import factorial
def combinations (n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = combinations (36, 4)
print(f'm = {m}')

# Определить сочетания, размещения или перестановки используются для решения этой задачи. !!! СОЧЕТАНИЯ !!!
# Сколькими способами можно выбрать из колоды, состоящей из 36 карт, 4 карты? 