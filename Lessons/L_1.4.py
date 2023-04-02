from math import factorial
def arrangements(n, k):
    return int(factorial(n) / factorial(n - k))
m=arrangements(20, 5)
print(m)

# В магазине 20 покупателей. Сколькими способами они могут образовать очередь из 5 человек?
# Определить сочетания, размещения или перестановки используются для решения этой задачи - !!! РАЗМЕЩЕНИЯ !!!
