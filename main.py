def is_palindrome(s):
    # 2. Преобразуем строку к нижнему регистру
    s = s.lower()

    # 3. Оставляем только буквы и цифры
    cleaned = ''.join(char for char in s if char.isalnum())

    # 4. Создаём перевёрнутую версию строки
    reversed_cleaned = cleaned[::-1]

    # 5–7. Сравниваем и возвращаем результат
    return cleaned == reversed_cleaned