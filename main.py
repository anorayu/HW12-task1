from pymystem3 import Mystem

# Создание экземпляра класса Mystem
m = Mystem()

# Получение словарной формы для каждого слова
words = ["слово1", "слово2", "слово3", ..., "слово20"]
lemmas = [m.lemmatize(word)[0] for word in words]

# Вывод словарной формы каждого слова
for word, lemma in zip(words, lemmas):
    print(f"{word} -> {lemma}")


