sentence = input("Введіть речення: ")
words = sentence.split()

if all(word.isalpha() for word in words):
    for word in words:
        print(f"Слово '{word}' має {len(word)} літер")
else:
    print("Речення має містити лише слова!")
