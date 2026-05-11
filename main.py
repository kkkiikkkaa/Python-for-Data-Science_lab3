import numpy as np

# 1. Створюємо одновимірний масив з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

# 2. Використовуючи маску, відфільтровуємо всі додатні числа
positive_numbers = arr[arr > 0]

print("\nДодатні числа:")
print(positive_numbers)

# 3. Замінюємо всі від’ємні значення на нулі
modified_arr = arr.copy()
modified_arr[modified_arr < 0] = 0

print("\nМасив після заміни від’ємних чисел на 0:")
print(modified_arr)

# 4. Обчислюємо середнє значення отриманого масиву
average_value = modified_arr.mean()

print("\nСереднє значення отриманого масиву:", average_value)
