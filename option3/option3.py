# Этот вариант использует модуль re для работы с регулярными выражениями, что позволяет более элегантно находить гласные.
import re  # Импортируем модуль для работы с регулярными выражениями

def count_vowels(input_string):
    return len(re.findall(r'[aeiouAEIOU]', input_string))  # Находим все гласные и возвращаем их количество

# Ввод строки от пользователя
user_input = input("Введите строку: ")
result = count_vowels(user_input)  # Вызов функции для подсчета гласных
print(f"Количество гласных: {result}")  # Вывод результата