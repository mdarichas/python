word = input("Введіть слово: ")

if word.isalpha():
    print("Голосні:")
    for letter in word:
        if letter in "аеєиіїоуюяАЕЄИІЇОУЮЯ":
            print(letter)

    print("Приголосні:")
    for letter in word:
        if letter not in "аеєиіїоуюяАЕЄИІЇОУЮЯ":
            print(letter)
else:
    print("Слово має містити лише букви!")