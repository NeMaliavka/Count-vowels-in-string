# Этот вариант более компактный и использует генератор для подсчета гласных.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Список гласных
    return sum(1 for char in input_string if char in vowels)  # Подсчет гласных с помощью генератора

# Ввод строки от пользователя
user_input = input("Введите строку: ")
result = count_vowels(user_input)  # Вызов функции для подсчета гласных
print(f"Количество гласных: {result}")  # Вывод результата